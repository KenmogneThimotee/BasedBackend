from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from .views import *


routes = SimpleRouter()

routes.register('post', PostViewset)
routes.register('postComment', PostCommentViewset)
routes.register('upvote', UpVoteViewset)
routes.register('downvote', DownVoteViewset)
routes.register('lileComment', LikeCommentViewset)
routes.register('dislikeComment', DislikeCommentViewset)
routes.register('imagesPost', ImageViewset)

urlpatterns = routes.get_urls()