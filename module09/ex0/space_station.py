import sys
from datetime import datetime
try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError as error:
    print(f"Error: {error}")
    sys.exit(1)


class SpaceStation(BaseModel):
    """Definition of SpaceStation object, which will ensure data is correct"""
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    """Main function to test implementation"""
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(station_id="ISS001",
                               name="International Space Station",
                               crew_size=6,
                               power_level=85.5,
                               oxygen_level=92.3,
                               last_maintenance="2024-01-15T09:30:00")
    except ValidationError as error:
        print(f"{error}")
        sys.exit(1)

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not operational")
    print("\n========================================")
    print("Expected validation error:")
    try:
        SpaceStation(station_id="ISS002",
                     name="National Space Station",
                     crew_size=23,
                     power_level=86.3,
                     oxygen_level=93.2,
                     last_maintenance="2024-01-15T09:30:00",
                     is_operational=False)  # noqa F841
    except ValidationError as error:
        print(f"{error}")
        sys.exit(1)


if __name__ == "__main__":
    """Program entry point"""
    main()
