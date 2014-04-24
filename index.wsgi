import sae
from app import wsgi

application = sae.create_wsgi_app(wsgi.application)
