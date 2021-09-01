from retro_api.forms import SignupForm
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from .views import  CustomAuthentication,CustomSignup
from django.urls import path
from rest_framework import routers
from retro_api import views as myapp_views


urlpatterns = [
 path(r'', views.home,name='home'),
    path('signup/', CustomSignup.as_view(), name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',views.activate,name='activate'),
    path('accounts/', include('allauth.urls')),
    path('v1/login/', CustomAuthentication.as_view()),


    url(r'v1/invite-team-member/', views.TeamMemberInviteView.as_view(), name='invitation'),
    url(r'v1/accept-invitation/$', views.AcceptInvitationApiView.as_view(), name='accept-invitation'),


    url(r'^password_reset/$', auth_views.PasswordResetView, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
       auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView, name='password_reset_complete'),

]
