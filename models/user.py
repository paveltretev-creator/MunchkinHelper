from dataclasses import dataclass


@dataclass
class User:
    login: str
    age: int
    email: str