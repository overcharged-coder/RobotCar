from gpiozero import Motor
import sys
import tty
import termios

front_left = Motor(forward=27, backward=17)
front_right = Motor(forward=23, backward=24)
rear_left = Motor(forward=6, backward=5)
rear_right = Motor(forward=16, backward=20)

SPEED = 1.0

def stop():
    front_left.stop()
    front_right.stop()
    rear_left.stop()
    rear_right.stop()

def forward():
    front_left.forward(SPEED)
    front_right.forward(SPEED)
    rear_left.forward(SPEED)
    rear_right.forward(SPEED)

def backward():
    front_left.backward(SPEED)
    front_right.backward(SPEED)
    rear_left.backward(SPEED)
    rear_right.backward(SPEED)

def left():
    front_left.backward(SPEED)
    rear_left.backward(SPEED)
    front_right.forward(SPEED)
    rear_right.forward(SPEED)

def right():
    front_left.forward(SPEED)
    rear_left.forward(SPEED)
    front_right.backward(SPEED)
    rear_right.backward(SPEED)

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setcbreak(fd)

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
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
