

def test_check_roaming_data(api):
    pattern = 'prod*'
    region_is_int = api.roaming.check_region_is_int()
    product_matches_pattern = api.roaming.check_roaming_product(pattern)
    assert region_is_int == True
    assert product_matches_pattern == True