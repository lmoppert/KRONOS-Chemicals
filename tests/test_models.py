from django.core.urlresolvers import reverse
from django.test import TestCase
from chemicals import models
from model_mommy import mommy


class ChecklistTest(TestCase):
    "Test the models contained in the checklist.py file"

    def test_model_check_usage(self):
        obj = mommy.make(models.CheckUsage)
        self.assertTrue(isinstance(obj, models.CheckUsage))
        self.assertEqual(obj.__unicode__(), obj.description)


class PeripheryTest(TestCase):
    "Test the models contained in the periphery.py file"

    def test_model_person(self):
        obj = mommy.make(models.Person)
        result = "{} {}".format(obj.surname, obj.givenname)
        self.assertTrue(isinstance(obj, models.Person))
        self.assertEqual(obj.name, result)
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_supplier(self):
        obj = mommy.make(models.Supplier)
        url = reverse('supplier_detail', kwargs={'pk': obj.pk})
        self.assertTrue(isinstance(obj, models.Supplier))
        self.assertEqual(obj.get_absolute_url(), url)
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_plant(self):
        obj = mommy.make(models.Plant)
        self.assertTrue(isinstance(obj, models.Plant))
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_department(self):
        obj = mommy.make(models.Department)
        url = reverse('department_detail', kwargs={'pk': obj.pk})
        self.assertTrue(isinstance(obj, models.Department))
        self.assertEqual(obj.get_absolute_url(), url)
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_profile(self):
        obj = mommy.make(models.Profile)
        self.assertTrue(isinstance(obj, models.Profile))
        self.assertEqual(obj.__unicode__(), obj.user.get_full_name())

    def test_model_location(self):
        obj = mommy.make(models.Location)
        url = reverse('stock_location_list', kwargs={'pk': obj.pk})
        self.assertTrue(isinstance(obj, models.Location))
        self.assertEqual(obj.get_absolute_url(), url)
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_consumer(self):
        d = mommy.make(models.Department)
        l = mommy.make(models.Location, department=d)
        c = mommy.make(models.Chemical)
        obj = mommy.make(models.Consumer, chemical=c, department=d)
        stocks = mommy.make(models.Stock, _quantity=10, chemical=c)
        self.assertEqual(len(stocks), 10)
        self.assertEqual(len(obj.stocks), 0)
        stocks[0].location = l
        stocks[0].save()
        self.assertEqual(len(obj.stocks), 1)


class ChemicalsTest(TestCase):
    "Test the models contained in the chemical.py file"

    def test_model_chemical(self):
        obj = mommy.make(models.Chemical, make_m2m=True)
        url = reverse('chemical_detail', kwargs={'pk': obj.pk})
        self.assertTrue(isinstance(obj, models.Chemical))
        self.assertEqual(obj.get_absolute_url(), url)
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_chemical_documents(self):
        from datetime import date
        obj = mommy.make(models.Chemical)
        cd = date.today()
        df = mommy.make(models.Document, doctype='f', chemical=obj, created=cd)
        di = mommy.make(models.Document, doctype='i', chemical=obj, created=cd)
        dfs = obj.get_approval_documents()
        dis = obj.get_info_documents()
        self.assertEqual(len(obj.document_set.all()), 2)
        self.assertEqual(len(dfs), 1)
        self.assertEqual(len(dis), 1)
        self.assertEqual(dfs[0], df)
        self.assertEqual(dis[0], di)

    def test_model_chemical_properties(self):
        obj = mommy.make(models.Chemical)
        self.assertFalse(obj.cmr1)
        self.assertFalse(obj.cmr2)
        h9 = mommy.make(models.HPhrase, cmr=9, seveso_relevant=False)
        models.HPhraseRelation(chemical=obj, hphrase=h9).save()
        self.assertFalse(obj.cmr1)
        self.assertFalse(obj.cmr2)
        self.assertFalse(obj.seveso_relevant)
        h2 = mommy.make(models.HPhrase, cmr=2, seveso_relevant=True)
        models.HPhraseRelation(chemical=obj, hphrase=h2).save()
        self.assertFalse(obj.cmr1)
        self.assertTrue(obj.cmr2)
        self.assertTrue(obj.seveso_relevant)
        h1 = mommy.make(models.HPhrase, cmr=1, seveso_relevant=False)
        models.HPhraseRelation(chemical=obj, hphrase=h1).save()
        self.assertTrue(obj.cmr1)
        self.assertFalse(obj.cmr2)
        self.assertTrue(obj.seveso_relevant)

    def test_model_synonym(self):
        obj = mommy.make(models.Synonym)
        self.assertTrue(isinstance(obj, models.Synonym))
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_risk_indication(self):
        obj = mommy.make(models.RiskIndication)
        self.assertTrue(isinstance(obj, models.RiskIndication))
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_pictogram(self):
        obj = mommy.make(models.Pictogram)
        self.assertTrue(isinstance(obj, models.Pictogram))
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_model_toxdata(self):
        obj = mommy.make(models.Toxdata)
        self.assertTrue(isinstance(obj, models.Toxdata))
        self.assertEqual(obj.__unicode__(), obj.supplier.name)

    def test_model_risk(self):
        obj = mommy.make(models.Risk)
        self.assertTrue(isinstance(obj, models.Risk))
        self.assertEqual(obj.__unicode__(), obj.riskindication.name)

    def test_model_reach_information(self):
        obj = mommy.make(models.ReachInformation)
        self.assertTrue(isinstance(obj, models.ReachInformation))
        self.assertEqual(obj.__unicode__(), obj.description)

    def test_model_seveso_information(self):
        obj = mommy.make(models.SevesoInformation)
        self.assertTrue(isinstance(obj, models.SevesoInformation))
        self.assertEqual(obj.__unicode__(), obj.description)

    def test_model_hphrase_relation(self):
        obj = mommy.make(models.HPhraseRelation)
        self.assertTrue(isinstance(obj, models.HPhraseRelation))
        self.assertEqual(obj.__unicode__(), obj.hphrase.name)

    def test_model_hphrase(self):
        obj = mommy.make(models.HPhrase)
        result = "{} - {}".format(obj.name, obj.description)
        self.assertTrue(isinstance(obj, models.HPhrase))
        self.assertEqual(obj.__unicode__(), result)

    def test_model_pphrase(self):
        obj = mommy.make(models.PPhrase)
        result = "{} - {}".format(obj.name, obj.description)
        self.assertTrue(isinstance(obj, models.PPhrase))
        self.assertEqual(obj.__unicode__(), result)

    def test_model_rphrase(self):
        obj = mommy.make(models.RPhrase)
        result = "{} - {}".format(obj.name, obj.description)
        self.assertTrue(isinstance(obj, models.RPhrase))
        self.assertEqual(obj.__unicode__(), result)

    def test_model_wgk(self):
        obj = mommy.make(models.WGK)
        result = "{} - {}".format(obj.name, obj.description)
        self.assertTrue(isinstance(obj, models.WGK))
        self.assertEqual(obj.__unicode__(), result)

    def test_model_seveso_category(self):
        obj = mommy.make(models.SevesoCategory)
        result = "{} - {}".format(obj.name, obj.description)
        self.assertTrue(isinstance(obj, models.SevesoCategory))
        self.assertEqual(obj.__unicode__(), result)

    def test_model_storage_class(self):
        obj = mommy.make(models.StorageClass)
        result = "{} - {}".format(obj.name, obj.description)
        self.assertTrue(isinstance(obj, models.StorageClass))
        self.assertEqual(obj.__unicode__(), result)
