from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import VaccineRegistration


class AuthFlowTests(TestCase):
    def test_signup_then_login(self):
        resp = self.client.post(reverse('registerPage'), {
            'username': 'tester', 'password1': 'Str0ng-pass-123', 'password2': 'Str0ng-pass-123'})
        self.assertRedirects(resp, reverse('loginPage'))
        resp = self.client.post(reverse('loginPage'), {'u': 'tester', 'p': 'Str0ng-pass-123'})
        self.assertRedirects(resp, reverse('userProfile'))

    def test_logout_url_resolves(self):
        self.assertEqual(reverse('logout'), '/logout/')

    def test_pages_require_login(self):
        resp = self.client.get(reverse('userProfile'))
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse('loginPage'), resp['Location'])


class RegistrationTests(TestCase):
    def setUp(self):
        User.objects.create_user('staff', password='Str0ng-pass-123')
        self.client.login(username='staff', password='Str0ng-pass-123')

    def _register(self, nid='1234567890'):
        return self.client.post(reverse('vacRegistration'), {
            'name': 'Test Person', 'address': 'Dhaka', 'mobile': '01000000000',
            'nid': nid, 'p_vac': 'PFIZER'})

    def test_register_edit_delete(self):
        self.assertRedirects(self._register(), reverse('userProfile'))
        reg = VaccineRegistration.objects.get(nid='1234567890')
        self.assertEqual(reg.a_vac, 'Not Assigned')
        self.assertFalse(reg.vaced)

        resp = self.client.post(reverse('editDetails', args=[reg.id]), {
            'name': 'Renamed', 'address': 'Dhaka', 'mobile': '01000000000',
            'nid': '1234567890', 'p_vac': 'MODERNA'})
        self.assertRedirects(resp, reverse('userProfile'))
        reg.refresh_from_db()
        self.assertEqual((reg.name, reg.p_vac), ('Renamed', 'MODERNA'))

        self.assertEqual(self.client.get(reverse('certificate', args=[reg.id])).status_code, 200)
        self.client.post(reverse('deleteDetails', args=[reg.id]))
        self.assertFalse(VaccineRegistration.objects.exists())

    def test_duplicate_nid_rejected(self):
        self._register()
        resp = self._register()
        self.assertEqual(resp.status_code, 200)  # form re-rendered with an error
        self.assertEqual(VaccineRegistration.objects.count(), 1)

    def test_missing_record_is_404(self):
        self.assertEqual(self.client.get(reverse('certificate', args=[999])).status_code, 404)
