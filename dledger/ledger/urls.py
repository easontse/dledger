from django.conf.urls import url
from ledger import views

urlpatterns = [
    url(r'^$', views.index, name='ledger_index'),
]
