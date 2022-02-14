from test import __version__
# Import classes from your brand new package
from test import Mammals

# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()


def test_version():
    assert __version__ == '0.1.0'
