import sys
from datetime import datetime
from enum import Enum
from typing import Self
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError as error:
    print(f"Error: {error}")
    sys.exit(1)


class ContactType(Enum):
    """Enum to check valid contact types"""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Alien contact class with pydantic checks"""
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def custom_validation(self) -> Self:
        """custom validation with model_validator"""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError("Strong signals require received messages")
        return self


def main() -> None:
    """main function to show output"""
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        alien = AlienContact(contact_id="AC_2024_001",
                             timestamp="2024-01-15T09:30:00",
                             location="Area 51, Nevada",
                             contact_type="radio",
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=5,
                             message_received="'Greetings from Zeta Reticuli'")
    except ValidationError as message:
        print(f"{message}")
        sys.exit(1)

    print("Valid contact report:")
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type.value}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witnesses: {alien.witness_count}")
    print(f"Message: {alien.message_received}")
    print("======================================\n")
    print("Expected validation error:")
    try:
        AlienContact(contact_id="AC_2024_001",
                     timestamp="2024-01-15T09:30:00",
                     location="Area 51, Nevada",
                     contact_type="telepathic",
                     signal_strength=8.5,
                     duration_minutes=45,
                     witness_count=1,
                     message_received="'Greetings from Zeta Reticuli'")
    except ValidationError as message:
        print(f"{message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
