# Start with a base Python 3.10 image from the Debian Buster distribution
FROM python:3.10-buster AS base

# Switch to the root user and set the working directory to /root
USER root
WORKDIR /root

# Install required packages for building and running the software
RUN apt update \
    && apt install -y --no-install-recommends \
        git \
        build-essential \
        libsuitesparse-dev \
        libopenblas-dev \
        libjansson-dev \
        libssl-dev \
        zlib1g-dev \
        libev-dev \
    && rm -rf /var/lib/apt/lists/*

# Run selftest for the Andes package and move the config file to the new user's home directory

# Build DiME 2 and install the Python client library
WORKDIR /tmp

RUN python3 -m pip install kvxopt && \
    git clone -b develop https://github.com/CURENT/andes.git && \ 
    cd andes && \
    python3 -m pip install -e . && \
    cd ../../

# Create a new user named 'cui' and a work directory
RUN useradd -ms /bin/bash cui && \
    mkdir -p /home/cui/work

# RUN python3 -m andes selftest && \
#     mv /root/.andes /home/cui && \
#     chown -R cui:cui /home/cui/.andes

# Run selftest for the Andes package and move the config file to the new user's home directory
RUN mkdir -p /root/.andes && \
    mv /root/.andes /home/cui && \
    chown -R cui:cui /home/cui/.andes && \
    python3 -m andes misc --save-config /home/cui/.andes/andes.rc

RUN git clone -b develop https://github.com/CURENT/ams.git && \ 
    cd ams && \
    python3 -m pip install -e . && \
    cd ../../

RUN git clone -b develop https://github.com/CURENT/agvis.git && \ 
    cd agvis && \
    python3 -m pip install -e . && \
    cd ../../

RUN git clone https://github.com/CURENT/dime.git && \
    cd dime/server && \
    make clean && \
    make && \
    make install && \
    cd ../client/python && \
    python3 -m pip install . && \
    cd ../../ && \
    rm -rf dime \
    && rm -rf /tmp/dime

# Switch to the 'cui' user and set the working directory to the new user's work directory
USER cui
WORKDIR /home/cui/work

# Set the entrypoint and command for the container
ENTRYPOINT []
CMD []
