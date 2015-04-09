__title__ = 'i18next.testing.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('I18NextCoreTest',)

import unittest

from six import text_type
from bs4 import BeautifulSoup

from django.test import TestCase, Client

from i18next.testing.base import print_info
from i18next.testing.helpers import setup_i18next

class I18NextCoreTest(TestCase):
    """
    Tests of django-i18next core functionality.
    """
    def setUp(self):
        setup_i18next()
        c = Client()

        self.response = c.get('/nl/')
        self.soup = BeautifulSoup(self.response.content)

        self.link_overridelocale_en_text = text_type('Log in')
        self.link_normal_text = text_type('Inloggen')
        self.link_disabletranslations_text = text_type('Log in')

    @print_info
    def test_01_overridelocale_en_while_when_set_to_nl(self):
        """
        Test ``overridelocale`` en when visiting Dutch site (locale==nl).
        """
        link_overridelocale_en = self.soup.find(
            'a',
            attrs={'class': 'overridelocale-en'}
            )
        self.assertEqual(link_overridelocale_en.text,
                         self.link_overridelocale_en_text)
        return link_overridelocale_en.text

    @print_info
    def test_02_normal_while_when_set_to_nl(self):
        """
        Test normal when visiting Dutch site (locale==nl).
        """
        link_normal = self.soup.find('a', attrs={'class': 'normal'})
        self.assertEqual(link_normal.text, self.link_normal_text)
        return link_normal.text

    @print_info
    def test_03_disabletranslations_while_when_set_to_nl(self):
        """
        Test ``disabletranslations`` when visiting Dutch site (locale==nl).
        """
        link_disabletranslations = self.soup.find(
            'a',
            attrs={'class': 'disabletranslations'}
            )
        self.assertEqual(link_disabletranslations.text,
                         self.link_disabletranslations_text)
        return link_disabletranslations.text


if __name__ == '__main__':
    unittest.main()
