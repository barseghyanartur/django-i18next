from __future__ import print_function

__title__ = 'i18next.testing.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'PRINT_INFO', 'TRACK_TIME', 'print_info', 'i18next_setup', 'skip',
    'is_i18next_setup_completed', 'mark_i18next_setup_as_completed',
)

PRINT_INFO = True
TRACK_TIME = False

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop() # Stop timer

        print('\n{0}'.format(func.__name__))
        print('============================')
        if func.__doc__:
            print('""" {0} """'.format(func.__doc__.strip()))
        print('----------------------------')
        if result is not None:
            print(result)
        if TRACK_TIME:
            print('done in {0} seconds'.format(timer.duration))
        print('\n')

        return result
    return inner

SKIP = False

def skip(func):
    """
    Simply skips the test.
    """
    def inner(self, *args, **kwargs):
        if SKIP:
            return
        return func(self, *args, **kwargs)
    return inner

class I18NextSetup(object):
    """
    Basic setup class in order to avoid the i18next test data
    to be initialised multiple times.
    """
    def __init__(self):
        self.is_done = False

i18next_setup = I18NextSetup()

def is_i18next_setup_completed():
    return i18next_setup.is_done == True

def mark_i18next_setup_as_completed():
    i18next_setup.is_done = True
