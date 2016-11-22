from __future__ import print_function

import logging

__title__ = 'i18next.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'LOG_INFO',
    'TRACK_TIME',
    'log_info',
    'i18next_setup',
    'skip',
    'is_i18next_setup_completed',
    'mark_i18next_setup_as_completed',
)


LOGGER = logging.getLogger(__name__)

LOG_INFO = True
TRACK_TIME = False

if TRACK_TIME:
    try:
        import simple_timer
    except ImportError as err:
        simple_timer = None
        TRACK_TIME = False


def log_info(func):
    """Log some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        """Inner."""
        if TRACK_TIME:
            timer = simple_timer.Timer()  # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop()  # Stop timer

        LOGGER.info('\n{0}'.format(func.__name__))
        LOGGER.info('============================')
        if func.__doc__:
            LOGGER.info('""" {0} """'.format(func.__doc__.strip()))
        LOGGER.info('----------------------------')
        if result is not None:
            LOGGER.info(result)
        if TRACK_TIME:
            LOGGER.info('done in {0} seconds'.format(timer.duration))
        LOGGER.info('\n')

        return result
    return inner


SKIP = False


def skip(func):
    """Simply skip the test."""
    def inner(self, *args, **kwargs):
        """Inner."""
        if SKIP:
            return
        return func(self, *args, **kwargs)
    return inner


class I18NextSetup(object):
    """Basic setup class.

    Created in order to avoid the i18next test data to be initialised
    multiple times.
    """
    def __init__(self):
        self.is_done = False


i18next_setup = I18NextSetup()


def is_i18next_setup_completed():
    """Check if i18next setup is completed."""
    return i18next_setup.is_done is True


def mark_i18next_setup_as_completed():
    """Mark i18next setup as completed."""
    i18next_setup.is_done = True
