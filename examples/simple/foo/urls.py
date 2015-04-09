__all__ = ('urlpatterns',)

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from foo import views

urlpatterns = [
    url(_(r'^foo/$'), view=views.foo_view, name='foo.foo_view'),
]
