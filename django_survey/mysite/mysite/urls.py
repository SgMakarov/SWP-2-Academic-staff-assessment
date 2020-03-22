
from django.urls import include, path
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('survey/', include('survey.urls'))
    ]