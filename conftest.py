import pytest

from precondition.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    return fixture