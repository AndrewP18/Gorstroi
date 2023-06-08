from django.contrib import admin
from .models import Project, Image, Company_contact, Feedback_form


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name_project", "type_project", "project_area", "number_of_rooms", "number_of_floors", "time_create", "time_update"]
    search_fields = ["name_project", "type_project"]
    readonly_fields = ["time_create", "time_update"]


class ImageAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]
    search_fields = ["name"]
    readonly_fields = ['image_tag']


class Company_contactAdmin(admin.ModelAdmin):
    list_display = ["email", "number_phone", "address"]


class Feedback_formAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email"]
    search_fields = ["name", "email"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Company_contact, Company_contactAdmin)
admin.site.register(Feedback_form, Feedback_formAdmin)