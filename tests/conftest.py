import pytest

def pytest_addoption(parser):
    parser.addoption("--step", action="store", default="default step")


@pytest.fixture(scope='session')
def step(request):
    step_value = request.config.option.step
    if step_value is None:
        pytest.skip()
    return step_value
