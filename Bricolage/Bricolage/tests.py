if __name__=="__main__":
  import os
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


from models import Item, User
import random


def rand_int(low, high):
  return int(random.random()*(high-low))+low

def populate_sample_items():

  num_items = 30
  lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum".split(" ")

  user = User.objects.get(username="sampleUser")

  for i in range(num_items):
    item = Item()

    item.owner = user

    item.name = " ".join(random.sample(lorem, rand_int(3,10)))
    item.description = " ".join(random.sample(lorem, rand_int(10,20)))

    item.quantity = rand_int(0,7)
    item.cost = float(rand_int(0,10))

    item.save()

  print "{} sample entries added!".format(num_items)

