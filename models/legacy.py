# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class KronosChecklist(models.Model):
    checklistid = models.IntegerField(db_column='ChecklistID', primary_key=True)
    arbeitsplatzid = models.IntegerField(db_column='ArbeitsplatzID')
    chemicalid = models.IntegerField(db_column='ChemicalID')
    countrycode = models.CharField(db_column='CountryCode', max_length=100)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList'


class KronosChecklistAnwendung(models.Model):
    anwendungid = models.IntegerField(db_column='AnwendungID', primary_key=True)
    anwendung = models.CharField(db_column='Anwendung', max_length=100)
    countrycode = models.CharField(max_length=24)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_Anwendung'


class KronosChecklistInformation(models.Model):
    check_infoid = models.IntegerField(db_column='Check_InfoID', primary_key=True)
    checklistid = models.IntegerField(db_column='CheckListID')
    kapitelid = models.IntegerField(db_column='KapitelID')
    information = models.TextField(db_column='Information', blank=True)
    countrycode = models.CharField(max_length=24)
    anbetrieb = models.IntegerField(db_column='AnBetrieb', blank=True, null=True)
    vonbetrieb = models.IntegerField(db_column='VonBetrieb', blank=True, null=True)
    uws = models.IntegerField(db_column='UWS', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_Information'


class KronosChecklistKapitel(models.Model):
    kapitelid = models.IntegerField(db_column='KapitelID', primary_key=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_Kapitel'


class KronosChecklistKapiteltext(models.Model):
    kapiteltextid = models.IntegerField(db_column='KapitelTextID', primary_key=True)
    kapiteltext = models.TextField(db_column='KapitelText', blank=True)
    kapitelid = models.ForeignKey(KronosChecklistKapitel, db_column='KapitelID')
    countrycode = models.CharField(db_column='CountryCode', max_length=100)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_KapitelText'


class KronosChecklistKapitelTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    kapitelid = models.ForeignKey(KronosChecklistKapitel, db_column='KapitelID')
    kapitel = models.TextField(db_column='Kapitel', blank=True)
    countrycode = models.CharField(db_column='CountryCode', max_length=100)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_Kapitel_Translation'


class KronosChecklistMasnahme(models.Model):
    masnahmeid = models.IntegerField(db_column='MasnahmeID')
    kapitelid = models.IntegerField(db_column='KapitelID')
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_Masnahme'


class KronosChecklistMasnahmeTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    masnahmeid = models.ForeignKey(KronosChecklistMasnahme, db_column='MasnahmeID')
    masnahme = models.TextField(db_column='Masnahme', blank=True)
    countrycode = models.CharField(db_column='CountryCode', max_length=100)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_Masnahme_Translation'


class KronosChecklistPsa(models.Model):
    psa_id = models.IntegerField(db_column='PSA_ID', primary_key=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_PSA'


class KronosChecklistPsaArtikel(models.Model):
    psa_artikelid = models.IntegerField(db_column='PSA_ArtikelID', primary_key=True)
    psa_artikel = models.TextField(db_column='PSA_Artikel', blank=True)
    countrycode = models.CharField(db_column='CountryCode', max_length=100)
    psa = models.ForeignKey(KronosChecklistPsa, db_column='PSA_ID')
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_PSA_Artikel'


class KronosChecklistPsaImg(models.Model):
    psa_imgid = models.IntegerField(db_column='PSA_imgID', primary_key=True)
    psa_id = models.IntegerField(db_column='PSA_ID')
    path = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_PSA_Img'


class KronosChecklistPsaTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    psa = models.ForeignKey(KronosChecklistPsa, db_column='PSA_ID')
    psa_0 = models.TextField(db_column='PSA', blank=True)
    countrycode = models.CharField(db_column='CountryCode', max_length=100)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_PSA_Translation'


class KronosChecklistStatus(models.Model):
    checklist_statusid = models.IntegerField(db_column='CheckList_StatusID', primary_key=True)
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    startdate = models.DateTimeField(db_column='StartDate')
    startby = models.IntegerField(db_column='StartBy')
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)
    closeddate = models.DateTimeField(db_column='ClosedDate', blank=True, null=True)
    closedby = models.IntegerField(db_column='ClosedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_CheckList_Status'


class KronosCheckAnwendung(models.Model):
    anwendungid = models.ForeignKey(KronosChecklistAnwendung, db_column='AnwendungID')
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    countrycode = models.ForeignKey(KronosChecklistAnwendung, db_column='countrycode', related_name='cc')

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_Anwendung'


class KronosCheckHphrase(models.Model):
    hphrase_id = models.CharField(db_column='hphrase_ID', max_length=40)
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    countrycode = models.CharField(max_length=24)
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_HPhrase'


class KronosCheckKapiteltext(models.Model):
    kapiteltextid = models.ForeignKey(KronosChecklistKapiteltext, db_column='KapitelTextID')
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_KapitelText'


class KronosCheckMasnahme(models.Model):
    masnahmeid = models.ForeignKey(KronosChecklistMasnahme, db_column='MasnahmeID')
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    erledigt = models.IntegerField(db_column='Erledigt', blank=True, null=True)
    erledigtdate = models.DateTimeField(db_column='Erledigtdate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_Masnahme'


class KronosCheckPphrase(models.Model):
    pphrase = models.ForeignKey('StoffePphrase', db_column='pphrase_ID')
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_PPhrase'


class KronosCheckPsaArtikel(models.Model):
    psa_artikelid = models.ForeignKey(KronosChecklistPsaArtikel, db_column='PSA_ArtikelID')
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_PSA_Artikel'


class KronosCheckPsaImg(models.Model):
    checklistid = models.IntegerField(db_column='CheckListID')
    psa_imgid = models.IntegerField(db_column='PSA_imgID')
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_PSA_Img'


class KronosCheckParameter(models.Model):
    checklistid = models.IntegerField(db_column='CheckListID')
    stoffparameterid = models.IntegerField(db_column='StoffParameterID')
    grenzwertparameterid = models.IntegerField(db_column='GrenzwertParameterID')
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_Parameter'


class KronosCheckPictogramm(models.Model):
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    pictogramm = models.ForeignKey('StoffePictogramm', db_column='pictogramm_ID')
    signal_id = models.IntegerField(db_column='signal_ID', blank=True, null=True)
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_Pictogramm'


class KronosCheckStorageclass(models.Model):
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    storageclassid = models.ForeignKey('StoffeStorageclass', db_column='storageclassID')
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_StorageClass'


class KronosCheckWgk(models.Model):
    wgk = models.ForeignKey('StoffeWgk', db_column='wgk_ID')
    checklistid = models.ForeignKey(KronosChecklist, db_column='CheckListID')
    betriebinfo = models.IntegerField(db_column='BetriebInfo')
    personinfo = models.IntegerField(db_column='PersonInfo')
    erledigt = models.IntegerField(db_column='Erledigt')
    erledigtdate = models.DateTimeField(db_column='ErledigtDate', blank=True, null=True)
    erledigtby = models.IntegerField(db_column='ErledigtBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KRONOS_Check_WGK'


class StoffHistorie(models.Model):
    stoffhistorieid = models.IntegerField(db_column='StoffHistorieID', primary_key=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy')
    modifieddate = models.DateTimeField(db_column='ModifiedDate')
    modifiedtyp = models.CharField(db_column='ModifiedTyp', max_length=100)
    stofftableid = models.IntegerField(db_column='StoffTableID')
    chemicalid = models.IntegerField(db_column='ChemicalID')
    primobjektid = models.CharField(db_column='PrimObjektID', max_length=100, blank=True)
    subobjektid = models.CharField(db_column='SubObjektID', max_length=100, blank=True)
    infoobjektname = models.CharField(db_column='InfoObjektName', max_length=100, blank=True)
    infoobjekt = models.TextField(db_column='InfoObjekt', blank=True)
    countrycode = models.CharField(db_column='CountryCode', max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'Stoff_Historie'


class StoffTables(models.Model):
    stofftableid = models.IntegerField(db_column='StoffTableID')
    stofftablename = models.TextField(db_column='StoffTableName')

    class Meta:
        managed = False
        db_table = 'Stoff_Tables'


class ReachChemContact(models.Model):
    chemical_id = models.IntegerField(db_column='chemical_ID')
    contact_id = models.IntegerField(db_column='contact_ID')
    r_type_id = models.IntegerField(db_column='r_type_ID')

    class Meta:
        managed = False
        db_table = 'reach_Chem_Contact'


class ReachChemData(models.Model):
    data_id = models.IntegerField(db_column='data_ID', primary_key=True)
    substance = models.IntegerField(blank=True, null=True)
    preparation = models.IntegerField(blank=True, null=True)
    polymer = models.IntegerField(blank=True, null=True)
    article = models.IntegerField(blank=True, null=True)
    pre_reg = models.IntegerField(blank=True, null=True)
    pre_date = models.DateTimeField(blank=True, null=True)
    registration = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    reg_deadline = models.CharField(max_length=100, blank=True)
    annexiv = models.IntegerField(db_column='annexIV', blank=True, null=True)
    annexv = models.IntegerField(db_column='annexV', blank=True, null=True)
    undercharge = models.IntegerField(blank=True, null=True)
    chemical_id = models.IntegerField(db_column='chemical_ID')
    contact_id = models.IntegerField(db_column='contact_ID')
    rtype = models.CharField(db_column='Rtype', max_length=100, blank=True)
    info = models.TextField(db_column='Info', blank=True)
    preno = models.CharField(max_length=100, blank=True)
    regno = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'reach_Chem_Data'


class ReachStatement(models.Model):
    statement_id = models.IntegerField(db_column='statement_ID', primary_key=True)
    path = models.CharField(max_length=100)
    data_id = models.IntegerField(db_column='data_ID')
    sdate = models.DateTimeField(db_column='SDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reach_Statement'


class ReachStatus1(models.Model):
    rstatus_id = models.IntegerField(db_column='RStatus_ID', primary_key=True)
    sname = models.CharField(db_column='SName', max_length=100, blank=True)
    contact_id = models.IntegerField(db_column='Contact_ID')
    cname = models.CharField(db_column='CName', max_length=200, blank=True)
    chemical_id = models.IntegerField(db_column='Chemical_ID')
    dname = models.CharField(db_column='DName', max_length=100, blank=True)
    mname = models.CharField(db_column='MName', max_length=100, blank=True)
    rstatus = models.TextField(db_column='RStatus', blank=True)

    class Meta:
        managed = False
        db_table = 'reach_Status1'


class StoffeChemCas(models.Model):
    cas_no = models.CharField(db_column='CAS_No', max_length=100)
    chemical_id = models.IntegerField(db_column='chemical_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_CAS'


class StoffeChemContact(models.Model):
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    contact = models.ForeignKey('StoffeContact', db_column='contact_ID')
    contacttype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Contact'


class StoffeChemDep(models.Model):
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    department = models.ForeignKey('StoffeDepartment', db_column='department_ID')
    have_instruction = models.IntegerField(db_column='Have_Instruction', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Dep'


class StoffeChemDepContact(models.Model):
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    contact = models.ForeignKey('StoffeContact', db_column='contact_ID')
    department = models.ForeignKey('StoffeDepartment', db_column='department_ID')
    have_instruction = models.IntegerField(db_column='Have_Instruction', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Dep_Contact'


class StoffeChemGroup(models.Model):
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    group = models.ForeignKey('StoffeGroup', db_column='group_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Group'


class StoffeChemHphrase(models.Model):
    hphrase = models.CharField('StoffeHphrase', db_column='hphrase_ID', max_length=100)
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    info = models.TextField(blank=True)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_HPhrase'


class StoffeChemPphrase(models.Model):
    pphrase = models.CharField('StoffePphrase', db_column='pphrase_ID', max_length=100)
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_PPhrase'


class StoffeChemPictogramm(models.Model):
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    pictogramm = models.ForeignKey('StoffePictogramm', db_column='pictogramm_ID')
    signal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Pictogramm'


class StoffeChemRphrase(models.Model):
    rphrase = models.CharField('StoffeRphrase', db_column='rphrase_ID', max_length=100)
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_RPhrase'


class StoffeChemSevesoKategorie(models.Model):
    seveso_kategorie = models.CharField('StoffeSevesoKategorie', db_column='seveso_kategorie_ID', max_length=100)
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Seveso_Kategorie'


class StoffeChemStorageclass(models.Model):
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    storageclassid = models.ForeignKey('StoffeStorageclass', db_column='storageclassID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_StorageClass'


class StoffeChemSynonym(models.Model):
    synonym = models.ForeignKey('StoffeSynonym', db_column='synonym_ID')
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    countrycode = models.CharField('StoffeSynonym', db_column='countrycode', max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Synonym'


class StoffeChemTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    countrycode = models.CharField(max_length=24)
    name = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=800, blank=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_Translation'


class StoffeChemWgk(models.Model):
    wgk = models.CharField('StoffeWgk', db_column='wgk_ID', max_length=100)
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_WGK'


class StoffeChemProc(models.Model):
    proc = models.ForeignKey('StoffeProc', db_column='proc_ID')
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_proc'


class StoffeChemRisk(models.Model):
    chemical = models.ForeignKey('StoffeChemical', db_column='chemical_ID')
    riskindication = models.ForeignKey('StoffeRiskindication', db_column='riskindication_ID')
    info = models.TextField(blank=True)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Chem_risk'


class StoffeChemical(models.Model):
    chemical_id = models.IntegerField(db_column='chemical_ID', primary_key=True)
    cmr = models.IntegerField(db_column='CMR')
    needed = models.IntegerField()
    preparation = models.IntegerField()
    archive = models.IntegerField()
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)
    replaced = models.IntegerField(blank=True, null=True)
    article = models.CharField(max_length=100, blank=True)
    instruction = models.IntegerField()
    cas_no = models.CharField(db_column='CAS_No', max_length=100, blank=True)
    einecs = models.CharField(db_column='EINECS', max_length=100, blank=True)
    stoerfallstoff = models.IntegerField(db_column='Stoerfallstoff')
    reach_vo = models.IntegerField(db_column='Reach_VO')
    regno = models.CharField(db_column='RegNo', max_length=100, blank=True)
    regkomponents = models.IntegerField(db_column='RegKomponents', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Chemical'


class StoffeContact(models.Model):
    contact_id = models.IntegerField(db_column='contact_ID', primary_key=True)
    name = models.TextField()
    street = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=100, blank=True)
    plz = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=80, blank=True)
    country = models.CharField(max_length=80, blank=True)
    telefon = models.CharField(max_length=80, blank=True)
    fax = models.CharField(max_length=80, blank=True)
    mail = models.CharField(max_length=100, blank=True)
    www = models.CharField(max_length=100, blank=True)
    typ = models.IntegerField()
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=200, blank=True)
    contactinfo = models.TextField(db_column='ContactInfo', blank=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Contact'


class StoffeContactPerson(models.Model):
    contact = models.ForeignKey(StoffeContact, db_column='contact_ID')
    personid = models.ForeignKey('StoffePerson', db_column='personID')
    roule = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stoffe_Contact_Person'


class StoffeDepartment(models.Model):
    department_id = models.IntegerField(db_column='department_ID', primary_key=True)
    name = models.CharField(max_length=100)
    menufacturing = models.ForeignKey('StoffeMenufacturing', db_column='menufacturing_ID', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Department'


class StoffeDocument(models.Model):
    document_id = models.IntegerField(db_column='document_ID', primary_key=True)
    path = models.CharField(max_length=100)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    menufacturing = models.ForeignKey('StoffeMenufacturing', db_column='menufacturing_ID')
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    doctype = models.CharField(max_length=100)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Document'


class StoffeGroup(models.Model):
    group_id = models.IntegerField(db_column='group_ID', primary_key=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Group'


class StoffeGroupTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    group = models.ForeignKey(StoffeGroup, db_column='group_ID')
    name = models.CharField(max_length=100)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Group_Translation'


class StoffeHphrase(models.Model):
    hphrase_id = models.CharField(db_column='hphrase_ID', max_length=40)
    seveso_relevant = models.IntegerField()
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_HPhrase'


class StoffeHphraseTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    hphrase = models.ForeignKey(StoffeHphrase, db_column='hphrase_ID')
    name = models.CharField(max_length=400)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_HPhrase_Translation'


class StoffeLocation(models.Model):
    location_id = models.IntegerField(db_column='location_ID', primary_key=True)
    department = models.ForeignKey(StoffeDepartment, db_column='department_ID')
    name = models.CharField(max_length=100, blank=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Location'


class StoffeMenuTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    menufacturing = models.ForeignKey('StoffeMenufacturing', db_column='menufacturing_ID')
    name = models.CharField(max_length=100, blank=True)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Menu_Translation'


class StoffeMenufacturing(models.Model):
    menufacturing_id = models.IntegerField(db_column='menufacturing_ID', primary_key=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Menufacturing'


class StoffePphrase(models.Model):
    pphrase_id = models.CharField(db_column='pphrase_ID', max_length=40)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_PPhrase'


class StoffePphraseTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    pphrase = models.ForeignKey(StoffePphrase, db_column='pphrase_ID')
    name = models.CharField(max_length=400)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_PPhrase_Translation'


class StoffePerson(models.Model):
    personid = models.IntegerField(db_column='personID', primary_key=True)
    anrede = models.CharField(max_length=100, blank=True)
    titel = models.CharField(max_length=100, blank=True)
    vorname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100, blank=True)
    fax = models.CharField(max_length=100, blank=True)
    mail = models.CharField(max_length=100, blank=True)
    roule = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stoffe_Person'


class StoffePictoTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    pictogramm = models.ForeignKey('StoffePictogramm', db_column='pictogramm_ID')
    bezeichnung = models.CharField(db_column='Bezeichnung', max_length=400)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Picto_Translation'


class StoffePictogramm(models.Model):
    pictogramm_id = models.IntegerField(db_column='pictogramm_ID', primary_key=True)
    kodierung = models.CharField(max_length=100)
    path = models.CharField(max_length=100, blank=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Pictogramm'


class StoffeRphrase(models.Model):
    rphrase_id = models.CharField(db_column='rphrase_ID', max_length=40)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_RPhrase'


class StoffeRphraseTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    rphrase = models.ForeignKey(StoffeRphrase, db_column='rphrase_ID')
    name = models.CharField(max_length=400)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_RPhrase_Translation'


class StoffeReachDocument(models.Model):
    reach_docid = models.IntegerField(db_column='Reach_DocID', primary_key=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    reachdoc_path = models.TextField(db_column='ReachDoc_path')
    countrycode = models.CharField(db_column='Countrycode', max_length=24)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Reach_Document'


class StoffeReachInfo(models.Model):
    reach_infoid = models.IntegerField(db_column='Reach_InfoID', primary_key=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Reach_Info'


class StoffeReachInfoTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    reach_infoid = models.ForeignKey(StoffeReachInfo, db_column='Reach_InfoID')
    information = models.TextField(db_column='Information', blank=True)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Reach_Info_Translation'


class StoffeRiskRphrase(models.Model):
    rphrase_id = models.CharField(db_column='rphrase_ID', max_length=40)
    riskindication_id = models.IntegerField(db_column='riskindication_ID')

    class Meta:
        managed = False
        db_table = 'stoffe_Risk_RPhrase'


class StoffeRiskTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    riskindication = models.ForeignKey('StoffeRiskindication', db_column='riskindication_ID')
    name = models.CharField(max_length=100)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Risk_Translation'


class StoffeRiskindication(models.Model):
    riskindication_id = models.IntegerField(db_column='riskindication_ID', primary_key=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Riskindication'


class StoffeSafetydatasheet(models.Model):
    safetydatasheet_id = models.IntegerField(db_column='safetydatasheet_ID', primary_key=True)
    path = models.CharField(max_length=100, blank=True)
    instruction = models.IntegerField(blank=True, null=True)
    issuedate = models.DateTimeField(blank=True, null=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    supplier = models.ForeignKey(StoffeContact, db_column='supplier_ID')
    countrycode = models.CharField(db_column='CountryCode', max_length=24)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_SafetyDataSheet'


class StoffeSevesoproductlist(models.Model):
    sevesoproductlistid = models.IntegerField(db_column='SevesoProductListID', primary_key=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='Chemical_ID')
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_SevesoProductList'


class StoffeSevesoDocument(models.Model):
    seveso_docid = models.IntegerField(db_column='Seveso_DocID', primary_key=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    doc_path = models.TextField(db_column='Doc_path')
    countrycode = models.CharField(db_column='Countrycode', max_length=24)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Seveso_Document'


class StoffeSevesoInfo(models.Model):
    seveso_infoid = models.IntegerField(db_column='Seveso_InfoID', primary_key=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Seveso_Info'


class StoffeSevesoInfoTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    seveso_infoid = models.ForeignKey(StoffeSevesoInfo, db_column='Seveso_InfoID')
    information = models.TextField(db_column='Information')
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Seveso_Info_Translation'


class StoffeSevesoKategorie(models.Model):
    seveso_kategorie_id = models.CharField(db_column='Seveso_Kategorie_ID', max_length=40)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Seveso_Kategorie'


class StoffeSevesoKategorieTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    seveso_kategorie = models.ForeignKey(StoffeSevesoKategorie, db_column='Seveso_Kategorie_ID')
    name = models.TextField()
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Seveso_Kategorie_Translation'


class StoffeSignalTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    signal_id = models.IntegerField(db_column='Signal_ID')
    signal = models.CharField(db_column='Signal', max_length=100)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_Signal_Translation'


class StoffeStock(models.Model):
    stock_id = models.IntegerField(db_column='stock_ID', primary_key=True)
    volumestock = models.CharField(max_length=100)
    unitstock = models.CharField(max_length=100)
    location = models.ForeignKey(StoffeLocation, db_column='location_ID')
    volumeyear = models.CharField(max_length=100, blank=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    unityear = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Stock'


class StoffeStorageclass(models.Model):
    storageclassid = models.IntegerField(db_column='storageclassID', primary_key=True)
    classification = models.CharField(max_length=100)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_StorageClass'


class StoffeStorageclassTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    storageclassid = models.ForeignKey(StoffeStorageclass, db_column='storageclassID')
    description = models.TextField()
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_StorageClass_Translation'


class StoffeSynonym(models.Model):
    synonym_id = models.IntegerField(db_column='synonym_ID', primary_key=True)
    name = models.CharField(max_length=100)
    countrycode = models.CharField(max_length=24)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_Synonym'


class StoffeToxdata(models.Model):
    toxid = models.IntegerField(db_column='ToxID')
    chemical_id = models.IntegerField(db_column='chemical_ID')
    supplier_id = models.IntegerField(db_column='supplier_ID')
    toxdata = models.IntegerField(db_column='ToxData')
    oekotoxdata = models.IntegerField(db_column='OekotoxData')
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_ToxData'


class StoffeWgk(models.Model):
    wgk_id = models.CharField(db_column='wgk_ID', max_length=40)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_WGK'


class StoffeWgkTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    wgk = models.ForeignKey(StoffeWgk, db_column='WGK_ID')
    name = models.CharField(max_length=400)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_WGK_Translation'


class StoffeEsafetydatasheet(models.Model):
    esafetydatasheet_id = models.IntegerField(db_column='esafetydatasheet_ID', primary_key=True)
    path = models.CharField(max_length=100, blank=True)
    instruction = models.IntegerField(blank=True, null=True)
    issuedate = models.DateTimeField(blank=True, null=True)
    chemical = models.ForeignKey(StoffeChemical, db_column='chemical_ID')
    supplier = models.ForeignKey(StoffeContact, db_column='supplier_ID')
    countrycode = models.CharField(db_column='CountryCode', max_length=24)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_eSafetyDataSheet'


class StoffeProc(models.Model):
    proc_id = models.CharField(db_column='proc_ID', max_length=40)
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stoffe_proc'


class StoffeProcTranslation(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    proc = models.ForeignKey(StoffeProc, db_column='proc_ID')
    name = models.CharField(max_length=400)
    countrycode = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'stoffe_proc_Translation'


class DummyTranslation(models.Model):
    name = models.CharField(max_length=100, blank=True, default=None, null=True)
    comment = models.CharField(max_length=800, blank=True, default=None, null=True)
    information = models.TextField(blank=True, default=None, null=True)
    kapitel = models.TextField(blank=True, default=None, null=True)
    masnahme = models.TextField(blank=True, default=None, null=True)
    psa_0 = models.TextField(blank=True, default=None, null=True)
    bezeichnung = models.CharField(max_length=400, default=None, null=True)
    description = models.TextField(blank=True, default=None, null=True)
    signal = models.CharField(db_column='Signal', max_length=100, blank=True, default=None, null=True)

    class Meta:
        db_table = 'Dummy_Translation'


class LegacyFiles(models.Model):
    fileid = models.IntegerField(db_column='FileId', primary_key=True)
    portalid = models.IntegerField(db_column='PortalId', blank=True, null=True)
    filename = models.CharField(db_column='FileName', max_length=200)
    extension = models.CharField(db_column='Extension', max_length=200)
    size = models.IntegerField(db_column='Size')
    width = models.IntegerField(db_column='Width', blank=True, null=True)
    height = models.IntegerField(db_column='Height', blank=True, null=True)
    contenttype = models.CharField(db_column='ContentType', max_length=400)
    folder = models.CharField(db_column='Folder', max_length=400, blank=True)
    # folderid = models.ForeignKey('Folders', db_column='FolderID')
    content = models.TextField(db_column='Content', blank=True)

    class Meta:
        managed = False
        db_table = 'Files'


class Profilepropertydefinition(models.Model):
    propertydefinitionid = models.IntegerField(db_column='PropertyDefinitionID', primary_key=True)
    portalid = models.IntegerField(db_column='PortalID', blank=True, null=True)
    moduledefid = models.IntegerField(db_column='ModuleDefID', blank=True, null=True)
    deleted = models.IntegerField(db_column='Deleted')
    datatype = models.IntegerField(db_column='DataType')
    defaultvalue = models.TextField(db_column='DefaultValue', blank=True)
    propertycategory = models.CharField(db_column='PropertyCategory', max_length=100)
    propertyname = models.CharField(db_column='PropertyName', max_length=100)
    length = models.IntegerField(db_column='Length')
    required = models.IntegerField(db_column='Required')
    validationexpression = models.CharField(db_column='ValidationExpression', max_length=4000, blank=True)
    vieworder = models.IntegerField(db_column='ViewOrder')
    visible = models.IntegerField(db_column='Visible')

    class Meta:
        managed = False
        db_table = 'ProfilePropertyDefinition'


class Roles(models.Model):
    roleid = models.IntegerField(db_column='RoleID', primary_key=True) # Field name made lowercase.
    portalid = models.IntegerField(db_column='PortalID') # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=100) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, blank=True) # Field name made lowercase.
    servicefee = models.DecimalField(db_column='ServiceFee', max_digits=19, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    billingfrequency = models.CharField(db_column='BillingFrequency', max_length=1, blank=True) # Field name made lowercase.
    trialperiod = models.IntegerField(db_column='TrialPeriod', blank=True, null=True) # Field name made lowercase.
    trialfrequency = models.CharField(db_column='TrialFrequency', max_length=1, blank=True) # Field name made lowercase.
    billingperiod = models.IntegerField(db_column='BillingPeriod', blank=True, null=True) # Field name made lowercase.
    trialfee = models.DecimalField(db_column='TrialFee', max_digits=19, decimal_places=4, blank=True, null=True) # Field name made lowercase.
    ispublic = models.IntegerField(db_column='IsPublic') # Field name made lowercase.
    autoassignment = models.IntegerField(db_column='AutoAssignment') # Field name made lowercase.
    rolegroupid = models.IntegerField(db_column='RoleGroupID', blank=True, null=True) # Field name made lowercase.
    rsvpcode = models.CharField(db_column='RSVPCode', max_length=100, blank=True) # Field name made lowercase.
    iconfile = models.CharField(db_column='IconFile', max_length=200, blank=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Userprofile(models.Model):
    profileid = models.IntegerField(db_column='ProfileID', primary_key=True)
    userid = models.ForeignKey('Users', db_column='UserID')
    propertydefinitionid = models.ForeignKey(Profilepropertydefinition, db_column='PropertyDefinitionID')
    propertyvalue = models.CharField(db_column='PropertyValue', max_length=7500, blank=True)
    propertytext = models.TextField(db_column='PropertyText', blank=True)
    visibility = models.IntegerField(db_column='Visibility')
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate')

    class Meta:
        managed = False
        db_table = 'UserProfile'


class Userroles(models.Model):
    userroleid = models.IntegerField(db_column='UserRoleID', primary_key=True)
    userid = models.ForeignKey('Users', db_column='UserID')
    roleid = models.ForeignKey(Roles, db_column='RoleID')
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)
    istrialused = models.IntegerField(db_column='IsTrialUsed', blank=True, null=True)
    effectivedate = models.DateTimeField(db_column='EffectiveDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserRoles'


class Users(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)
    username = models.CharField(db_column='Username', unique=True, max_length=200)
    firstname = models.CharField(db_column='FirstName', max_length=100)
    lastname = models.CharField(db_column='LastName', max_length=100)
    issuperuser = models.IntegerField(db_column='IsSuperUser')
    affiliateid = models.IntegerField(db_column='AffiliateId', blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=512, blank=True)
    displayname = models.CharField(db_column='DisplayName', max_length=256)
    updatepassword = models.IntegerField(db_column='UpdatePassword')

    class Meta:
        managed = False
        db_table = 'Users'
