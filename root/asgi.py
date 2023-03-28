"""
ASGI config for root project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

print(websocket_urlpatterns)
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # "websocket": URLRouter(websocket_urlpatterns),
    # "websocket": AllowedHostsOriginValidator(
    #         # AuthMiddlewareStack(URLRouter(root.routing.websocket_urlpatterns))
    #         AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    #         # re_path(r"", get_asgi_application()),
    #     ),
    # "websocket":
    #         # AuthMiddlewareStack(URLRouter(root.routing.websocket_urlpatterns))
    #         (URLRouter(websocket_urlpatterns)
    #         # re_path(r"", get_asgi_application()),
    #     ),
})

# application = get_asgi_application()
