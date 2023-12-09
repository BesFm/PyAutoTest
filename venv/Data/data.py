from dataclasses import dataclass

@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_Address: str = None
    permanent_Address: str = None