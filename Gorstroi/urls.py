from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from api.views import Projects_list, ProjectOne, Images_list, Slider_images_list, Company_contacts_list, Application_form_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', Projects_list.as_view()),
    path('api/projects/<int:pk>', ProjectOne.as_view()),
    path('api/images/', Images_list.as_view()),
    path('api/slider/images/', Slider_images_list.as_view()),
    path('api/contacts/', Company_contacts_list.as_view()),
    path('api/applications/create', Application_form_create.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)