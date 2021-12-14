
# Usage

```
// Build ESP-IDF Image
$ docker build -t builder-esp-idf:v4.3.1 --build-arg IDF_VERSION=v4.3.1 .

// Build ESP32S2 Micropython Flash
$ git clone -b v1.17 git@github.com:micropython/micropython.git
$ docker run -ti --rm -v /data/src/micropython:/root/esp/micropython builder-esp-idf:v4.3.1 \
      bash -c -l "cd micropython && \
      . ~/esp/esp-idf/export.sh && \
      make -C mpy-cross && \
      make -C ports/esp32 submodules && \
      make -C ports/esp32 BOARD=GENERIC_S2"
```
