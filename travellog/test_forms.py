import os
from pathlib import Path
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import ImageForm, LogentryForm, CountryForm
from .models import Image, Logentry, Country

# BASE_DIR = Path(__file__).resolve().parent.parent


class TestCountryForm(TestCase):

    def test_country_form_ctry_title_label(self):
        form = CountryForm()
        self.assertTrue(
            form.fields['ctry_title'].label == 'Country')

    def test_ctry_title_is_required(self):
        form = CountryForm({'ctry_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ctry_title', form.errors.keys())
        self.assertEqual(form.errors['ctry_title']
                         [0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CountryForm()
        self.assertEqual(form.Meta.fields, ('ctry_title',))


class TestLogentryForm(TestCase):

    #     def test_logentry_form_is_valid(self):
    #         user = User.objects.create_user(
    #             username='testuser',
    #             email='test@email.com',
    #             password='pwrd',
    #         )
    #         country = Country.objects.create(
    #             ctry_title='testcountry',
    #         )

    #         request = HttpRequest()
    #         request.POST = {
    #             'title': 'Test Title',
    #             'author': user.pk,
    #             'year': '2000',
    #             'description': 'Details about test',
    #             'status': 1,
    #             'privacy': 1,
    #             'country': country.pk,
    #         }

    #         form = LogentryForm(request.POST)
    #         self.assertTrue(form.is_valid())

    def test_logentry_form_title_label(self):
        form = LogentryForm()
        self.assertTrue(
            form.fields['title'].label == 'Title')


# class TestImageForm(TestCase):

#     def test_image_form_valid(self):
#         self.image_file = open(
#             os.path.join(BASE_DIR, 'static/media/images/erd.jpeg'), "rb"
#         )
#         data = {'caption': 'Test', 'alttest': 'Test', }
#         files_data = {
#             'gallery_image': SimpleUploadedFile(
#                 self.image_file.name,
#                 self.image_file.read()
#             )
#         }
#         form = ImageForm(files=files_data, data=data)
#         self.assertTrue(form.is_valid())
