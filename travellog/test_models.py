from django.test import TestCase
from django.template.defaultfilters import slugify
from .models import Country, Logentry, Image


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Country.objects.create(ctry_title='Test')

    def test_country_ctry_title_label(self):
        country = Country.objects.get(id=1)
        field_label = country._meta.get_field('ctry_title').verbose_name
        self.assertEqual(field_label, 'Country')

    def test_country_ctry_title_max_length(self):
        country = Country.objects.get(id=1)
        max_length = country._meta.get_field('ctry_title').max_length
        self.assertEqual(max_length, 40)

    def test_country__str__(self):
        country = Country.objects.get(id=1)
        expected_object_name = country.ctry_title
        self.assertEqual(str(country), expected_object_name)

    def test_country_slug(self):
        country = Country.objects.get(id=1)
        expected_slug = slugify(country.ctry_title)
        self.assertEqual(country.slug, expected_slug)

    def test_country_approved_defaults_to_false(self):
        country = Country.objects.get(id=1)
        self.assertFalse(country.approved)
