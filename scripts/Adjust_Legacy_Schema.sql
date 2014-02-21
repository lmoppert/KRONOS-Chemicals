###############################################################################
# This script adds id columns to all tables, that hava a complex primary key.
#
# The following tables are ommitted, as they have a valid primary key that
# can be used in the model definition.
#
# KRONOS_CheckList
# KRONOS_CheckList_Anwendung
# KRONOS_CheckList_Information
# KRONOS_CheckList_Kapitel
# KRONOS_CheckList_KapitelText
# KRONOS_CheckList_PSA
# KRONOS_CheckList_PSA_Artikel
# KRONOS_CheckList_PSA_Img
# KRONOS_CheckList_Status
# Stoff_Historie
# reach_Chem_Data
# reach_Statement
# reach_Status1
# stoffe_Chemical
# stoffe_Contact
# stoffe_Department
# stoffe_Document
# stoffe_eSafetyDataSheet
# stoffe_Group
# stoffe_Location
# stoffe_Menufacturing
# stoffe_Person
# stoffe_Pictogramm
# stoffe_Reach_Document
# stoffe_Reach_Info
# stoffe_Riskindication
# stoffe_SafetyDataSheet
# stoffe_Seveso_Document
# stoffe_Seveso_Info
# stoffe_SevesoProductList
# stoffe_Stock
# stoffe_StorageClass
# stoffe_Synonym
#
###############################################################################
# For the translation tables the combined pk is copied to the id field and
# that is defined as the primary_key in the model definition
#
ALTER TABLE `Substance_Portal`.`KRONOS_CheckList_Kapitel_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`KRONOS_CheckList_Kapitel_Translation` SET `id` = concat(`KapitelID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`KRONOS_CheckList_Masnahme_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`KRONOS_CheckList_Masnahme_Translation` SET `id` = concat(`MasnahmeID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`KRONOS_CheckList_PSA_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`KRONOS_CheckList_PSA_Translation` SET `id` = concat(`PSA_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Chem_Translation` SET `id` = concat(`chemical_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Group_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Group_Translation` SET `id` = concat(`group_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_HPhrase_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_HPhrase_Translation` SET `id` = concat(`hphrase_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Menu_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Menu_Translation` SET `id` = concat(`menufacturing_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Picto_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Picto_Translation` SET `id` = concat(`pictogramm_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_PPhrase_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_PPhrase_Translation` SET `id` = concat(`pphrase_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_proc_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_proc_Translation` SET `id` = concat(`proc_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Reach_Info_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Reach_Info_Translation` SET `id` = concat(`Reach_InfoID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Risk_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Risk_Translation` SET `id` = concat(`riskindication_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_RPhrase_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_RPhrase_Translation` SET `id` = concat(`rphrase_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Seveso_Info_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Seveso_Info_Translation` SET `id` = concat(`Seveso_InfoID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Seveso_Kategorie_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Seveso_Kategorie_Translation` SET `id` = concat(`Seveso_Kategorie_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_Signal_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_Signal_Translation` SET `id` = concat(`Signal_ID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_StorageClass_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_StorageClass_Translation` SET `id` = concat(`storageclassID`, `CountryCode`);
ALTER TABLE `Substance_Portal`.`stoffe_WGK_Translation` ADD COLUMN `id` VARCHAR(45) NOT NULL FIRST;
UPDATE `Substance_Portal`.`stoffe_WGK_Translation` SET `id` = concat(`WGK_ID`, `CountryCode`);
#
###############################################################################
# All other tables get a simple autoincrement id column
#
ALTER TABLE `Substance_Portal`.`KRONOS_Check_Anwendung` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_HPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_KapitelText` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_Masnahme` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_Parameter` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_Pictogramm` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_PPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_PSA_Artikel` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_PSA_Img` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_StorageClass` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_Check_WGK` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`KRONOS_CheckList_Masnahme` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`Stoff_Tables` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`reach_Chem_Contact` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_CAS` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Contact` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Dep` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Dep_Contact` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Group` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_HPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Pictogramm` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_PPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_proc` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_risk` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_RPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Seveso_Kategorie` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_StorageClass` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_Synonym` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Chem_WGK` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Contact_Person` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_HPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_PPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_proc` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Risk_RPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_RPhrase` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_Seveso_Kategorie` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_ToxData` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
ALTER TABLE `Substance_Portal`.`stoffe_WGK` ADD COLUMN `id` INT(11) NOT NULL AUTO_INCREMENT FIRST, ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC);
#
###############################################################################
# For missing translations migration we need a dummy table
#
CREATE TABLE `Substance_Portal`.`Dummy_Translation` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `comment` VARCHAR(800) NULL,
  `information` LONGTEXT NULL,
  `kapitel` LONGTEXT NULL,
  `masnahme` LONGTEXT NULL,
  `psa_0` LONGTEXT NULL,
  `bezeichnung` VARCHAR(400) NULL,
  `description` LONGTEXT NULL,
  `signal` VARCHAR(100) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));
