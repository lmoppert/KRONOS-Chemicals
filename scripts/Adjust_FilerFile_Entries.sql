UPDATE `she`.`filer_file` SET `owner_id` = 1, `name` = LEFT(`original_filename`, CHAR_LENGTH(`original_filename`)-4) WHERE `id` > 100;
SELECT * FROM she.filer_file;
