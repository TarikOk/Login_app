from django.contrib import admin
from django.urls import path
from django.urls import include
#from rest_framework_swagger.views import get_swagger_view


#schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authorize.urls')),
    path('api/v1/', include("chat_room.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
 #   path('api/swagger', schema_view),

]
