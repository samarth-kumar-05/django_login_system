"""
URL configuration for login_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views import home,patient_signup, doctor_signup, patient_login, doctor_login, patient_dashboard, doctor_dashboard,logout_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name='home'),
    path('patient/signup/', patient_signup, name='patient_signup'),
    path('doctor/signup/', doctor_signup, name='doctor_signup'),
    path('patient/login/', patient_login, name='patient_login'),
    path('doctor/login/', doctor_login, name='doctor_login'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('logout/', logout_view, name='logout'),
]
# from app.views import home, patient_signup, doctor_signup, patient_dashboard, doctor_dashboard, login_view, logout_view

# urlpatterns = [
#     path('', home, name='home'),
#     path('patient/signup/', patient_signup, name='patient_signup'),
#     path('doctor/signup/', doctor_signup, name='doctor_signup'),
#     path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
#     path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
# ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
