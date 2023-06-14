from django.conf import settings
from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
from .models import Project, Image, Slider_image, Company_contact, Application_form


class ModelsTestCase(APITestCase):
    def test_project_model(self):
        self.project = Project.objects.create(
            name_project='TestHouse',
            type_project='This is a test project',
            project_area='100 m',
            floor_height='2m',
            description='Good house for good family',
        )
        self.assertEqual(self.project.name_project, 'TestHouse')
        self.assertEqual(self.project.type_project, 'This is a test project')
        self.assertEqual(self.project.project_area, '100 m')
        self.assertEqual(self.project.floor_height, '2m')
        self.assertEqual(self.project.description, 'Good house for good family')

    def test_image_model(self):
        self.image = Image.objects.create(
            name='TestImage',
            link='TestLinkImage',
        )
        self.assertEqual(self.image.name, 'TestImage')
        self.assertEqual(self.image.link, 'TestLinkImage')

    def test_slider_image_model(self):
        self.slider_image = Slider_image.objects.create(
            name='TestSliderImage',
            link='TestLinkSliderImage',
            description='/testresourse',
        )
        self.assertEqual(self.slider_image.name, 'TestSliderImage')
        self.assertEqual(self.slider_image.link, 'TestLinkSliderImage')
        self.assertEqual(self.slider_image.description, '/testresourse')

    def test_company_contact_model(self):
        self.company_contact = Company_contact.objects.create(
            email='testemail@com',
            number_phone='+79998887766',
            address='City Test, Street Test, House 5',
        )
        self.assertEqual(self.company_contact.email, 'testemail@com')
        self.assertEqual(self.company_contact.number_phone, '+79998887766')
        self.assertEqual(self.company_contact.address, 'City Test, Street Test, House 5')

    def test_application_form_model(self):
        self.application_form = Application_form.objects.create(
            name='Test Name',
            surname='Test Surname',
            phone_number='+79998887766',
            email='testemail@com',
            theme='Test Theme',
            note='Test small comment'
        )
        self.assertEqual(self.application_form.name, 'Test Name')
        self.assertEqual(self.application_form.surname, 'Test Surname')
        self.assertEqual(self.application_form.phone_number, '+79998887766')
        self.assertEqual(self.application_form.email, 'testemail@com')
        self.assertEqual(self.application_form.theme, 'Test Theme')
        self.assertEqual(self.application_form.note, 'Test small comment')


class SendEmailTestCase(APITestCase):
    def test_send_email(self):
        mail.send_mail(
            'This is Theme',
            'Here is the note',
            settings.EMAIL_HOST_USER,
            ['shadowandgod@mail.ru'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'This is Theme')
        self.assertEqual(mail.outbox[0].body, 'Here is the note')
        self.assertEqual(mail.outbox[0].from_email, settings.EMAIL_HOST_USER)
        self.assertEqual(mail.outbox[0].to, ['shadowandgod@mail.ru'])


class ViewsTestCase(APITestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            name_project='test',
            description='description'
        )
        self.url = f'/api/projects/{self.project.pk}/'
        Image.objects.create(
            name='test',
        )
        Company_contact.objects.create(
            email='test@mail.ru',
            number_phone='test',
            address='test'
        )

    def test_get_projects_list(self):
        response = self.client.get('/api/projects/')
        project = Project.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(project))

    def test_get_project_one(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name_project'), 'test')

    def test_get_images_list(self):
        response = self.client.get('/api/images/')
        image = Image.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(image))

    def test_get_contacts_list(self):
        response = self.client.get('/api/contacts/')
        contacts = Company_contact.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(contacts))

    def test_create_application(self):
        url = '/api/applications/create/'
        data = {
            "name": "test",
            "surname": "test",
            "phone_number": "1234567890",
            "email": "test@mail.ru",
            "theme": "Дом",
            "note": "test"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        applications = Application_form.objects.all()
        self.assertEqual(len(applications), 1)

        application = applications[0]
        self.assertEqual(application.name, 'test')
        self.assertEqual(application.surname, 'test')
        self.assertEqual(application.phone_number, '1234567890')
        self.assertEqual(application.email, 'test@mail.ru')
        self.assertEqual(application.theme, 'Дом')
        self.assertEqual(application.note, 'test')