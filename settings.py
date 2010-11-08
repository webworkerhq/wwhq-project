# Django settings for myproject project.
import os
import django

# For setting relative paths. See: http://tinyurl.com/adsa3k
# Path of Django framework files (no trailing /):
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
# Path of this "site" (no trailing /):
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BUILT_IN_MESSAGES_FRAMEWORK = False
try:
    import django.contrib.messages.context_processors
    BUILT_IN_MESSAGES_FRAMEWORK = True
except ImportError:
    pass

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fsanchez3_main_site',                      # Or path to database file if using sqlite3.
        'USER': 'fsanchez3_main_site',                      # Not used with sqlite3.
        'PASSWORD': 'M<>wer789',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$7*d+2g+#bmgu+v5!q_)i4plxz)88%#kf294d#z2@t8a64smnq'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = 'myproject.urls'

TEMPLATE_DIRS = (
    '/home/fsanchez3/webapps/website/myproject/django_rpx_plus/templates',
    '/home/fsanchez3/webapps/website/myproject/commercials/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'myproject.tagging',
    'myproject.commercials',
    'myproject.home_page',
    'south',
    'myproject.django_rpx_plus',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.auth', #for user template var
    #'django.core.context_processors.debug',
    #'django.core.context_processors.i18n',
    'django.core.context_processors.media', #for MEDIA_URL template var
    'django.core.context_processors.request', #includes request in RequestContext
)


AUTHENTICATION_BACKENDS = (
    'myproject.django_rpx_plus.backends.RpxBackend', 
    'django.contrib.auth.backends.ModelBackend', #default django auth
)

# Here are some settings related to auth urls. django has default values for them
# as specified on page: http://docs.djangoproject.com/en/dev/ref/settings/. You
# can override them if you like.
#account.
#LOGIN_REDIRECT_URL = '' #default: '/accounts/profile/'
LOGIN_URL = '/login/' #default: '/accounts/login/'
#LOGOUT_URL = '' #default: '/accounts/logout/'

########################################
# django messages framework settings:  #
########################################

#First uses CookieStorage for all messages, falling back to using
#SessionStorage for the messages that could not fit in a single cookie.

if BUILT_IN_MESSAGES_FRAMEWORK:
    MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
else:
    MESSAGE_STORAGE = 'django_messages_framework.storage.fallback.FallbackStorage'

############################
#django_rpx_plus settings: #
############################
RPXNOW_API_KEY = 'hbdamhkplfheiapcobnb'

# The realm is the subdomain of rpxnow.com that you signed up under. It handles 
# your HTTP callback. (eg. http://mysite.rpxnow.com implies that RPXNOW_REALM  is
# 'mysite'.
RPXNOW_REALM = 'tvcmdb'

# (Optional)
#RPX_TRUSTED_PROVIDERS = ''

# (Optional)
# Sets the language of the sign-in interface for *ONLY* the popup and the embedded
# widget. For the valid language options, see the 'Sign-In Interface Localization'
# section of https://rpxnow.com/docs. If not specified, defaults to
# settings.LANGUAGE_CODE (which is usually 'en-us').
# NOTE: This setting will be overridden if request.LANGUAGE_CODE (set by django's
#       LocaleMiddleware) is set. django-rpx-plus does a best attempt at mapping
#       django's LANGUAGE_CODE to RPX's language_preference (using
#       helpers.django_lang_code_to_rpx_lang_preference).
#RPX_LANGUAGE_PREFERENCE = 'en'

# If it is the first time a user logs into your site through RPX, we will send 
# them to a page so that they can register on your site. The purpose is to 
# let the user choose a username (the one that RPX returns isn't always suitable)
# and confirm their email address (RPX doesn't always return the user's email).
REGISTER_URL = '/accounts/register/'
