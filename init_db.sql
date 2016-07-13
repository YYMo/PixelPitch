drop database if exists pixelpitchdb;
create database pixelpitchdb;
create user pixelpitchdb_user with password 'QWER1234zxcv';
alter role pixelpitchdb_user set client_encoding to 'utf8';
alter role pixelpitchdb_user set default_transaction to 'read commit';
grant all privileges on databas pixelpitchdb to pixelpitchdb_user;

