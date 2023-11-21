from .base import *  # noqa
from .base import env


# ADDED FOR PRODUCTION
# ------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True


# # INTERNALLY-DEFINED, NOT DJANGO-SPECIFIC

# DB_USERNAME = env('DB_USERNAME')
# DB_PASSWORD = env('DB_PASSWORD')
# DB_NAME = env('DB_NAME')
# DB_HOST = env('DB_HOST')
# DB_PORT = env('DB_PORT')
# SECRET_KEY = get_random_secret_key()
# PRODUCTION_SERVER = env('PRODUCTION_SERVER')
# PRODUCTION_DOMAIN = env('PRODUCTION_DOMAIN')
# DEBUG = env('DEBUG') == 'True'


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

# The first 3 items are provided by default for localhost, the 4th one is for the app being visible by users

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]', PRODUCTION_SERVER]

CSRF_TRUSTED_ORIGINS = [
    'https://' + PRODUCTION_DOMAIN,
    'http://127.0.0.1',
    'https://' + PRODUCTION_SERVER,
]

# DATABASES
# ------------------------------------------------------------------------------
# DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa: F405

# DATABASES = {
#     'default': {  # A 'default' database alias has to be specified
#         'NAME': DB_NAME,
#         'ENGINE': 'django.db.backends.postgresql',
#         'USER': DB_USERNAME,
#         'PASSWORD': DB_PASSWORD,
#         'HOST': DB_HOST,
#         'PORT': DB_PORT,
#     },
# }

# CACHES
# ------------------------------------------------------------------------------
#CACHES = {
#    "default": {
#        "BACKEND": "django_redis.cache.RedisCache",
#        "LOCATION": env("REDIS_URL"),
#        "OPTIONS": {
#            "CLIENT_CLASS": "django_redis.client.DefaultClient",
#            # Mimicing memcache behavior.
#            # https://github.com/jazzband/django-redis#memcached-exceptions-behavior
#            "IGNORE_EXCEPTIONS": True,
#        },
#    }
#}

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)

# STORAGES
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/#installation
# INSTALLED_APPS += ["storages"]  # noqa: F405
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_QUERYSTRING_AUTH = False
# # DO NOT change these unless you know what you're doing.
# _AWS_EXPIRY = 60 * 60 * 24 * 7
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate",
# }
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_MAX_MEMORY_SIZE = env.int(
#     "DJANGO_AWS_S3_MAX_MEMORY_SIZE",
#     default=100_000_000,  # 100MB
# )
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
# AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
# aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

# STATIC
# ------------------------
# STATICFILES_STORAGE = "cqt_customer_query_tool.utils.storages.StaticRootS3Boto3Storage"
# COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
# STATIC_URL = f"https://{aws_s3_domain}/static/" # static variables added under to match base.py

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATIC_ROOT = str(BASE_DIR / "static")

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]

# MEDIA
# ------------------------------------------------------------------------------
# DEFAULT_FILE_STORAGE = "cqt_customer_query_tool.utils.storages.MediaRootS3Boto3Storage"
# MEDIA_URL = f"https://{aws_s3_domain}/media/"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="cqt_customer_query_tool <noreply@example.com>",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[cqt_customer_query_tool]",
)

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env("DJANGO_ADMIN_URL")

# Anymail
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa: F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# https://anymail.readthedocs.io/en/stable/esps
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
ANYMAIL = {}

# Collectfast
# ------------------------------------------------------------------------------
# https://github.com/antonagestam/collectfast#installation
INSTALLED_APPS = ["collectfast"] + INSTALLED_APPS  # noqa: F405

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}


# Your stuff...
# ------------------------------------------------------------------------------
