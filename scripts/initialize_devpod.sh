#!/bin/bash

yum -y install gcc gcc-c++ curl bzip2 postgresql vim \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && /bin/sh /tmp/miniconda.sh -bfp /usr/local/ \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3.7.3 pip

pip install --upgrade pip awscli awscli-local
pip install cython \
    && pip install -r requirements.txt
