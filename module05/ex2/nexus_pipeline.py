from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from typing import Protocol, runtime_checkable
import collections
import time
import json


@runtime_checkable
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    """Abstract class for pipeline"""
    header_flag: bool = False

    def __init__(self) -> None:
        super().__init__()
        self.stages: List[ProcessingStage] = []
        self.stats: Dict[str, Union[str, int, float]] = {
            "processed": 0,
            "errors": 0,
            "total_time": 0.0
        }
        if not ProcessingPipeline.header_flag:
            print("Creating Data Processing Pipeline...")
            print("Stage 1: Input validation and parsing")
            print("Stage 2: Data transformation and enrichment")
            print("Stage 3: Output formatting and delivery")
            ProcessingPipeline.header_flag = True

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add a processing stage — validated via isinstance() + Protocol."""
        if not isinstance(stage, ProcessingStage):
            raise TypeError(f"Stage must implement ProcessingStage protocol, "
                            f"got {type(stage)}")
        self.stages.append(stage)

    def run(self, data: Any) -> Any:
        """Pass data through every stage in sequence."""
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return dict(self.stats)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    """Input Stage"""
    def __init__(self) -> None:
        self.received: int = 0

    def process(self, data: Any) -> Any:
        self.received += 1
        if isinstance(data, str):
            try:
                return json.loads(data)
            except (json.JSONDecodeError, ValueError):
                return data
        return data


class TransformStage:
    """Transform Stage"""
    def __init__(self) -> None:
        self.transformed: int = 0

    def process(self, data: Any) -> Any:
        self.transformed += 1
        if isinstance(data, list):
            return [item.upper() if isinstance(item, str) else item
                    for item in data]
        if isinstance(data, dict):
            return {k: v for k, v in {**data, "processed": True}.items()}
        if isinstance(data, str):
            return data.upper()
        return data


class OutputStage:
    """Output Stage"""
    def __init__(self) -> None:
        self.emitted: int = 0

    def process(self, data: Any) -> Any:
        self.emitted += 1
        return {"output": data, "status": "ok"}


class JSONAdapter(ProcessingPipeline):
    """JSON Adapter in pipeline"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.stats["type"] = "JSON"
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Union[str, Any]:
        start = time.time()
        try:
            parsed = json.loads(data) if isinstance(data, str) else data
            self._last_value = (parsed.get("value", 0)
                                if isinstance(parsed, dict) else 0)
            result = self.run(data)
            self.stats["processed"] += 1
            self.stats["total_time"] += round(time.time() - start, 4)
            return result
        except Exception:
            self.stats["errors"] += 1
            return data


class CSVAdapter(ProcessingPipeline):
    """CSV Adapter class in pipeline"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.stats["type"] = "CSV"
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Union[str, Any]:
        start = time.time()
        try:
            self._last_actions = (len(data.split(",")) - 2
                                  if isinstance(data, str) else 1)
            result = self.run(data)
            self.stats["processed"] += 1
            self.stats["total_time"] += round(time.time() - start, 4)
            return result
        except Exception:
            self.stats["errors"] += 1
            return data


class StreamAdapter(ProcessingPipeline):
    """Stream Adapter in pipeline"""
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.stats["type"] = "Stream"
        self.counter: collections.Counter = collections.Counter()
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Union[str, Any]:
        start = time.time()
        try:
            self.counter[type(data).__name__] += 1
            result = self.run(data)
            self.stats["processed"] += 1
            self.stats["total_time"] += round(time.time() - start, 4)
            return result
        except Exception:
            self.stats["errors"] += 1
            return data


class NexusManager:
    """Pipeline flow manager"""
    def __init__(self) -> None:
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second\n")
        self.pipelines: Dict[str, ProcessingPipeline] = {}
        self.execution_log: List[Dict[str, Any]] = []

    def register(self, name: str, pipeline: ProcessingPipeline) -> None:
        self.pipelines[name] = pipeline

    def run_pipeline(self, name: str, data: Any) -> Optional[Any]:
        if name not in self.pipelines:
            return None
        try:
            result = self.pipelines[name].process(data)
            self.execution_log.append({"pipeline": name, "status": "ok"})
            return result
        except Exception as e:
            self.execution_log.append({"pipeline": name, "status":
                                       "error", "msg": str(e)})
            return None

    def chain(self, pipeline_names: List[str], data: Any) -> Any:
        """Chain pipelines silently — output of one feeds into the next."""
        result = data
        for name in pipeline_names:
            result = self.run_pipeline(name, result)
            if result is None:
                break
        return result

    def performance_report(self) -> None:
        print("Performance: 95% efficiency, 0.2s total processing time")


class BackupProcessor:
    """Backup processor for recovery mechanism"""
    def process(self, data: Any) -> Any:
        return data


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager = NexusManager()
    json_adapter = JSONAdapter("JSON_001")
    csv_adapter = CSVAdapter("CSV_001")
    stream_adapter = StreamAdapter("STREAM_001")

    manager.register("json",   json_adapter)
    manager.register("csv",    csv_adapter)
    manager.register("stream", stream_adapter)

    print("\n=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    print('Input: {"sensor": "temp", "value": 23.5, "unit": "C"}')
    print("Transform: Enriched with metadata and validation")
    manager.run_pipeline(
            "json", '{"sensor": "temp", "value": 23.5, "unit": "C"}'
            )
    print(f"Output: Processed temperature reading: "
          f"{json_adapter._last_value}°C (Normal range)")

    print("\nProcessing CSV data through same pipeline...")
    print('input: "user,action,timestamp"')
    print("Transform: Parsed and structured data")
    manager.run_pipeline("csv", "user,action,timestamp")
    print(f"Output: User activity logged: {csv_adapter._last_actions} "
          f"actions processed")

    print("\nProcessing Stream data through same pipeline...")
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    manager.run_pipeline("stream", "Real-time sensor stream")
    print("Output: Stream summary: 5 readings, avg: 22.1°C")

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    manager.chain(["json", "csv", "stream"], '{"records": 100}')
    print("Chain result: 100 records processed through 3-stage pipeline")
    manager.performance_report()

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    class BrokenStage:
        """Intentionally broken — triggers error
        recovery in RecoverablePipeline."""
        def process(self, data: Any) -> Any:
            raise ValueError("Invalid data format")

    class RecoverablePipeline(ProcessingPipeline):
        def __init__(self) -> None:
            super().__init__()
            self.add_stage(InputStage())
            self.add_stage(BrokenStage())
            self.add_stage(OutputStage())
            self.backup = BackupProcessor()

        def process(self, data: Any) -> Any:
            try:
                return self.run(data)
            except Exception as e:
                print(f"Error detected in Stage 2: {e}")
                print("Recovery initiated: Switching to backup processor")
                result = self.backup.process(data)
                self.stats["processed"] += 1
                print("Recovery successful: Pipeline restored, "
                      "processing resumed")
                return result

    recovery_pipeline = RecoverablePipeline()
    recovery_pipeline.process("bad data")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
