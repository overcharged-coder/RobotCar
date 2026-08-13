from gpiozero import Motor
import sys
import tty
import termios

fl = Motor(forward=27, backward=17)
fr = Motor(forward=23, backward=24)
rl = Motor(forward=6, backward=5)
rr = Motor(forward=16, backward=20)

def stop():
    fl.stop()
    fr.stop()
    rl.stop()
    rr.stop()

def forward():
    fl.forward(1.0)
    fr.forward(1.0)
    rl.forward(1.0)
    rr.backward(1.0)

def backward():
    fl.backward(1.0)
    fr.backward(1.0)
    rl.backward(1.0)
    rr.forward(1.0)

def left():
    fl.backward(1.0)
    rl.backward(1.0)
    fr.forward(1.0)
    rr.backward(1.0)

def right():
    fl.forward(1.0)
    rl.forward(1.0)
    fr.backward(1.0)
    rr.forward(1.0)

fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)

try:
    tty.setcbreak(fd)

    print("W = forward")
    print("S = backward")
    print("A = left")
    print("D = right")
    print("SPACE = stop")
    print("Q = quit")

    while True:
        key = sys.stdin.read(1).lower()

        if key == "w":
            forward()
        elif key == "s":
            backward()
        elif key == "a":
            left()
        elif key == "d":
            right()
        elif key == " ":
            stop()
        elif key == "q":
            break

finally:
    stop()
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
