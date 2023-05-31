from django.db import models

class Project(models.Model):
    name_project = models.CharField(max_length=45)
    type_project = models.CharField(max_length=45)
    project_area = models.CharField(max_length=20)
    number_of_rooms = models.IntegerField()
    number_of_floors = models.IntegerField()
    description = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_project


class Image(models.Model):
    name = models.CharField(max_length=255)
    link = models.ImageField(upload_to='images', null=True)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='images')

    def __str__(self):
        return self.name


class Company_contact(models.Model):
    email = models.CharField(max_length=45)
    number_phone = models.CharField(max_length=12)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Feedback_form(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=45)
    subject_of_question = models.CharField(max_length=100)
    quesion_body = models.CharField(max_length=500)

    def __str__(self):
        return self.name
