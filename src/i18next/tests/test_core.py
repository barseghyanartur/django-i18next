# -*- coding: utf-8 -*-

import unittest

from bs4 import BeautifulSoup
from django.test import TestCase, Client
from six import text_type

from .base import log_info
from .helpers import setup_i18next

__title__ = 'i18next.tests.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('I18NextCoreTest',)


class I18NextCoreTest(TestCase):
    """Testing `django-i18next` core functionality."""

    def setUp(self):
        """Set up."""
        setup_i18next()
        client = Client()

        self.response = client.get('/nl/')
        self.soup = BeautifulSoup(self.response.content)

        self.link_overridelocale_en_text = text_type('Log in')
        self.link_overridelocale_ru_text = text_type(u'Войти')
        self.link_normal_text = text_type('Inloggen')
        self.link_disabletranslations_text = text_type('Log in')

    @log_info
    def test_01_overridelocale_en_while_when_set_to_nl(self):
        """Test ``overridelocale`` `en` when visiting Dutch (nl) site."""
        link_overridelocale_en = self.soup.find(
            'a',
            attrs={'class': 'overridelocale-en'}
        )
        self.assertEqual(link_overridelocale_en.text,
                         self.link_overridelocale_en_text)
        return link_overridelocale_en.text

    @log_info
    def test_02_normal_while_when_set_to_nl(self):
        """Test normal when visiting Dutch site (locale==nl)."""
        link_normal = self.soup.find('a', attrs={'class': 'normal'})
        self.assertEqual(link_normal.text, self.link_normal_text)
        return link_normal.text

    @log_info
    def test_03_disabletranslations_while_when_set_to_nl(self):
        """Test ``disabletranslations`` when visiting Dutch (nl) site."""
        link_disabletranslations = self.soup.find(
            'a',
            attrs={'class': 'disabletranslations'}
        )
        self.assertEqual(link_disabletranslations.text,
                         self.link_disabletranslations_text)
        return link_disabletranslations.text

    @log_info
    def test_04_overridelocale_ru_while_when_set_to_nl(self):
        """Test ``overridelocale`` `ru` when visiting Dutch (nl) site."""
        link_overridelocale_ru = self.soup.find(
            'a',
            attrs={'class': 'overridelocale-ru'}
        )
        self.assertEqual(link_overridelocale_ru.text,
                         self.link_overridelocale_ru_text)
        return link_overridelocale_ru.text


if __name__ == '__main__':
    unittest.main()
