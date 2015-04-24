from django.core.urlresolvers import reverse
from django.test import TestCase
from model_mommy import mommy
from chemicals import models, admin
from chemicals.tests.utils import TestUsers


class ChemicalAdminTest(TestCase):
    "Test custom admin functions"

    def SetUp(self):
        users = TestUsers()
        self.assertTrue(users.login(users.superadmin))

    def count_archived(self):
        return models.Chemical.objects.filter(archive=True).count()

    def count_active(self):
        return models.Chemical.objects.filter(archive=False).count()

    def test_archive_chemicals(self):
        active = mommy.make(models.Chemical, archive=False, _quantity=5)
        archived = mommy.make(models.Chemical, archive=True, _quantity=4)
        change_url = reverse('admin:chemicals_chemical_changelist')
        self.assertEqual(self.count_active(), 5)
        self.assertEqual(self.count_archived(), 4)
        sel = [active[0].pk, active[1].pk]
        data = {'action': 'archive_chemicals', '_selected_action': sel}
        response = self.client.post(change_url, data)
        self.assertTrue(response.status_code, 302)
        self.assertEqual(self.count_active(), 3)
        self.assertEqual(self.count_archived(), 6)

    def test_unarchive_chemicals(self):
        active = mommy.make(models.Chemical, archive=False, _quantity=5)
        archived = mommy.make(models.Chemical, archive=True, _quantity=4)
        change_url = reverse('admin:chemicals_chemical_changelist')
        self.assertEqual(self.count_active(), 5)
        self.assertEqual(self.count_archived(), 4)
        sel = [archived[0].pk, archived[0].pk, archived[0].pk]
        data = {'action': 'unarchive_chemicals', '_selected_action': sel}
        response = self.client.post(change_url, data)
        self.assertTrue(response.status_code, 302)
        self.assertEqual(self.count_active(), 8)
        self.assertEqual(self.count_archived(), 1)
