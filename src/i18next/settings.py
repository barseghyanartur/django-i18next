"""
- `DEBUG`
"""
from .conf import get_setting

__title__ = 'i18next.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DEBUG',)


DEBUG = get_setting('DEBUG')
