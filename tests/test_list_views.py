# from model_mommy.recipe import Recipe, foreign_key
# from django.utils.translation import activate
from django.core.urlresolvers import reverse
from django.test import TestCase
from model_mommy import mommy
from chemicals import models


class ChemicalList(TestCase):
    "Testing the list view for chemicals"

    def test_redirect_from_root(self):
        self.assertEqual(self.client.get('/').status_code, 302)
