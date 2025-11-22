from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-m1jzio8*==xjjax3ooy(4d+%xhh#yi0d(u)bgi6bi5e5=wks-f"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Django REST framework
    "rest_framework",
    "rest_framework.authtoken",

    # Autenticación dj-rest-auth + allauth
    "dj_rest_auth",
    "dj_rest_auth.registration",

    "django.contrib.sites",
    "allauth",
    "allauth.account",

    # socialaccount requerido pero no usarás proveedores sociales
    "allauth.socialaccount",

    # Tu app
    "apps.authentication",
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Login solo con email
ACCOUNT_LOGIN_METHODS = {"email"}

ACCOUNT_SIGNUP_FIELDS = {
    "email*": {},
    "username*": {},
    "first_name*": {},
    "last_name*": {},
    "password1*": {},
    "password2*": {},
}

# No pedir verificación de correo
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "apps.authentication.serializers.CustomRegisterSerializer",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",

    # Requerido por django-allauth
    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",  # requerido por allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Contraseñas libres durante desarrollo
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
