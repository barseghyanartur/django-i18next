from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

__all__ = ('urlpatterns',)


urlpatterns = [
    url(_(r'^foo/$'), view=views.foo_view, name='foo.foo_view'),
]
