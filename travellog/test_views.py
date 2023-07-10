from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Logentry, Country

class TestViews(TestCase):
    """
    Unitests for travellog app views
    """

    def test_home_page(self):
        """Test home page renders correct page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def setUp(self):
        """Create test login user"""

        email = "test@gmail.com"
        usrnm = "test"
        pswd = "T987654321!"
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, username=usrnm, password=pswd
        )
        logged_in = self.client.login(username=usrnm, password=pswd)
        self.assertTrue(logged_in)

    def test_add_logentry(self):
        """Test if add_logentry page renters correctly """
        response = self.client.get('/add_logentry/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_logentry.html')

    def test_user_logentry(self):
        """Tests if user_logentry page renders correctly """
        response = self.client.get('/user_logentry/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_logentry.html')

    def test_add_country(self):
        """Tests if add_country page renders correctly """
        response = self.client.get('/add_country/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_country.html')
