import os
import unittest
from pathlib import Path
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import ImageForm, LogentryForm, CountryForm
from .models import Image, Logentry, Country


class TestCountryForm(TestCase):
    """
    Unittest for testing the add country form
    """

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
    """
    Testing the Logentry form
    """

    def test_logentry_form_title_label(self):
        form = LogentryForm()
        self.assertTrue(
            form.fields['title'].label == 'Title')
