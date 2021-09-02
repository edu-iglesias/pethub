#### Create database and Owner #####

psql -U postgres << END_OF_SCRIPT

DROP DATABASE IF EXISTS pethub_db; -- drop the DB
DROP ROLE IF EXISTS pethub_role;
CREATE ROLE pethub_role CREATEDB CREATEROLE LOGIN PASSWORD 'pethub_role';
ALTER USER pethub_role CREATEDB;
CREATE DATABASE pethub_db WITH OWNER = pethub_role CONNECTION LIMIT = -1;

END_OF_SCRIPT