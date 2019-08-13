#!/bin/bash

if test -z "$DEVPOD_NAME"
then
    echo "This is not a devpod"
else
    PGPASSWORD=test psql --host dev-db.jx-develop -U test -c "DROP DATABASE \"$HOSTNAME-{{ project_name }}\""
    PGPASSWORD=test psql --host dev-db.jx-develop -U test -c "CREATE DATABASE \"$HOSTNAME-{{ project_name }}\""
fi
