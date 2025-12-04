# PZEM 17 reader
# by nyoman yudi kurniawan
# Silahkan install library minimalmodbus dan pyserial di environment python kamu
# Sesuaikan Com Port yang muncul di PC
# script ini hanya membaca sekali, sesuaikan dengan bantuan AI jika untuk IOT

import minimalmodbus
import serial

# Konfigurasi PZEM-017
instrument = minimalmodbus.Instrument('COM32', 1)  # port (diubah sesuai com pc kamu), slave address
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1
instrument.mode = minimalmodbus.MODE_RTU

# Non-verbose untuk menghindari error log berlebihan
instrument.debug = False

try:
    # Membaca register sesuai PZEM-017 Modbus map
    voltage = instrument.read_register(0x0000, functioncode=4)/100
    current = instrument.read_register(0x0001,functioncode=4)/100
    power = instrument.read_register(0x0002, functioncode=4)/10       
    energy = instrument.read_long(0x0004, functioncode=4)/1000  

    print(f"Tegangan (V): {voltage}")
    print(f"Arus (A): {current}")
    print(f"Daya (W): {power}")
    print(f"Energi (kWh): {energy}")

except Exception as e:
    print("Gagal membaca PZEM-017:", e)