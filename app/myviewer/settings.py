"""
Django settings for myviewer project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-xz^$5s^82o8wab8bo1opw0c-irbtyr4$j!u+_=gbfp10tpdy8@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "snippets.apps.SnippetsConfig",  # アプリの追加
    "accounts.apps.AccountsConfig",
    "viewer.apps.ViewerConfig",
    "django_bootstrap5",
    "pygments_renderer",
    "django_extensions",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "sample_batch",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

ROOT_URLCONF = "myviewer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # テンプレートが格納されたフォルダを複数個リストで指定する
        "APP_DIRS": True,  # Trueなら 各アプリケーション以下の templates ディレクトリを検索対象に含める
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myviewer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DJANGO_DB_NAME"),
        "USER": os.environ.get("DJANGO_DB_USERNAME"),
        "PASSWORD": os.environ.get("DJANGO_DB_PASSWORD"),
        "HOST": os.environ.get("DJANGO_DB_HOSTNAME"),
        "PORT": os.environ.get("DJANGO_DB_PORT"),
    }
}

# 認証ユーザー追加
AUTH_USER_MODEL = "accounts.MSYSUser"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# リクエストパスが以下で指定したパスから始まる場合、staticファイルを探して返す
STATIC_URL = "/static/"

# collectstaticなどを行った際にファイルを設置するstaticフォルダの場所を記述（開発の際は必要ないのでコメントアウトしておく）
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# htmlファイルなどから読み込むstaticフォルダの場所を記述
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

# MEDIA_URL
MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_ROOT = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# sitesフレームワーク用サイトID
SITE_ID = 1


# login settings
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# allauth settings
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "optional"  # ユーザ登録時に確認メールを送信するか(none=送信しない, mandatory=送信する)
ACCOUNT_EMAIL_REQUIRED = True  # ユーザ登録にメルアド必須にする
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3  # 招待メールの期限
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # email出力をコンソールに出す
ACCOUNT_FORMS = {"signup": "accounts.admin.UserCreationForm"}  # カスタムフォームを使用

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # デバッグ用 メールをコンソール表示
# # メール送信の設定 Gmailを使う場合。
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') #送信元メールアドレス
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') # gmailならアプリパスワード
# EMAIL_USE_TLS = True

# Loging settings
LOGGING = {
    "version": 1,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    "formatters": {"local": {"format": "%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s"}},
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        }
    },
    # 自分が出すログ出力
    "root": {
        "handlers": ["console"],
        #        "level": "DEBUG",
        "level": "INFO",
        "propagate": False,
        "formatter": "local",
    },
    "loggers": {
        # Djangoのエラー・警告・開発WEBサーバのアクセスログ
        "django": {"handlers": ["console"], "level": "INFO", "propagate": False, "formatter": "local"},
        # 実行SQL
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}