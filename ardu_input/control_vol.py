import serial
import alsaaudio

ser = serial.Serial('/dev/ttyUSB1')

m = alsaaudio.Mixer()
m.setmute(False)
vol = m.getvolume()[0]


def update_vol(new_vol):
    global vol
    if abs(new_vol - vol) > 1:
        m.setvolume(int(new_vol))
        vol = new_vol


while True:
    line = ser.readline()

    try:
        match line.decode().split():
            case ['VOL', new_vol]:
                update_vol(new_vol)

    except UnicodeDecodeError:
        pass
