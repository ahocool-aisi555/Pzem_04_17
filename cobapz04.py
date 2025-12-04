# PZEM 04 reader
# by nyoman yudi kurniawan
# Silahkan install library minimalmodbus dan pyserial di environment python kamu
# Sesuaikan Com Port yang muncul di PC
# script ini hanya membaca sekali, sesuaikan dengan bantuan AI jika untuk IOT

import minimalmodbus
import serial

# Konfigurasi PZEM-04
instrument = minimalmodbus.Instrument('COM7', 1)  # port (diubah sesuai com pc kamu), slave address 
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1
instrument.mode = minimalmodbus.MODE_RTU

# Non-verbose untuk menghindari error log berlebihan
instrument.debug = False

try:
    # Membaca register sesuai PZEM-04 Modbus map
    voltage = instrument.read_register(0x0000, functioncode=4)/10
    current = instrument.read_register(0x0001,functioncode=4)/1000
    power = instrument.read_register(0x0003, functioncode=4)/10       
    energy = instrument.read_long(0x0004, functioncode=4)/1000 
    frek = instrument.read_register(0x0007, functioncode=4)/10 
    pf = instrument.read_register(0x0008, functioncode=4)/100     

    print(f"Tegangan (V): {voltage}")
    print(f"Arus (A): {current}")
    print(f"Daya (W): {power}")
    print(f"Energi (kWh): {energy}")
    print(f"Frekuensi (hz): {frek}")
    print(f"Power Factor : {pf}")

except Exception as e:
    print("Gagal membaca PZEM-04:", e)