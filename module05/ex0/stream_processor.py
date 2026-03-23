from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Base Class"""
    def __init__(self) -> None:
        """initialization method"""
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """abstract method for processing data"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """abstract method for validating data"""
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        """abstract method for formatting output"""
        pass


class NumericProcessor(DataProcessor):
    """Specialized class: Numeric"""
    def __init__(self) -> None:
        """initialization class"""
        super().__init__()
        self.data: Any = None
        self.count: int = 0

    def process(self, data: Any) -> str:
        """processing method for numeric data"""
        print(f"Processing data: {data}")
        self.data = data
        try:
            if not self.validate(self.data):
                self.format_output("False")
                raise Exception
                return ""
            print("Validation: Numeric data verified")
            self.format_output("True")
        except Exception as message:
            print(f"{message}")
        return ""

    def validate(self, data: Any) -> bool:
        """validating method for numeric data"""
        for self.count, element in enumerate(data):
            if not isinstance(element, int):
                return False
        return True

    def format_output(self, result: str) -> str:
        """formatting output for numeric data"""
        try:
            if result == "True":
                print(f"Output: Processed {self.count + 1} numeric values, "
                      f"sum={sum(self.data)}, "
                      f"avg={sum(self.data) / self.count}")
            else:
                raise Exception
            return ""
        except Exception as message:
            print(f"{message}")


class TextProcessor(DataProcessor):
    """Specialized class: Text"""
    def __init__(self) -> None:
        """initialization method"""
        super().__init__()
        self.data: Any = None
        self.count: int = 0

    def process(self, data: Any) -> str:
        """processing method for textual data"""
        print(f"Processing data: {data}")
        self.data = data
        try:
            if not self.validate(self.data):
                self.format_output("False")
                raise Exception
                return ""
            print("Validation: Text data verified")
            self.format_output("True")
            return ""
        except Exception as message:
            print(f"{message}")

    def validate(self, data: Any) -> bool:
        """validating method for textual method"""
        for self.count, element in enumerate(data):
            if not isinstance(element, str):
                return False
        return True

    def format_output(self, result: str) -> str:
        """formatting method for textual data"""
        try:
            if result == "True":
                print(f"Output: Processed text: {self.count + 1} characters, "
                      f"{len(self.data.split(' '))} words")
            else:
                raise Exception
            return ""
        except Exception as message:
            print(f"{message}")


class LogProcessor(DataProcessor):
    """Specialized class: Log"""
    def __init__(self) -> None:
        """initialization method"""
        super().__init__()
        self.data: Any = None
        self.log: str = None
        self.entry: str = None
        self.count: int = 0

    def process(self, data: Any) -> str:
        """processing method for log data"""
        print(f"Processing data: {data}")
        self.data = data
        self.log, self.entry = self.data.split(':')
        try:
            if not self.validate(self.data):
                self.format_output("False")
                raise Exception
                return ""
            print("Validation: Text data verified")
            self.format_output("True")
            return ""
        except Exception as message:
            print(f"{message}")

    def validate(self, data: Any) -> bool:
        """validating method for log data"""
        for element in data:
            if not isinstance(element, str):
                return False
        if self.log != "ERROR" and self.log != "INFO":
            return False
        return True

    def format_output(self, result: str) -> str:
        """formatting method for log data"""
        try:
            if result == "True":
                if self.log == "ERROR":
                    print(f"Output: [ALERT]: {self.log} level detected: "
                          f"{self.entry}")
                else:
                    print(f"Output: [{self.log}]: {self.log} level detected: "
                          f"{self.entry}")
            else:
                raise Exception
            return ""
        except Exception as message:
            print(f"{message}")


def main() -> None:
    """program orchestrator"""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    num_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    num_proc.process(num_data)
    print("\nInitializing Text Processor...")
    txt_proc = TextProcessor()
    txt_proc.process(text_data)
    print("\nInitalizing Log Processor...")
    log_proc = LogProcessor()
    log_proc.process(log_data)

    def polymorphic_demo() -> None:
        """polymorphic method"""
        print("\n=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")
        print("Result 1: ", end="")
        num_proc.format_output("True")
        print("Result 2: ", end="")
        txt_proc.format_output("True")
        print("Result 3: ", end="")
        log_proc.format_output("True")
    polymorphic_demo()


if __name__ == "__main__":
    """program entry point"""
    main()
