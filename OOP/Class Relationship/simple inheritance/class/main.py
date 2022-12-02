from client import Client
from collaborator import Collaborator

client = Client('Jhonata', "123", 'email@email.com')
collaborator = Collaborator('Figueredo', '321', 'email@email.com.br', 1)

print(client.buy_item('Ball'),
      '\n',
      client.update_data(),
      '\n',
      collaborator.promoted_office(),
      '\n',
      collaborator.retire_from_office(),
      '\n',
      collaborator.update_data())
