from people import People


class Client(People):
    def buy_item(self, item: str):
        return 'The value of the item is 10 dollars'
