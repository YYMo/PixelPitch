drop database if exists pixelpitchdb;
drop role if exists pixelpitchdb_user;
create database pixelpitchdb;
create user pixelpitchdb_user with password 'QWER1234zxcv';
alter role pixelpitchdb_user set client_encoding to 'utf8';
grant all privileges on database pixelpitchdb to pixelpitchdb_user;

