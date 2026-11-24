cat > django_template/'{{ project_name }}'/settings/production.py <<'EOF'
import os

from .base import *


# Production settings

DEBUG = False


# Security

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"

X_FRAME_OPTIONS = "DENY"


# HTTPS settings

SECURE_SSL_REDIRECT = True

# Enable HSTS only after HTTPS is confirmed to work correctly.

SECURE_HSTS_SECONDS = int(
    os.environ.get("DJANGO_SECURE_HSTS_SECONDS", "0")
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = (
    os.environ.get("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", "False").lower()
    in ("true", "1", "yes")
)

SECURE_HSTS_PRELOAD = (
    os.environ.get("DJANGO_SECURE_HSTS_PRELOAD", "False").lower()
    in ("true", "1", "yes")
)


# Static files

STATIC_ROOT = BASE_DIR / "staticfiles"


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.environ.get("DJANGO_LOG_LEVEL", "INFO"),
    },
}
EOF
