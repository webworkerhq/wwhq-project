from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^login/$', 'myproject.django_rpx_plus.views.login', name='auth_login'),
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^commercials/$', include('myproject.commercials.urls')),
    # (r'^example/', include('example.foo.urls')),
   
    url(r'^accounts/profile/$', 'myproject.home_page.views.profile', name='auth_profile'),
    #We will use django's built in logout view.
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', 
                      {'template_name': 'django_rpx_plus/logged_out.html'}, 
                      name='auth_logout'),

    (r'^accounts/$', include('myproject.django_rpx_plus.urls')),
    url(r'^$', 'django.views.generic.simple.redirect_to', 
               {'url': '/accounts/profile/', 'permanent': False},
               name='home'),
)
