"""disquaire_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from store import views
import debug_toolbar
from rest_framework.routers import DefaultRouter

from store.views import *
# router.register('product', ProductViewset, basename='product')
# router.register('article', ArticleViewset, basename='article')

router=DefaultRouter()
router.register('artist', ArtistViewset, basename='artist')
router.register('category', AlbumViewset, basename='category')
urlpatterns = [
    path('store/', include(('store.urls', 'store'), namespace='store')),
    # path('api/artist/', ArtisList.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls)
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
