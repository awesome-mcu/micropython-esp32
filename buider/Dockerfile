# ESP32 Micropython Builder
#
# Build Esp-idf Image:
# $ docker build -t builder-esp-idf:v4.3.1 --build-arg IDF_VERSION=v4.3.1 .
#
# Build Esp32s2 Micropython Flash:
# $ git clone -b v1.17 https://github.com/micropython/micropython.git
# $ docker run -ti --rm -v micropython:/root/esp/micropython builder-esp-idf:v4.3.1 \
#       bash -c -l ". esp-idf/export.sh && \
#       cd micropython && \
#       make -C mpy-cross && \
#       make -C ports/esp32 submodules && \
#       make -C ports/esp32 BOARD=GENERIC_S2"
#
# notes:
#   * git cdn for mainland china:
#       - github.com.cnpmjs.org
#   * git clone submodules:
#       - git submodule update --init --recursive
#


FROM ubuntu:20.04

LABEL Name=esp32-micropython-builder Version=1.0
SHELL ["/bin/bash", "-c"]

ARG IDF_VERSION=v4.3.1
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en'
ENV DEBIAN_FRONTEND=noninteractive
ENV ESP_HOME="/root/esp"

RUN apt-get update -y && \
    apt-get install -y git wget flex bison gperf python3 python3-dev python3-pip ccache cmake ninja-build libffi-dev libssl-dev dfu-util libusb-1.0-0 && \
    rm -rf /var/lib/apt/lists/*
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
ENV PYTHON2=python

WORKDIR ${ESP_HOME}
RUN git clone -b ${IDF_VERSION} --recursive https://github.com/espressif/esp-idf.git && \
    cd ${ESP_HOME}/esp-idf && \
    ./install.sh && \
    . export.sh && \
    echo "alias get_idf='. $HOME/esp/esp-idf/export.sh'" >> .bashrc
