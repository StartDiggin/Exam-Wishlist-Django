from django.conf.urls import url
from . import views

from django.http import HttpResponse
def test(request):
    # return HttpResponse("It works project level")
    return HttpResponse("It works app level")

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^addProduct$', views.addProduct),
    url(r'^create$', views.create),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^item/(?P<id>\d+)$', views.item),
    url(r'^logout$', views.logout),
]
