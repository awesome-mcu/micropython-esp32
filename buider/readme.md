# ESP-IDF Release and SoC Compatibility


The following table shows ESP-IDF support of Espressif SoCs where ![alt text][preview] and ![alt text][supported] denote preview status and support, respectively. In preview status the build is not yet enabled and some crucial parts could be missing (like documentation, datasheet). Please use an ESP-IDF release where the desired SoC is already supported.

|Chip         |         v3.3           |          v4.0          |           v4.1         |          v4.2          |         v4.3           |          v4.4          |                                                            |
|:----------- |:---------------------: | :---------------------:| :---------------------:| :---------------------:| :---------------------:| :---------------------:|:---------------------------------------------------------- |
|ESP32        | ![alt text][supported] | ![alt text][supported] | ![alt text][supported] | ![alt text][supported] | ![alt text][supported] | ![alt text][supported] |                                                            |
|ESP32-S2     |                        |                        |                        | ![alt text][supported] | ![alt text][supported] | ![alt text][supported] |                                                            |
|ESP32-C3     |                        |                        |                        |                        | ![alt text][supported] | ![alt text][supported] |                                                            |
|ESP32-S3     |                        |                        |                        |                        | ![alt text][preview]   | ![alt text][supported] | [Announcement](https://www.espressif.com/en/news/ESP32_S3) |
|ESP32-H2     |                        |                        |                        |                        |                        | ![alt text][preview]   | [Announcement](https://www.espressif.com/en/news/ESP32_H2) |

[supported]: https://img.shields.io/badge/-supported-green "supported"
[preview]: https://img.shields.io/badge/-preview-orange "preview"


# Usage

```
// Build ESP-IDF 4.3.1 Image
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
