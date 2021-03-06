"""PatientManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

from patientmgt.forms import LoginForm

urlpatterns = [
    url(r"^patient/", include("patientmgt.urls")),
    url(r"^$",
        TemplateView.as_view(template_name="patientmgt/display.html"),
        name="display"
    ),
    url(r"^login/$", auth_views.login, {
        "template_name": "patientmgt/login.html",
        "authentication_form": LoginForm,
    }, name="login"),

    url(r"^logout/$", auth_views.logout, {
        "next_page": "login",
    }, name="logout"),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)