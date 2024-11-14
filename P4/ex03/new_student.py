import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = None
    id: str = None

    def __init__(self, **kwags):
        try:
            print(len(kwags))
            if not kwags['name'] and not kwags['surname'] and len(kwags) != 2:
                raise TypeError("")
            self.name = kwags['name']
            self.surname = kwags['surname']
            self.id = generate_id()
        except (Exception, TypeError):
            print("Error")
