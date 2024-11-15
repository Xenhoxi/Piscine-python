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
            unexpected = set(kwags) - {'name', 'surname'}
            unexpected = list(unexpected)
            if unexpected:
                msg = "Student.__init__() got an unexpected keyword argument"
                raise TypeError(f"{msg} {', '.join(unexpected)}")
            if not kwags['name'] or not kwags['surname']:
                raise TypeError("Student.__init__() missing keyword argument")
            self.name = kwags['name']
            self.surname = kwags['surname']
            self.id = generate_id()
            self.login = self.name[0] + self.surname[:7]
        except (Exception, TypeError) as err:
            print("TypeError:", err)
