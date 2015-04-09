__title__ = 'i18next.testing.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('setup_i18next',)

from django.core.management import call_command

from i18next.testing.base import (
    is_i18next_setup_completed, mark_i18next_setup_as_completed
)

def setup_i18next(collectstatic=False):
    """
    Set up i18next.
    """
    if is_i18next_setup_completed():
        return False

    if collectstatic:
        call_command('collectstatic', verbosity=3, interactive=False)

    mark_i18next_setup_as_completed()
