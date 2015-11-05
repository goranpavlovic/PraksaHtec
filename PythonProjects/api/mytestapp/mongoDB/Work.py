__author__ = 'vladimir'


from Mongo import *
from mongoengine.context_managers import switch_db

# for user in User.objects:
#     print('First Name: ' + user.first_name + ' Last Name: ' + user.last_name)
#
# num = User.objects.count()
#
# print("Number of users: %s" % num)
#
# for user in User.objects:
#     user.delete()
#
# num = User.objects.count()

# with switch_db(User, 'archive-user-db') as User:
#     User(name="Ross").save()

user_1 = User()
user_1.save()

