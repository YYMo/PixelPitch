#!/bin/bash
# need to set a password for user postgres first:
# http://serverfault.com/questions/110154/whats-the-default-superuser-username-password-for-postgres-after-a-new-install
# have to change the peer mode in postgres:
# http://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge
psql -U postgres -f script/init_db.sql
