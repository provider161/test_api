from fixtures.api import ApiFixture
import pytest
import jsonpickle
import os


def load_config_from_file(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as cf:
        configuration = jsonpickle.decode(cf.read())
    return configuration


@pytest.fixture
def api(request):
    config = load_config_from_file(request.config.getoption("--config"))
    base_url = config['base_url']
    path = config['path']
    params = config['params']
    fixture = ApiFixture(base_url=base_url, path=path, params=params)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json")