import os
from pathlib import Path
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import ImageForm, LogentryForm, CountryForm

BASE_DIR = Path(__file__).resolve().parent.parent


class TestCountryForm(TestCase):

    # def test_country_form_ctry_title_label(self):
    #     form = CountryForm()
    #     self.assertTrue(
    #         form.fields['ctry_title'].label is None)

    # def test_country_form_ctry_title_field_placeholder(self):
    #     form = CountryForm()
    #     self.assertTrue(
    #         form.fields['ctry_title'].help_text == 'Enter country name')

    def test_ctry_title_is_required(self):
        form = CountryForm({'ctry_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ctry_title', form.errors.keys())
        self.assertEqual(form.errors['ctry_title']
                         [0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CountryForm()
        self.assertEqual(form.Meta.fields, ('ctry_title',))


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
