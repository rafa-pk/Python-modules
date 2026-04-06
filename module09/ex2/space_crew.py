import sys
from datetime import datetime
from enum import Enum
from typing import Self, List
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError as error:
    print(f"Error: {error}")
    sys.exit(1)


class Rank(Enum):
    """Enum containing ranks"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """pydantic model for crew member"""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """pydantic model for space mission"""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> Self:
        """mission model_validator"""
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")
        if (not any(member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
                    for member in self.crew)):
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")
        inexperienced = [member for member in self.crew
                         if member.years_experience < 5]
        if (self.duration_days > 365
                and len(inexperienced) / len(self.crew) > 0.5):
            raise ValueError("Long missions (> 365 days) need "
                             "50% experienced crew (5+ years)")
        if [member.is_active for member in self.crew if not member.is_active]:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    """tester script"""
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        sarah = CrewMember(member_id="SC_SM_01", name="Sarah Connor",
                           rank="commander", age=27,
                           specialization="Mission Command",
                           years_experience=6)

        john = CrewMember(member_id="JS_SM_02", name="John Smith",
                          rank="lieutenant", age=34,
                          specialization="Navigation", years_experience=9)

        alice = CrewMember(member_id="AJ_SM_03", name="Alice Johnson",
                           rank="officer", age=45,
                           specialization="Officer", years_experience=15)

        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars",
                               launch_date="2024-01-15T09:30:00",
                               duration_days=900,
                               crew=[sarah, john, alice],
                               budget_millions=2500.0)
    except ValidationError as error:
        print(f"{error}")
        sys.exit(1)

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    print(f"- {mission.crew[0].name} ({mission.crew[0].rank.value}) "
          f"- {mission.crew[0].specialization}")
    print(f"- {mission.crew[1].name} ({mission.crew[1].rank.value}) "
          f"- {mission.crew[1].specialization}")
    print(f"- {mission.crew[2].name} ({mission.crew[2].rank.value}) "
          f"- {mission.crew[2].specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(mission_id="M2024_MARS",
                     mission_name="Mars Colony Establishment",
                     destination="Mars",
                     launch_date="2024-01-15T09:30:00",
                     duration_days=900,
                     crew=[john, alice],
                     budget_millions=2400.0)
    except ValidationError as error:
        print(f"{error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
