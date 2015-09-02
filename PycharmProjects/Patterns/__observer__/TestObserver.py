__author__ = 'vladimir'

from __observer__.TechForum import TechForum
from __observer__.Users import *

print("------------ TEST OBSERVER --------------")

tf1 = TechForum()

user1 = User1()
user2 = User2()

sister = SisterSites()

tf1.register(user1)
tf1.register(sister)
tf1.register(user1)


tf1.write_new_post("Design Patterns practice")

tf1.register(user2)

tf1.write_new_post("Design Patterns practice - OBSERVER")

tf1.unregister(sister)


