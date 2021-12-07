FROM ubuntu:20.04

LABEL Name=esp32-micropython-builder Version=1.0
# SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV ESPIDF=/esp-idf
ENV MICROPYTHON=/micropython
ENV PORT=/dev/ttyESP

RUN apt-get update -y && \
    apt-get install -y git wget flex bison gperf python3-dev python3-pip python3-pyparsing python3-serial python3-cryptography python3-future cmake ninja-build ccache libffi-dev libssl-dev dfu-util && \
    rm -rf /var/lib/apt/lists/*
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
ENV PYTHON2=python

RUN git clone https://github.com/espressif/esp-idf.git ${ESPIDF} && \
    cd ${ESPIDF} && \
    git submodule update --init --recursive && \
    bash install.sh && \
    source export.sh

WORKDIR /
