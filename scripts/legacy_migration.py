from django.contrib.auth.models import User
from filer.models.filemodels import File
from filer.models.foldermodels import Folder
#from chemicals.models.checklist import (
#    CheckList, CheckSection, CheckUsage, HPhraseCheck, PPE, PPECheck,
#    PPhraseCheck, PictogramCheck, StorageClassCheck, WGKCheck)
from chemicals.models.periphery import (
    Contact, Person, Role, Department, Plant, Location, Stock, Supplier)
from chemicals.models.substance import (
    Chemical, RiskIndication, StorageClass, SevesoCategory, HPhrase, Toxdata,
    WGK, RPhrase, PPhrase, Risk, HPhraseRelation, Pictogram, Document, Signal,
    SevesoDocument, ReachDocument, SafetyDataSheet, ExtendedSafetyDataSheet)
# Synonym
from chemicals.models.legacy import (
    StoffeChemical, StoffeChemTranslation, StoffeWgk, StoffeWgkTranslation,
    StoffeStorageclass, StoffeStorageclassTranslation, StoffeSevesoKategorie,
    StoffeSevesoKategorieTranslation, StoffeHphrase, StoffeHphraseTranslation,
    StoffePphrase, StoffePphraseTranslation, StoffeRphrase, StoffeReachInfo,
    StoffeReachInfoTranslation, StoffeSevesoInfo, StoffeSevesoInfoTranslation,
    StoffeRphraseTranslation, StoffeRiskindication, StoffeRiskTranslation,
    StoffeChemWgk, StoffeChemRisk, StoffeChemStorageclass, StoffeChemHphrase,
    StoffeChemSevesoKategorie, StoffeChemRphrase, StoffeChemPphrase,
    StoffePerson, StoffeContact, StoffeContactPerson, StoffeMenufacturing,
    StoffeMenuTranslation, StoffeDepartment, StoffeLocation, StoffeStock,
    StoffeChemDepContact, StoffeChemContact, StoffePictoTranslation, Users,
    StoffeChemPictogramm, StoffePictogramm, StoffeDocument, StoffeToxdata,
    StoffeReachDocument, StoffeSevesoDocument, StoffeEsafetydatasheet,
    StoffeSafetydatasheet, LegacyFiles, DummyTranslation)

CountryCodes = ('en-en', 'de-de', 'nl-be')


##############################################################################
# Helper methods
##############################################################################
def get_translations(TransTable, ObjID):
    trans = {}
    for code in CountryCodes:
        try:
            obj = TransTable.objects.using('legacy').get(id=str(ObjID) + code)
            if 'default' not in trans:
                trans['default'] = obj
        except:
            obj = DummyTranslation.objects.using('legacy').create()
        trans[code] = obj
    return trans


def get_language(s):
    if s == 'de-DE' or s == 'de-de':
        return 'de'
    elif s == 'nl-BE' or s == 'nl-be' or s == 'be-be':
        return 'nl'
    else:
        return 'en'


def get_term(s):
    if s == 1:
        return 'd'
    elif s == 2:
        return 'w'
    else:
        return 'n'


def get_file_handle(s):
    try:
        leg_file = LegacyFiles.objects.using('legacy').get(fileid=int(s[7:]))
    except:
        return None
    fid = 6  # The ID of the "Stoff-Portal" folder
    for fname in leg_file.folder[:-1].split("/"):
        fobj = Folder.objects.get(parent_id=fid, name=fname)
        fid = fobj.id
    try:
        handle = File.objects.get(original_filename=leg_file.filename,
                                  folder_id=fid)
    except:
        print "File not found: %s" % s
        return
    return handle


def make_unit(s):
    if s == 't' or s == 'g' or s == 'l':
        return s
    elif s == 'kg':
        return 'k'
    elif s == 'm3':
        return 'c'
    elif s == 'ml':
        return 'm'
    else:
        return 'p'


def make_address(info, street, number, zip, city):
    if info:
        address = info + ",\n"
    else:
        address = ""
    if street or number:
        address += street
        if street and number:
            address += " "
        address += number or ""
        address += ",\n"
    if zip or city:
        address += zip or ""
        if zip and city:
            address += " "
        address += city or ""
    return address


##############################################################################
# Create methods for the independent models
##############################################################################
def create_users():
    count = 0
    objs = Users.objects.using('legacy').all()
    print "Found %s Users, processing migrattion..." % objs.count()
    for obj in objs:
        oid = obj.userid
        if oid < 10 or oid == 114:
            continue
        count += 1
        User.objects.create(
            id=oid,
            username=obj.username,
            first_name=obj.firstname,
            last_name=obj.lastname,
            email=obj.email,
        )
    print "%s Users migrated" % count


def create_riskindications():
    count = 0
    objs = StoffeRiskindication.objects.using('legacy').all()
    print "Found %s Risks, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.riskindication_id
        trans = get_translations(StoffeRiskTranslation, oid)
        if trans != {}:
            RiskIndication.objects.create(
                id=oid,
                name=trans.itervalues().next(),
                name_en=trans['en-en'].name,
                name_de=trans['de-de'].name,
                name_nl=trans['nl-be'].name,
            )
    print "%s Risks migrated" % count


def create_wgks():
    count = 0
    objs = StoffeWgk.objects.using('legacy').all()
    print "Found %s WGKs, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.wgk_id
        trans = get_translations(StoffeWgkTranslation, oid)
        WGK.objects.create(
            name=oid,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].name,
            description_de=trans['de-de'].name,
            description_nl=trans['nl-be'].name,
        )
    print "%s WGKs migrated" % count


def create_storage_classes():
    count = 0
    objs = StoffeStorageclass.objects.using('legacy').all()
    print "Found %s Storage Classes, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.storageclassid
        trans = get_translations(StoffeStorageclassTranslation, oid)
        StorageClass.objects.create(
            id=oid,
            name=obj.classification,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].description,
            description_de=trans['de-de'].description,
            description_nl=trans['nl-be'].description,
        )
    print "%s Storage Classes migrated" % count


def create_seveso_categories():
    count = 0
    objs = StoffeSevesoKategorie.objects.using('legacy').all()
    print "Found %s Seveso Categories, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.seveso_kategorie_id
        trans = get_translations(StoffeSevesoKategorieTranslation, oid)
        SevesoCategory.objects.create(
            name=oid,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].name,
            description_de=trans['de-de'].name,
            description_nl=trans['nl-be'].name,
        )
    print "%s Seveso Categories migrated" % count


def create_hphrases():
    count = 0
    objs = StoffeHphrase.objects.using('legacy').all()
    print "Found %s H-Phrases, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.hphrase_id
        trans = get_translations(StoffeHphraseTranslation, oid)
        HPhrase.objects.create(
            name=oid,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].name,
            description_de=trans['de-de'].name,
            description_nl=trans['nl-be'].name,
            seveso_relevant=obj.seveso_relevant,
        )
    print "%s H-Phrases migrated" % count


def create_pphrases():
    count = 0
    objs = StoffePphrase.objects.using('legacy').all()
    print "Found %s P-Phrases, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.pphrase_id
        trans = get_translations(StoffePphraseTranslation, oid)
        PPhrase.objects.create(
            name=oid,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].name,
            description_de=trans['de-de'].name,
            description_nl=trans['nl-be'].name,
        )
    print "%s P-Phrases migrated" % count


def create_rphrases():
    count = 0
    objs = StoffeRphrase.objects.using('legacy').all()
    print "Found %s R-Phrases, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.rphrase_id
        trans = get_translations(StoffeRphraseTranslation, oid)
        RPhrase.objects.create(
            name=oid,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].name,
            description_de=trans['de-de'].name,
            description_nl=trans['nl-be'].name,
        )
    print "%s R-Phrases migrated" % count


def create_persons():
    count = 0
    objs = StoffePerson.objects.using('legacy').all()
    print "Found %s Persons, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        Person.objects.create(
            id=obj.personid,
            title=obj.anrede,
            academic_title=obj.titel,
            surname=obj.vorname,
            givenname=obj.name,
            phone=obj.tel,
            fax=obj.fax,
            email=obj.mail
        )
    print "%s Persons migrated" % count


##############################################################################
# Create methods contacts
##############################################################################
def create_contacts():
    count = 0
    objs = StoffeContact.objects.using('legacy').all()
    print "Found %s Contacts, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        if obj.contact_id % 100 == 0:
            print "Processing Contact above %s" % obj.contact_id
        address = make_address(obj.address, obj.street, obj.number, obj.plz,
                               obj.city)
        new_obj = Contact.objects.create(
            id=obj.contact_id,
            name=obj.name,
            address=address,
            country=obj.country,
            phone=obj.telefon,
            fax=obj.fax,
            email=obj.mail,
            web=obj.www,
            producer=obj.typ,
            info=obj.contactinfo,
        )
        scps = StoffeContactPerson.objects.using('legacy').filter(
            contact=obj.contact_id)
        for p in scps:
            person = Person.objects.get(id=p.personid.personid)
            role = StoffePerson.objects.using('legacy').get(
                personid=p.personid.personid).roule
            if role == 'Chemical':
                role = 'c'
            else:
                role = 'r'
            Role.objects.create(
                person=person,
                contact=new_obj,
                role=role
            )
    print "%s Contacts migrated" % count


def create_plants():
    count = 0
    print "Processing plants"
    objs = StoffeMenufacturing.objects.using('legacy').all()
    print "Found %s Plants, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.menufacturing_id
        trans = get_translations(StoffeMenuTranslation, oid)
        Plant.objects.create(
            name=trans.itervalues().next(),
            name_en=trans['en-en'].name,
            name_de=trans['de-de'].name,
            name_nl=trans['nl-be'].name,
        )
    print "%s Plants migrated" % count


def create_departments():
    count = 0
    print "Processing departments"
    objs = StoffeDepartment.objects.using('legacy').all()
    print "Found %s Departments, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.menufacturing_id
        trans = get_translations(StoffeMenuTranslation, oid)
        plant = Plant.objects.get(name=trans.itervalues().next().name)
        Department.objects.create(
            id=obj.department_id,
            name=obj.name,
            plant=plant
        )
    print "%s Departments migrated" % count


def create_locations():
    count = 0
    print "Processing locations"
    objs = StoffeLocation.objects.using('legacy').all()
    print "Found %s Locations, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.department_id
        department = Department.objects.get(id=oid)
        Location.objects.create(
            id=obj.location_id,
            name=obj.name,
            department=department
        )
    print "%s Locations migrated" % count


def create_stocks():
    count = 0
    print "Processing stocks"
    objs = StoffeStock.objects.using('legacy').all()
    print "Found %s Stocks, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        oid = obj.location_id
        if oid % 100 == 0:
            print "Processing Contact above %s" % oid
        location = Location.objects.get(id=oid)
        chemical = Chemical.objects.get(id=obj.chemical_id)
        Stock.objects.create(
            chemical=chemical,
            location=location,
            max_volume=obj.volumestock,
            max_unit=make_unit(obj.unitstock),
            year_volume=obj.volumeyear,
            year_unit=make_unit(obj.unityear)
        )
    print "%s Stocks migrated" % count


def create_suppliers():
    count = 0
    print "Processing suppliers"
    objs = StoffeChemDepContact.objects.using('legacy').all()
    print "Found %s Suppliers, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        if count % 100 == 0:
            print "    ...%s Suppliers have been processed" % count
        chemical = Chemical.objects.get(id=obj.chemical.chemical_id)
        contact = Contact.objects.get(id=obj.contact.contact_id)
        department = Department.objects.get(id=obj.department.department_id)
        Supplier.objects.create(
            chemical=chemical,
            contact=contact,
            department=department
        )
    print "%s Suppliers migrated" % count


def create_producers():
    count = 0
    print "Processing producesr"
    objs = StoffeChemContact.objects.using('legacy').all()
    print "Found %s Producers, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        chemical = Chemical.objects.get(id=obj.chemical.chemical_id)
        contact = Contact.objects.get(id=obj.contact.contact_id)
        chemical.producer.add(contact)
        chemical.save()
    print "%s Producers migrated" % count


##############################################################################
# Create methods chemicals
##############################################################################
def create_simple_relations(oid, chemical):
    ####################
    # Storage Class
    count = 0
    objs = StoffeChemStorageclass.objects.using('legacy').filter(chemical=oid)
    for obj in objs:
        count += 1
        chemical.storage_classes.add(
            StorageClass.objects.get(id=obj.storageclassid.storageclassid)
        )
    ####################
    # Seveso Categorie
    count = 0
    objs = StoffeChemSevesoKategorie.objects.using('legacy').filter(
        chemical=oid)
    for obj in objs:
        count += 1
        chemical.seveso_categories.add(
            SevesoCategory.objects.get(name=obj.seveso_kategorie)
        )
    ####################
    # R-Phrase
    count = 0
    objs = StoffeChemRphrase.objects.using('legacy').filter(chemical=oid)
    for obj in objs:
        count += 1
        chemical.rphrases.add(
            RPhrase.objects.get(name=obj.rphrase)
        )
    ####################
    # P-Phrase
    count = 0
    objs = StoffeChemPphrase.objects.using('legacy').filter(chemical=oid)
    for obj in objs:
        count += 1
        chemical.pphrases.add(
            PPhrase.objects.get(name=obj.pphrase)
        )
    ####################


def create_complex_relations(oid, chemical):
    ####################
    # Risk
    count = 0
    objs = StoffeChemRisk.objects.using('legacy').filter(
        chemical=oid, countrycode='en-en')
    for obj in objs:
        count += 1
        roid = obj.riskindication.riskindication_id
        ri = RiskIndication.objects.get(id=roid)
        robj = Risk.objects.create(
            chemical=chemical, riskindication=ri, info=obj.info)
        try:
            robj.info_de = StoffeChemRisk.objects.using('legacy').get(
                chemical=oid, countrycode='de-de', riskindication=roid).info
            robj.info_nl = StoffeChemRisk.objects.using('legacy').get(
                chemical=oid, countrycode='be-be', riskindication=roid).info
        except:
            pass
        chemical.risk_set.add(robj)
    ####################
    # H-Phrase
    count = 0
    objs = StoffeChemHphrase.objects.using('legacy').filter(
        chemical=oid, countrycode='en-en')
    for obj in objs:
        count += 1
        roid = obj.hphrase
        hphrase = HPhrase.objects.get(name=roid)
        robj = HPhraseRelation.objects.create(
            chemical=chemical, hphrase=hphrase, info=obj.info)
        try:
            robj.info_de = StoffeChemHphrase.objects.using('legacy').get(
                chemical=oid, countrycode='de-de', hphrase=roid).info
            robj.info_nl = StoffeChemHphrase.objects.using('legacy').get(
                chemical=oid, countrycode='be-be', hphrase=roid).info
        except:
            pass
        chemical.hphraserelation_set.add(robj)
    ####################


def create_chemicals(chemical):
    oid = chemical.chemical_id
    trans = get_translations(StoffeChemTranslation, oid)
    first_trans = trans.itervalues().next()
    if first_trans.name == '':
        first_trans.name == "<N/A>"
    # Create chemical
    if oid % 100 == 0:
        print "    ...processing Chemical above %s" % oid
    new_chemical = Chemical.objects.create(
        id=oid,
        name=first_trans.name,
        name_en=trans['en-en'].name,
        name_de=trans['de-de'].name,
        name_nl=trans['nl-be'].name,
        comment=first_trans.comment,
        comment_en=trans['en-en'].comment,
        comment_de=trans['de-de'].comment,
        comment_nl=trans['nl-be'].comment,
        article=chemical.article,
        registration_number=chemical.regno,
        cas=chemical.cas_no,
        einecs=chemical.einecs,
        cmr=chemical.cmr,
        needed=chemical.needed,
        preparation=chemical.preparation,
        archive=chemical.archive,
        instruction=chemical.instruction,
        hazardous=chemical.stoerfallstoff,
        reach_vo=chemical.reach_vo,
        components_registered=chemical.regkomponents,
        # FK to another chemical, currently there are three occurences,
        # where this field is filled. Will be migrated manually!
        replaced=None,

        # Many to many relations to contact model
        #producer=chemical.,
        #departments=chemical.,  # relation through Supplier
        #pictograms=chemical.,   # relation through Signal
        #locations=chemical.,    # relation through Stock
    )
    # Create Many to many relations
    create_simple_relations(oid, new_chemical)
    create_complex_relations(oid, new_chemical)

    # Create Many to one relations
    try:
        obj = StoffeChemWgk.objects.using('legacy').get(chemical=oid)
        new_chemical.wgk = WGK.objects.get(name=obj.wgk)
    except:
        pass
    try:
        obj = StoffeReachInfo.objects.using('legacy').get(chemical=oid)
        trans = get_translations(StoffeReachInfoTranslation, obj.reach_infoid)
        new_chemical.reachinformation_set.create(
            chemical=oid,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].information,
            description_de=trans['de-de'].information,
            description_nl=trans['nl-be'].information,
        )
    except:
        pass
    try:
        obj = StoffeSevesoInfo.objects.using('legacy').get(chemical=oid)
        trans = get_translations(StoffeSevesoInfoTranslation,
                                 obj.seveso_infoid)
        new_chemical.sevesoinformation_set.create(
            chemical=oid,
            description=trans.itervalues().next(),
            description_en=trans['en-en'].information,
            description_de=trans['de-de'].information,
            description_nl=trans['nl-be'].information,
        )
    except:
        pass
    # Save the newly created chemical
    new_chemical.save()


##############################################################################
# Create methods media objects
##############################################################################
def create_pictograms():
    count = 0
    print "Processing Pictograms"
    objs = StoffePictogramm.objects.using('legacy').all()
    print "Found %s Pictograms, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        trans = get_translations(StoffePictoTranslation, obj.pictogramm_id)
        new_pic = Pictogram.objects.create(
            code=obj.kodierung,
            name=trans.itervalues().next(),
            name_en=trans['en-en'].bezeichnung,
            name_de=trans['de-de'].bezeichnung,
            name_nl=trans['nl-be'].bezeichnung,
            image=get_file_handle(obj.path),
        )
        print "Pic created: %s" % new_pic.name
        signals = StoffeChemPictogramm.objects.using('legacy').filter(
            pictogramm=obj.pictogramm_id)
        for s in signals:
            chemical = Chemical.objects.get(id=s.chemical.chemical_id)
            Signal.objects.create(
                chemical=chemical,
                pictogram=new_pic,
                term=get_term(s.signal),
            )
    print "%s Pictograms migrated" % count


def create_document():
    count = 0
    print "Processing Documents"
    objs = StoffeDocument.objects.using('legacy').all()
    print "Found %s Documents, processing migration..." % objs.count()
    for obj in objs:
        count += 1
        trans = get_translations(
            StoffeMenuTranslation, obj.menufacturing.menufacturing_id)
        plant = Plant.objects.get(name=trans.itervalues().next().name)
        Document.objects.create(
            plant=plant,
            chemical=Chemical.objects.get(id=obj.chemical.chemical_id),
            file=get_file_handle(obj.path),
            doctype=obj.doctype,
            created=obj.createddate,
        )
    print "%s Documents migrated" % count


def create_reach_document():
    count = 0
    print "Processing REACH Documents"
    objs = StoffeReachDocument.objects.using('legacy').all()
    print "Found %s REACH Documents, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        ReachDocument.objects.create(
            chemical=Chemical.objects.get(id=obj.chemical.chemical_id),
            file=get_file_handle(obj.reachdoc_path),
            country_code=get_language(obj.countrycode),
            created=obj.createddate,
        )
    print "%s REACH Documents migrated" % count


def create_seveso_document():
    count = 0
    print "Processing Seveso Documents"
    objs = StoffeSevesoDocument.objects.using('legacy').all()
    print "Found %s Seveso Documents, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        SevesoDocument.objects.create(
            chemical=Chemical.objects.get(id=obj.chemical.chemical_id),
            file=get_file_handle(obj.doc_path),
            country_code=get_language(obj.countrycode),
            created=obj.createddate,
        )
    print "%s Seveso Documents migrated" % count


def create_sdb():
    count = 0
    print "Processing SDS"
    objs = StoffeSafetydatasheet.objects.using('legacy').all()
    print "Found %s SDS, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        if count % 500 == 0:
            print "    ...%s SDS have been processed" % count
        SafetyDataSheet.objects.create(
            supplier=Contact.objects.get(id=obj.supplier.contact_id),
            chemical=Chemical.objects.get(id=obj.chemical.chemical_id),
            file=get_file_handle(obj.path),
            instruction=obj.instruction or False,
            issue_date=obj.issuedate,
            country_code=get_language(obj.countrycode),
            created=obj.createddate,
        )
    print "%s SDS migrated" % count


def create_esdb():
    count = 0
    print "Processing eSDS"
    objs = StoffeEsafetydatasheet.objects.using('legacy').all()
    print "Found %s eSDS, processing migrattion..." % objs.count()
    for obj in objs:
        count += 1
        ExtendedSafetyDataSheet.objects.create(
            supplier=Contact.objects.get(id=obj.supplier.contact_id),
            chemical=Chemical.objects.get(id=obj.chemical.chemical_id),
            file=get_file_handle(obj.path),
            instruction=obj.instruction or False,
            issue_date=obj.issuedate,
            country_code=get_language(obj.countrycode),
            created=obj.createddate,
        )
    print "%s eSDS migrated" % count


def create_tox():
    count = 0
    print "Processing Toxdata"
    objs = StoffeToxdata.objects.using('legacy').all()
    print "Found %s Toxdata items, processing migration..." % objs.count()
    for obj in objs:
        count += 1
        Toxdata.objects.create(
            supplier=Contact.objects.get(id=obj.supplier_id),
            chemical=Chemical.objects.get(id=obj.chemical_id),
            tox=obj.toxdata,
            oekotox=obj.oekotoxdata,
        )
    print "%s Toxddata items migrated" % count


##############################################################################
# Main method
##############################################################################
def run():
    # Independent Tables
    create_users()
    create_riskindications()
    create_wgks()
    create_storage_classes()
    create_seveso_categories()
    create_rphrases()
    create_pphrases()
    create_hphrases()
    create_persons()
    create_plants()

    # Tables, that have relations to others
    count = 0
    chemicals = StoffeChemical.objects.using('legacy').all()
    print "Found %s Chemicals, processing migrattion..." % chemicals.count()
    for chemical in chemicals:
        count += 1
        create_chemicals(chemical)
    print "%s Chemicals migrated" % count
    create_contacts()
    create_departments()
    create_locations()
    create_stocks()
    create_suppliers()
    create_producers()

    # Tables that contain media files
    create_pictograms()
    create_document()
    create_reach_document()
    create_seveso_document()
    create_sdb()
    create_esdb()
    create_tox()

    # We are done!
    print "All objecst migrated - please do not forget to manually " \
          "migrate the chemicals that have been replaced!"
