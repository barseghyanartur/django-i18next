from __future__ import absolute_import

from django.utils import translation

from nine import versions

if versions.DJANGO_GTE_1_9:
    from django.template import (
        Library,
        Node,
        TemplateSyntaxError
    )
else:
    from django.template.base import (
        Library,
        Node,
        TemplateSyntaxError
    )

__title__ = 'i18next.templatetags.i18next'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2015-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'OverrideLocaleNode',
    'overridelocale',
    'DisableTranslationsNode',
    'disabletranslations',
)

register = Library()


class OverrideLocaleNode(Node):
    """Node for ``overridelocale``."""

    def __init__(self, language_code, nodelist):
        """Constructor."""
        self.language_code = language_code
        self.nodelist = nodelist

    def render(self, context):
        """Render."""
        language_code = self.language_code.resolve(context)
        with translation.override(language_code):
            return self.nodelist.render(context)


@register.tag
def overridelocale(parser, token):
    """Override locale for certain code block.

    Example usage::

        {% overridelocale 'en' %}
            <p>
                <a href="/login/">{% trans "Log in" %}</a>
            </p>
        {% endoverridelocale %}
    """
    bits = token.split_contents()

    if not 2 == len(bits):
        raise TemplateSyntaxError("{0} expected at least one variable "
                                  "assignment".format(bits[0]))

    language_code = parser.compile_filter(bits[1])

    nodelist = parser.parse(('endoverridelocale',))
    parser.delete_first_token()
    return OverrideLocaleNode(language_code, nodelist)


class DisableTranslationsNode(Node):
    """Node for ``disabletranslations``."""

    def __init__(self, nodelist):
        """Constructor."""
        self.nodelist = nodelist

    def render(self, context):
        """Render."""
        current_language = translation.get_language()

        translation.deactivate_all()

        rendered = self.nodelist.render(context)

        translation.activate(current_language)

        return rendered


@register.tag
def disabletranslations(parser, token):
    """Disable translations for the block.

    Example usage::

        {% disabletranslations %}
            <p>
                <a href="/login/">{% trans "Log in" %}</a>
            </p>
        {% enddisabletranslations %}
    """
    bits = token.split_contents()

    if not 1 == len(bits):
        raise TemplateSyntaxError("{0} does not take any arguments"
                                  "".format(bits[0]))

    nodelist = parser.parse(('enddisabletranslations',))
    parser.delete_first_token()
    return DisableTranslationsNode(nodelist)
