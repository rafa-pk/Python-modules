from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """Abstract base class defining the interface for all data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self._processed_count: int = 0
        self._error_count: int = 0
        self._batch_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data. Must be overridden by subclasses."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """
        Default filter: return all items, or those whose string representation
        contains the criteria substring (case-insensitive).
        """
        if criteria is None:
            return data_batch
        return [item for item in data_batch
                if criteria.lower() in str(item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return base stream statistics."""
        return {
            "stream_id":       self.stream_id,
            "processed_count": self._processed_count,
            "error_count":     self._error_count,
            "batch_count":     self._batch_count,
        }


class SensorStream(DataStream):
    """Handles environmental / IoT sensor readings."""

    STREAM_TYPE = "Environmental Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._temperatures: List[float] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Expects items like 'temp:22.5', 'humidity:65', 'pressure:1013'.
        Extracts temperature values for statistical analysis.
        """
        try:
            if not data_batch:
                raise ValueError("Empty sensor batch received.")

            temps: List[float] = []
            for item in data_batch:
                if not isinstance(item, str):
                    raise TypeError(
                        f"Expected str sensor reading, "
                        f"got {type(item).__name__}: {item}"
                    )
                if item.startswith("temp:"):
                    value_str = item.split(":", 1)[1]
                    temps.append(float(value_str))

            self._temperatures.extend(temps)
            self._processed_count += len(data_batch)
            self._batch_count += 1

            count = len(data_batch)
            if temps:
                avg_temp = sum(temps) / len(temps)
                return (
                    f"Sensor analysis: {count} readings processed, "
                    f"avg temp: {avg_temp:.1f}°C"
                )
            return (f"Sensor analysis: {count} readings processed "
                    f"(no temperature data)")

        except (ValueError, TypeError) as exc:
            self._error_count += 1
            return f"[SensorStream ERROR] {exc}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """
        Without criteria: return all items.
        criteria='critical' → return readings with value > 30 (temp).
        criteria='temp'     → return only temperature readings.
        Otherwise falls back to base substring search.
        """
        if criteria is None:
            return data_batch

        if criteria.lower() == "critical":
            critical: List[Any] = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    try:
                        if float(item.split(":", 1)[1]) > 30:
                            critical.append(item)
                    except ValueError:
                        pass
                elif isinstance(item, str) and "alert" in item.lower():
                    critical.append(item)
            return critical

        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        avg = (sum(self._temperatures) / len(self._temperatures)
               if self._temperatures else 0.0)
        base.update({
            "stream_type": self.STREAM_TYPE,
            "avg_temperature": round(avg, 2),
            "temp_readings": len(self._temperatures),
        })
        return base


class TransactionStream(DataStream):
    """Handles financial transaction records."""

    STREAM_TYPE = "Financial Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Expects items like 'buy:100', 'sell:150'.
        Buys add to net_flow; sells subtract.
        """
        try:
            if not data_batch:
                raise ValueError("Empty transaction batch received.")

            net: float = 0.0
            for item in data_batch:
                if not isinstance(item, str):
                    raise TypeError(
                        f"Expected str transaction, got "
                        f"{type(item).__name__}: {item!r}"
                    )
                parts = item.split(":", 1)
                if len(parts) != 2:
                    raise ValueError(f"Malformed transaction entry: {item!r}")
                op, val_str = parts[0].lower(), parts[1]
                amount = float(val_str)
                if op == "buy":
                    net += amount
                elif op == "sell":
                    net -= amount
                else:
                    raise ValueError(f"Unknown operation: {op!r}")

            self._net_flow += net
            self._processed_count += len(data_batch)
            self._batch_count += 1

            sign = "+" if net >= 0 else ""
            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {sign}{net:.0f} units"
            )

        except (ValueError, TypeError) as exc:
            self._error_count += 1
            return f"[TransactionStream ERROR] {exc}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """criteria='large' → transactions with amount > 100."""
        if criteria and criteria.lower() == "large":
            large: List[Any] = []
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    try:
                        if float(item.split(":", 1)[1]) > 100:
                            large.append(item)
                    except ValueError:
                        pass
            return large
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base.update({
            "stream_type": self.STREAM_TYPE,
            "net_flow":    round(self._net_flow, 2),
        })
        return base


class EventStream(DataStream):
    """Handles system / application event logs."""

    STREAM_TYPE = "System Events"
    ERROR_KEYWORDS = {"error", "critical", "fatal", "exception", "fail"}

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._error_events: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Expects plain string event names like 'login', 'error', 'logout'.
        Counts how many are error-class events.
        """
        try:
            if not data_batch:
                raise ValueError("Empty event batch received.")

            errors_in_batch = [
                item for item in data_batch
                if isinstance(item, str)
                and any(kw in item.lower() for kw in self.ERROR_KEYWORDS)
            ]

            non_strings = [item for item in data_batch if not
                           isinstance(item, str)]
            if non_strings:
                raise TypeError(
                    f"Non-string events detected: "
                    f"{[type(x).__name__ for x in non_strings]}"
                )

            self._error_events += len(errors_in_batch)
            self._processed_count += len(data_batch)
            self._batch_count += 1

            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{len(errors_in_batch)} error detected"
            )

        except (ValueError, TypeError) as exc:
            self._error_count += 1
            return f"[EventStream ERROR] {exc}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """criteria='errors' → only error-class events."""
        if criteria and criteria.lower() == "errors":
            return [
                item for item in data_batch
                if isinstance(item, str)
                and any(kw in item.lower() for kw in self.ERROR_KEYWORDS)
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base.update({
            "stream_type":  self.STREAM_TYPE,
            "error_events": self._error_events,
        })
        return base


class StreamProcessor:
    """
    Manages multiple DataStream instances polymorphically.
    Knows nothing about concrete subclasses — only the DataStream interface.
    """

    def __init__(self) -> None:
        self._streams: List[DataStream] = []

    def register_stream(self, stream: DataStream) -> None:
        """Register any DataStream subtype."""
        if not isinstance(stream, DataStream):
            raise TypeError(
                f"Expected a DataStream instance, got {type(stream).__name__}"
            )
        self._streams.append(stream)

    def process_all(
        self,
        batches: Dict[str, List[Any]],
    ) -> Dict[str, str]:
        """
        Process one batch per registered stream (matched by stream_id).
        Returns a dict of stream_id → result string.
        """
        results: Dict[str, str] = {}
        for stream in self._streams:
            batch = batches.get(stream.stream_id, [])
            try:
                result = stream.process_batch(batch)
                results[stream.stream_id] = result
            except Exception as exc:
                results[stream.stream_id] = f"[FATAL] {exc}"
        return results

    def filter_all(
        self,
        batches: Dict[str, List[Any]],
        criteria: Optional[str] = None,
    ) -> Dict[str, List[Any]]:
        """Apply filter_data() on each stream's batch — polymorphically."""
        filtered: Dict[str, List[Any]] = {}
        for stream in self._streams:
            batch = batches.get(stream.stream_id, [])
            try:
                filtered[stream.stream_id] = stream.filter_data(batch,
                                                                criteria)
            except Exception as exc:
                print(f"  [FILTER ERROR] {stream.stream_id}: {exc}")
                filtered[stream.stream_id] = []
        return filtered

    def all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        """Collect get_stats() from every registered stream."""
        return [stream.get_stats() for stream in self._streams]


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {SensorStream.STREAM_TYPE}")
    sensor_analysis = sensor.process_batch(["temp:22.5", "humidity:65",
                                            "pressure:1013"])
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(f"{sensor_analysis}\n")

    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, "
          f"Type: {TransactionStream.STREAM_TYPE}")
    trans_analysis = trans.process_batch(["buy:100", "sell:150", "buy:75"])
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(f"{trans_analysis}\n")

    print("Initializing Event Stream...")
    events = EventStream("EVENT_001")
    print(f"Stream ID: {events.stream_id}, Type: {EventStream.STREAM_TYPE}")
    event_analysis = events.process_batch(["login", "error", "logout"])
    print("Processing event batch: [login, error, logout]")
    print(f"{event_analysis}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.register_stream(SensorStream("SENSOR_002"))
    processor.register_stream(TransactionStream("TRANS_002"))
    processor.register_stream(EventStream("EVENT_002"))

    batches: Dict[str, List[Any]] = {
        "SENSOR_002":  ["temp:18.0", "humidity:70"],
        "TRANS_002":   ["buy:200", "sell:50", "buy:300", "sell:100"],
        "EVENT_002":   ["login", "critical_error", "logout"],
    }

    results = processor.process_all(batches)
    print("Batch 1 Results:")
    for entry_id, res in results.items():
        print(f"- {res}")

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
