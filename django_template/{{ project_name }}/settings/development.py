cat > django_template/'{{ project_name }}'/settings/development.py <<'EOF'
from .base import *


# Development settings

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]
EOF
