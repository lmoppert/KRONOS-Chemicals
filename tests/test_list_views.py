# from model_mommy.recipe import Recipe, foreign_key
# from django.utils.translation import activate
from django.core.urlresolvers import reverse
from django.test import TestCase
from model_mommy import mommy
from chemicals import models
from chemicals.tests.utils import TestUsers


class ChemicalList(TestCase):
    "Testing the list view for chemicals"

    def SetUp(self):
        users = TestUsers()
        self.assertTrue(users.login(users.superadmin))

    def test_redirect_from_root(self):
        self.assertEqual(self.client.get('/').status_code, 302)

    def test_view_chemical_detail(self):
        obj = mommy.make(models.Chemical, make_m2m=True)
        url = reverse('chemical_detail', kwargs={'pk': obj.pk})
        response = self.client.get(url)
        msg = "Error getting URL {}".format(url)
        self.assertEqual(response.status_code, 200, msg)
        self.assertContains(response, obj.name)

    # This one ist still failing with 404, maybe objects missing?
    # def test_view_chemical_list(self):
    #     mommy.make(models.Chemical, make_m2m=True, _quantity=30)
    #     response = self.client.get(reverse('chemical_list'))
    #     self.assertEqual(response.status_code, 200)

    def test_view_consumer_list(self):
        mommy.make(models.Consumer, make_m2m=True, _quantity=30)
        response = self.client.get(reverse('supplier_list'))
        self.assertEqual(response.status_code, 200)
