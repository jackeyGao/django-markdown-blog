# -*- coding:utf-8 -*-
# Django settings for mysite project.
import os
PROJ_DIR=''

site_info = {
    'name' : 'JackeyGao',
    'sign' : 'All things are difficult before they are easy.',
}

QINIU_ACCESS_KEY = '-9GvtvlzlYsJThtrNMVocrhcsh3lmOTAuY6aXEBT'
QINIU_SECRET_KEY = 'l7fqBwgd-3M5ApcquLCFb-KKmLmNcIrlpQGJbBem'
QINIU_BUCKET_DOMAIN = 'jackeygaoblog.qiniudn.com'
QINIU_BUCKET_NAME = 'jackeygaoblog'

ENGINE='django.db.backends.mysql' # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
MYSQL_DB='app'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_USER = 'django'
MYSQL_PASS = 'django123'
#    MYSQL_DB   = 'app'
DEBUG = False
TEMPLATE_DEBUG = False
     

alipay_transfer = "/page/alipayQRcode/"

url_list = ['[creativecommons]:http://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh', 
            '[alipay]:%s' % alipay_transfer,]

blog_template = u"""<hr align="left">\n\n如果[本文](%s)对你有帮助，欢迎对Jackey进行无负担小额赞助 [支付宝][alipay]
\n版权声明：**自由转载-非商用-非衍生-保持署名** | [Creative Commons BY-NC-ND 3.0][creativecommons]"""

ADMINS = (
    ('JackeyGao', 'gaojunqi@outlook.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': ENGINE, # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MYSQL_DB,                      # Or path to database file if using sqlite3.
        'USER': MYSQL_USER,                      # Not used with sqlite3.
        'PASSWORD': MYSQL_PASS,                  # Not used with sqlite3.
        'HOST': MYSQL_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': MYSQL_PORT,                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(PROJ_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/tmp/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(PROJ_DIR,'static')
STATIC_ROOT = '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJ_DIR,'static'),
    # os.path.join(PROJ_DIR,'media'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-inb32@&amp;3^!%8tdee!0bw0edibc+#l%cl$aca359smsklsuq&amp;v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
#GRAPPELLI_INDEX_DASHBOARD = 'blog.dashboard.CustomIndexDashboard'
#GRAPPELLI_INDEX_DASHBOARD = {  # alternative method
#    'blog.admin.admin_site': 'blog.my_dashboard.CustomIndexDashboard',
#}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', #simple page
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJ_DIR,'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

WMD_ADMIN_SHOW_PREVIEW=False

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # 'django.contrib.flatpages', #simple page
    # Uncomment the next line to enable the admin:
    #'filebrowser',
    #'grappelli.dashboard',
    'xadmin',
    'crispy_forms',
    'reversion',
    #'django.contrib.admin',
    'markup_deprecated',
    'blog',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
#STATICFILES_STORAGE  = 'qiniustorage.backends.QiniuStaticStorage'



