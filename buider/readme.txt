docker build -t micropython-esp32-builder:1.0 .

docker run -ti --rm -v ~/Projects/esp32/src/micropython-1.17:/micropython \
    micropython-esp32-builder:1.0 \
    bash -c -l "cd micropython && \
        make -C mpy-cross && \
        make -C ports/esp32 submodules && \
        make -C ports/esp32 BOARD=GENERIC_C3"
