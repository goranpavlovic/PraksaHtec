__author__ = 'vladimir'

from __observer__.Subscriber import Subscriber


class User1(Subscriber):

    def __init__(self):
        pass

    def notify(self, post_name):
        print('User1 notified of a new post %s' % post_name)


class User2(Subscriber):

    def __init__(self):
        pass

    def notify(self, post_name):
        print('User2 notified of a new post %s' % post_name)


class SisterSites(Subscriber):
    def __init__(self):
        self._sisterWebsites = ["Site1", "Site2", "Site3"]

    def notify(self, postname):
        for site in self._sisterWebsites:
            print("Sent notification to site: %s" % site)


