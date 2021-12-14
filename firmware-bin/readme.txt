# Example for esp32s2
esptool.py --chip esp32s2 \
    --port /dev/cu.wchusbserial1420 \
    -b 460800 \
    --before default_reset \
    --after hard_reset \
    write_flash \
    --flash_mode dio \
    --flash_size detect \
    --flash_freq 80m \
    0x0 bootloader.bin \
    0x8000 partition-table.bin \
    0x10000 micropython.bin


# Example for esp32c3(esp32-c3-mini-1)
esptool.py --chip esp32-c2 \
    --port /dev/cu.wchusbserial1420 \
    -b 460800 \
    --before default_reset \
    --after hard_reset \
    write_flash \
    --flash_mode dio \
    --flash_size detect \
    --flash_freq 80m \
    0x1000 bootloader.bin \
    0x8000 partition-table.bin \
    0x10000 micropython.bin


# Example for esp32(esp-12k)
# firmware bin download:
# https://micropython.org/download/esp32/
esptool.py -p  /dev/cu.SLAB_USBtoUART flash_id
esptool.py --chip esp32 -p /dev/cu.SLAB_USBtoUART erase_flash
esptool.py --chip esp32 \
    -p /dev/cu.SLAB_USBtoUART \
    --baud 460800 write_flash \
    -z 0x1000 esp32-20210902-v1.17.bin
