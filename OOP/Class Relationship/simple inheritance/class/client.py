from person import Person


class Client(Person):
    def buy_item(self, item: str):
        return 'The value of the item is 10 dollars'
