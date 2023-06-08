from django.db import models
from django.utils.safestring import mark_safe


class Project(models.Model):
    name_project = models.CharField(max_length=45)
    type_project = models.CharField(max_length=45)
    project_area = models.CharField(max_length=20)
    number_of_rooms = models.PositiveIntegerField(default=0)
    number_of_floors = models.PositiveIntegerField(default=0)
    number_of_bedrooms = models.PositiveIntegerField(default=0)
    number_of_bathrooms = models.PositiveIntegerField(default=0)
    floor_height = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_project

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Image(models.Model):
    name = models.CharField(max_length=255)
    link = models.ImageField(upload_to='images', null=True)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='images')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(f'<img src = "{self.link.url}" width = "300"/>')
    image_tag.short_description = 'Изображение'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Slider_image(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=50)
    link = models.ImageField(upload_to='images/slider', null=True)

    def __str__(self):
        return self.name

    def slider_image(self):
        return mark_safe(f'<img src = "{self.link.url}" width = "300"/>')
    slider_image.short_description = 'Изображение'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения для слайдера'


class Company_contact(models.Model):
    email = models.CharField(max_length=45)
    number_phone = models.CharField(max_length=12)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Feedback_form(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=45)
    subject_of_question = models.CharField(max_length=100)
    quesion_body = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'