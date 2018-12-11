from django.conf.urls import url

from kaola import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
]