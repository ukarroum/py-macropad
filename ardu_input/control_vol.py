import serial
import alsaaudio
from pymouse import PyMouse

ser = serial.Serial('/dev/ttyUSB1')

m = alsaaudio.Mixer()
m.setmute(False)
vol = m.getvolume()[0]

mouse = PyMouse()

def update_vol(new_vol):
    global vol
    if abs(new_vol - vol) > 1:
        m.setvolume(int(new_vol))
        vol = new_vol


def update_pos(x, y):
    mouse.move(mouse.position()[0] - int(y/70), mouse.position()[1] + int(x/70))


def click():

    mouse.click(mouse.position()[0], mouse.position()[1])


while True:
    line = ser.readline()

    try:
        match line.decode().split():
            case ['VOL', new_vol]:
                update_vol(new_vol)
            case ['JOYSTICK', x, y]:
                update_pos(int(x) - 520, int(y) - 520)
            case ['CLICK']:
                click()

    except UnicodeDecodeError:
        pass
