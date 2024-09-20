"""
URL configuration for lms project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


API_PREFIX = 'api/v1'

urlpatterns = [

    # UI interface
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),
    path('accounts/', include('accounts.urls')),

    # API interface
    path(f'{API_PREFIX}/lms/', include('accounts.api.urls')),
    path(f'{API_PREFIX}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_PREFIX}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path(f'{API_PREFIX}/lms/', include('students.api.urls')),
    path(f'{API_PREFIX}/lms/', include('teachers.api.urls')),
    path(f'{API_PREFIX}/lms/', include('groups.api.urls')),

]

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
