from django.conf.urls.defaults import *
from django.views.generic.simple import *

#import django_rpx.views

urlpatterns = patterns('',
    # Account/Auth URLs not implemented by django_rpx_plus:
    url(r'^rpx_response/$', 'myproject.django_rpx_plus.views.rpx_response', name='rpx_response'),
    url(r'^login/$', 'myproject.django_rpx_plus.views.login', name='auth_login'),
    url(r'^register/$', 'myproject.django_rpx_plus.views.register', name='auth_register'),
    url(r'^associate/$', 'myproject.django_rpx_plus.views.associate', name='auth_associate'),
    url(r'^associate/delete/(\d+)/$', 'myproject.django_rpx_plus.views.delete_associated_login', name='auth_delete_associated'),
    url(r'^associate/rpx_response/$', 'myproject.django_rpx_plus.views.associate_rpx_response', name='associate_rpx_response'),
    url(r'^$', 'django.views.generic.simple.redirect_to', 
                        {'url': '/accounts/profile/', 'permanent': False},
                        name='auth_home'),

)
