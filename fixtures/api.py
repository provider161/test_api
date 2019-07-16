from helpers.api import RoamingHelper


class ApiFixture:

    def __init__(self, base_url, path, params):
        self.base_url = base_url
        self.params = params
        self.path = path
        self.roaming = RoamingHelper(self)
