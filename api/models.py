from django.conf import settings
from django.db import models
from django.template import loader
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Project(models.Model):
    name_project = models.CharField("Название", max_length=45)
    type_project = models.CharField("Тип", max_length=45)
    project_area = models.CharField("Площадь", max_length=20)
    number_of_rooms = models.PositiveIntegerField("Количество комнат", default=0)
    number_of_floors = models.PositiveIntegerField("Количество этажей", default=0)
    number_of_bedrooms = models.PositiveIntegerField("Количество спален", default=0)
    number_of_bathrooms = models.PositiveIntegerField("Количество санузлов", default=0)
    floor_height = models.CharField("Высота одного этажа", max_length=10, null=True)
    description = models.CharField("Описание", max_length=255)
    time_create = models.DateTimeField("Время создания", auto_now_add=True)
    time_update = models.DateTimeField("Время обновления", auto_now=True)

    def __str__(self):
        return self.name_project

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Image(models.Model):
    name = models.CharField("Наименование",max_length=255)
    link = models.ImageField("Полное название",upload_to='images', null=True)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Проект', related_name='images')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(f'<img src = "{self.link.url}" height = "300" width = "500"/>')
    image_tag.short_description = "Изображение"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Slider_image(models.Model):
    name = models.CharField("Наименование", max_length=255)
    description = models.CharField("Переход на ресурс", max_length=50)
    link = models.ImageField("Полное название", upload_to='images/slider', null=True)

    def __str__(self):
        return self.name

    def slider_image(self):
        return mark_safe(f'<img src = "{self.link.url}" width = "300"/>')
    slider_image.short_description = "Изображение"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения для слайдера"


class Company_contact(models.Model):
    email = models.CharField("Электронная почта", max_length=45)
    number_phone = models.CharField("Номер телефона", max_length=12, help_text='В формате +79998887766')
    address = models.CharField("Адрес", max_length=255)

    def __str__(self):
        return self.number_phone

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты компании"


THEME_CHOICES = [
    ('Дом', 'Заказать строительство жилого дома'),
    ('Инженерное сооружение', 'Заказать строительство инженерного сооружения'),
    ('Отделка', 'Заказать отделку помещения'),
    ('Вопрос', 'Другой вопрос'),
]

class Application_form(models.Model):
    name = models.CharField("Имя", max_length=45)
    surname = models.CharField("Фамилия", max_length=45)
    phone_number = models.CharField("Номер телефона", max_length=12)
    email = models.CharField("Электронная почта", max_length=45)
    theme = models.CharField("Тема", choices=THEME_CHOICES, default='Дом', max_length=100)
    note = models.CharField("Комментарий", max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявку"
        verbose_name_plural = "Заявки"

@receiver(post_save, sender=Application_form)
def send(sender, instance, **kwargs):
    if kwargs['created']:
        html_messsage = loader.render_to_string(
            'emails/email_message.html',
            {
                'sender_name': instance.name,
                'sender_surname': instance.surname,
                'phone_number': instance.phone_number,
                'email': instance.email,
                'theme': instance.theme,
                'note': instance.note,
            }
        )

        send_mail(
            "Заявка",
            None,
            settings.EMAIL_HOST_USER,
            ['shadowandgod@mail.ru'],
            fail_silently=False,
            html_message=html_messsage
        )