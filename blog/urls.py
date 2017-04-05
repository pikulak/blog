from django.conf.urls import include,url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$',views.index),
    url(r'^projekt/([0-9])/$', views.view_projekt),
    url(r'^pikulski/$',views.o_mnie),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)