from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ktac', views.ktac, name='ktac'),
    url(r'^ktqry', views.ktqry, name='ktqry'),
    url(r'^ktproc', views.ktproc, name='ktproc'),

]