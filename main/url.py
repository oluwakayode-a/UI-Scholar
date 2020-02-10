"""mauvelli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import handler404, handler500
from blog import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet', include('jet.urls')),
    path('', include(('blog.urls', 'blog'))),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name="ckeditor_upload"),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
    path('dashboard/', include(('dashboard.urls', 'dashboard'))),
    path('subscribe/', include(('subscribe.urls', 'subscribe'))),

    # password reset
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# custom 404 and 500 handlers
handler404 = views.error_404
handler500 = views.error_500

admin.site.site_header = 'Mauvelli'
admin.site.site_title = 'Mauvelli Site Admin'
admin.site.index_title = "Mauvelli Administration"
