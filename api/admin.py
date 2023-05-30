from django.contrib import admin
from .models import Project
from .models import Image
from .models import Company_contact
from .models import Feedback_form

admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Company_contact)
admin.site.register(Feedback_form)