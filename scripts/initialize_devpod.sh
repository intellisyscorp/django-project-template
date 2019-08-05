#!/bin/bash

yum -y install gcc gcc-c++ curl bzip2 postgresql vim \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && /bin/sh /tmp/miniconda.sh -bfp /usr/local/ \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3

pip install --upgrade pip awscli awscli-local
pip install cython \
    && pip install -r requirements.txt

ln -s /workspace ~/workspace

echo "export DJANGO_SETTINGS_MODULE={{ project_name }}.settings.base" >> ~/.bashrc 
echo "source ~/.bashrc"

if test -z $DEVPOD_NAME
then
    echo "This is not a devpod"
else
    PGPASSWORD=test psql --host develop-service-db -U test -c "DROP DATABASE \"$HOSTNAME_{{ project_name }}\""
    PGPASSWORD=test psql --host develop-service-db -U test -c "CREATE DATABASE \"$HOSTNAME_{{ project_name }}\""
    python manage.py migrate
fi
