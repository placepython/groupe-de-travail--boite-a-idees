from .base import *
from .base import env

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='django-insecure-5=5o807&9c1ssy0aenzp&-coo$#+s#0f+-bspv_llseims8%q@',
)

DEBUG = True

# Configuration of the email
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

# Configuration of Django Extensions
INSTALLED_APPS += ["django_extensions"]

# Configuration of Django Debug Toolbar
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1"]
