from django.core.management import call_command

from .base import (
    is_i18next_setup_completed,
    mark_i18next_setup_as_completed
)

__title__ = 'i18next.tests.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('setup_i18next',)


def setup_i18next(collectstatic=False):
    """Set up i18next."""
    if is_i18next_setup_completed():
        return False

    if collectstatic:
        call_command('collectstatic', verbosity=3, interactive=False)

    mark_i18next_setup_as_completed()
