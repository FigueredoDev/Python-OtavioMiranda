from person import Person


class Collaborator(Person):
    def __init__(self, name: str, phone: str, email: str, id: int) -> None:
        super().__init__(name, phone, email)
        self._id = id

    def promoted_office(self):
        return 'You got promoted'

    def retire_from_office(self):
        return 'You retired from office'
