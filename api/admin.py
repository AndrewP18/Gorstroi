from django.contrib import admin
from .models import Project, Image, Slider_image, Company_contact, Application_form


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name_project", "type_project", "project_area", "number_of_rooms", "number_of_floors", "time_create", "time_update"]
    search_fields = ["name_project", "type_project"]
    readonly_fields = ["time_create", "time_update"]


class ImageAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]
    search_fields = ["name"]
    readonly_fields = ['image_tag']


class Slider_imageAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "link"]
    search_fields = ["name"]
    readonly_fields = ['slider_image']

class Company_contactAdmin(admin.ModelAdmin):
    list_display = ["email", "number_phone", "address"]


class Application_formAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email", "theme"]
    search_fields = ["name", "email"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Slider_image, Slider_imageAdmin)
admin.site.register(Company_contact, Company_contactAdmin)
admin.site.register(Application_form, Application_formAdmin)