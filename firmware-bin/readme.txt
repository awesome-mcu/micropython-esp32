# Example for esp32s2
esptool.py --chip esp32-S2 \
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
