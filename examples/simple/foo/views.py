import uuid
import logging

from django.http import HttpResponse
from django.utils import translation

logger = logging.getLogger('i18next')

def foo_view(request):
    """
    Foo view.

    :param django.http.HttpRequest request:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    return HttpResponse(
        "request.LANGUAGE_CODE: {0}, translation.get_language: "
        "{1}".format(request.LANGUAGE_CODE, translation.get_language())
        )
