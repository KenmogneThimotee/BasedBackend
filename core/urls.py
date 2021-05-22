from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import *


routes = SimpleRouter()

routes.register('styledImage', StyleImageViewset)
routes.register('styledImage', StyledImageViewset)
routes.register('originalImage', OriginalImageViewset)
routes.register('styledCollection', StyledImageCollectionViewset)
routes.register('styleCollection', StyleImageCollectionViewset)


urlpatterns = routes.get_urls()