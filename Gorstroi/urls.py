from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from api.views import ProjectAPIView, ProjectOneAPIView, ImageAPIView, Company_contactAPIView, Application_formSerializerAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', ProjectAPIView.as_view()),
    path('api/projects/<int:pk>', ProjectOneAPIView.as_view()),
    path('api/images/', ImageAPIView.as_view()),
    path('api/contacts/', Company_contactAPIView.as_view()),
    path('api/applications/', Application_formSerializerAPIView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)