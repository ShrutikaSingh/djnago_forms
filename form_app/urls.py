from django.conf.urls import url
from . import views


urlpatterns = [
    url('snippet',views.snippet_detail),
    url('',views.contact)

]
