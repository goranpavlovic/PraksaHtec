__author__ = 'vladimir'

from __observer__.Publisher import Publisher


class TechForum(Publisher):

    def __init__(self):
        self.all_users = []        # A list of all users
        self.post_name = None

    # Adding user in the list of all users
    def register(self, user_obj):
        if user_obj not in self.all_users:
            self.all_users.append(user_obj)

    # Removing user from the list of all users
    def unregister(self, user_obj):
        if user_obj in self.all_users:
            self.all_users.remove(user_obj)

    # For all users in the list notify every user
    def notify_all(self):
        for item in self.all_users:
            item.notify(self.post_name)

    def write_new_post(self, post_name):
        self.post_name = post_name

        self.notify_all()


