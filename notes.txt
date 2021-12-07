// prepare tools
pip3 install rshell esptool adafruit-ampy mpfshell
brew install picocom minicom

ls /dev/cu.*
screen /dev/cu.usbserial-0001 115200


// ampy
export AMPY_PORT=/dev/cu.wchusbserial1420
ampy --baud 115200 ls
ampy put main.py
ampy rm main.py


// build micropython for esp32s2
git clone -b v1.17 git@github.com:micropython/micropython.git micropython-1.17

docker run -ti --rm -v ~/Projects/esp32/src/micropython-1.17:/micropython \
    micropython/build-micropython-esp32 \
    bash -c -l "cd micropython && \
        make -C mpy-cross && \
        make -C ports/esp32 submodules && \
        make -C ports/esp32 BOARD=GENERIC_C3"


// 编译后烧录固件
esptool.py --chip esp32-S2 \
    --port /dev/cu.wchusbserial1420 \
    -b 460800 \
    --before default_reset \
    --after hard_reset \
    write_flash \
    --flash_mode dio \
    --flash_size detect \
    --flash_freq 80m \
    0x1000 build-GENERIC_S2/bootloader/bootloader.bin \
    0x8000 build-GENERIC_S2/partition_table/partition-table.bin \
    0x10000 build-GENERIC_S2/micropython.bin


// 查看固件
esptool.py --chip esp32-S2 \
    --port /dev/cu.wchusbserial1420 \
    flash_id

// 擦除固件
esptool.py --chip esp32-S2 \
    --port /dev/cu.wchusbserial1420 \
    erase_flash

// 烧录固件
esptool.py --chip esp32-S2 \
    --port /dev/cu.wchusbserial1420 \
    --baud 460800 \
    write_flash -z 0x1000 \
    esp32s2-firmware.bin



REF:
https://github.com/dhylands/rshell
https://esp32.iotclub.io/flash_firmware
https://blog.csdn.net/qq_34440409/article/details/119175631
https://github.com/micropython/micropython-lib#usage
https://github.com/micropython/micropython-lib/blob/master/python-ecosys/urequests/urequests.py
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/tools/idf-docker-image.html
https://github.com/espressif/crosstool-NG/releases
https://zhuanlan.zhihu.com/p/406128630
https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all
http://www.wch.cn/downloads/CH341SER_LINUX_ZIP.html
http://www.wch.cn/downloads/CH341SER_ZIP.html
https://github.com/espressif/arduino-esp32/issues/1084
https://blog.csdn.net/ami82?t=1
