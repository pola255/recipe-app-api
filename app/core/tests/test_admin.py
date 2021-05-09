from django.test import TestCase 
from django.contrib.auth import get_user_model
# generate url from Django admin page
from django.urls import reverse
# Give test request to aor application
from django.test import Client


class AdminSiteTests(TestCase):
    # Run before every test run
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        # help automatically login to test
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test User Full Name',
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        # Generate url for our user page
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        # assertContains is a Django customization that check on contain
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
