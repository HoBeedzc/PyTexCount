import sys
from .Tex import Tex
from .TexCount import TexCount


class PyTexCountNotSupportError(Exception):
    pass


if sys.version_info[0] < 3:
    raise PyTexCountNotSupportError(
        "Sorry, PyTexCount does not support Python2.\
        Please update your Python to 3.x version.")

__version__ = '1.0.0'
__license__ = 'MIT'
__author__ = 'Hobee'
__github__ = r'https://github.com/HoBeedzc/PyTexCount'
__slogan__ = r'Never Settle!'
__hello_world__ = '''PyTexCount {}
Author: {}
license: {}
Find more info at: {}
{}
'''.format(__version__, __author__, __license__, __github__, __slogan__)
print(__hello_world__)
