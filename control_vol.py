import serial
import alsaaudio

ser = serial.Serial('/dev/ttyUSB0')

m = alsaaudio.Mixer()
m.setmute(False)
vol = m.getvolume()[0]

while True:
    print(m.getvolume())
    line = ser.readline()

    try:
        new_vol = (int(line.decode().strip()) / 1024) * 100
        if abs(new_vol - vol) > 1:
            m.setvolume(int(new_vol))
            vol = new_vol

    except UnicodeDecodeError:
        pass
