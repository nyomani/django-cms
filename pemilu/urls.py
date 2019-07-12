# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from voters.views import PersonSearchResulView
from users import views as user_views
from django.contrib.auth import views as auth_views
from ppln  import views as ppln_views
from cms.wizards.views import WizardCreateView

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),  # NOQA
    path('create/',WizardCreateView.as_view(), name="create-page"),
    path('register/', user_views.register, name='register'),
    path('edit-page/', ppln_views.edit_page, name='edit-page'),
    path('pages/', ppln_views.list_page, name='pages'),
    path('profile/', user_views.profile, name='profile'),
    path('profile-update/', user_views.update_profile, name='profile-update'),
    path('voter-registration/', user_views.voter_registration, name='voter-registration'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password-reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password-reset-done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password-reset-confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password-reset-complete.html'
         ),
         name='password_reset_complete'),
    url('search/',PersonSearchResulView.as_view(),name='search-voter'),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
