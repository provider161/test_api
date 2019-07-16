import requests
import re


class RoamingHelper:

    def __init__(self, api):
        self.api = api

    def get_roaming_data(self):
        url = ''.join((self.api.base_url, self.api.path))
        request = requests.get(url=url, params=self.api.params)
        data = request.json()
        return data

    def check_region_is_int(self):
        data = self.get_roaming_data()['data']
        is_integer = None
        for region in data:
            if not re.match('\D+', region['regionId']):
                is_integer = True
            else:
                is_integer = False
                print(f'Region {region} is not integer')

        return is_integer

    def check_roaming_product(self, pattern):
        data = self.get_roaming_data()['data']
        matches_pattern = None
        for product in data:
            if re.match(pattern, product['roamingProductId']):
                matches_pattern = True
            else:
                matches_pattern = False
                print(f'Product {product} does not match pattern')
        return matches_pattern