from dataclasses import dataclass


@dataclass
class Employee:
    id: str
    name: str
    experience: int
    department: str
    role: str
    skills: str
    location: str
    employment_type: str

    def to_document(self) -> str:
        return (
            f"{self.role} with {self.experience} years of experience in "
            f"{self.department}. Skills: {self.skills}. "
            f"Located in {self.location}. "
            f"Employment type: {self.employment_type}."
        )

    def to_metadata(self):
        return {
            "name": self.name,
            "department": self.department,
            "role": self.role,
            "experience": self.experience,
            "location": self.location,
            "employment_type": self.employment_type,
        }
