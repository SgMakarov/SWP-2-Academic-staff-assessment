
from django.urls import include, path
from django.contrib import admin
<<<<<<< HEAD
from django.conf import settings

urlpatterns = [
=======
from django.contrib.auth import views as auth_views
from survey.views import IndexView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('survey/', include('survey.urls')),
    path('students/', include('students.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', IndexView.as_view()),
>>>>>>> b7c41758791903fbcd6ef999a40e4c837d1bddc7
    path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name='index.html'), name='home'),
]

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('survey/', include('survey.urls'))
    ]