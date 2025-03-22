from subprocess import Popen

import serial
import alsaaudio

ser = serial.Serial('/dev/ttyUSB0')

m = alsaaudio.Mixer()
m.setmute(False)
vol = m.getvolume()[0]


def update_vol(new_vol: int):
    global vol
    if abs(new_vol - vol) > 1:
        m.setvolume(int((new_vol / 1024) * 100))
        vol = new_vol


while True:
    line = ser.readline()

    try:
        match line.decode().split():
            case ['VOL', new_vol]:
                update_vol(int(new_vol))
            case ['BTN']:
                Popen(["ghostty"])

    except UnicodeDecodeError:
        pass
