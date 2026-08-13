from gpiozero import Motor, OutputDevice, DigitalInputDevice
from time import sleep, perf_counter
import sys, tty, termios, select

# Motors
fl = Motor(forward=27, backward=17)
fr = Motor(forward=23, backward=24)
rl = Motor(forward=6, backward=5)
rr = Motor(forward=16, backward=20)

# Ultrasonic sensors
lt, le = OutputDevice(25), DigitalInputDevice(13)
ct, ce = OutputDevice(12), DigitalInputDevice(19)
rt, re = OutputDevice(26), DigitalInputDevice(21)

# Speeds
DRIVE_SPEED = 0.85
REVERSE_SPEED = 0.60

# Actual chassis clearances
FRONT_STOP = 22.0
SIDE_STOP = 7.0

# Sensor positions
FRONT_OFFSET = 3.0
SIDE_OFFSET = 1.8

# Maneuver timing
REVERSE_TIME = 0.25
FRONT_TURN_TIME = 0.85
SIDE_TURN_TIME = 0.50

# Manual override
MANUAL_TIMEOUT = 1.0

# Ultrasonic
ECHO_TIMEOUT = 0.010
MAX_DISTANCE = 170.0
SENSOR_GAP = 0.025


def stop():
    fl.stop()
    fr.stop()
    rl.stop()
    rr.stop()


def forward(speed=DRIVE_SPEED):
    fl.forward(speed)
    fr.forward(speed)
    rl.forward(speed)
    rr.backward(speed)


def backward(speed=REVERSE_SPEED):
    fl.backward(speed)
    fr.backward(speed)
    rl.backward(speed)
    rr.forward(speed)


def turn_left():
    fl.backward(1.0)
    rl.backward(1.0)
    fr.forward(1.0)
    rr.backward(1.0)


def turn_right():
    fl.forward(1.0)
    rl.forward(1.0)
    fr.backward(1.0)
    rr.forward(1.0)


def get_key():
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    return sys.stdin.read(1).lower() if ready else None


def distance(trig, echo, offset):
    trig.off()
    sleep(0.000002)

    trig.on()
    sleep(0.00001)
    trig.off()

    timeout = perf_counter() + ECHO_TIMEOUT

    while not echo.value:
        if perf_counter() >= timeout:
            return MAX_DISTANCE

    start = perf_counter()
    timeout = start + ECHO_TIMEOUT

    while echo.value:
        if perf_counter() >= timeout:
            return MAX_DISTANCE

    d = (perf_counter() - start) * 34300 / 2
    return max(0, min(d, MAX_DISTANCE) - offset)


fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)

left = center = right = MAX_DISTANCE

sensor = 0
next_sensor = 0

last_manual = -100
manual_command = ""

auto_action = "drive"
action_end = 0
turn_direction = None

last_display = 0

try:
    tty.setcbreak(fd)

    print("AUTO + RC")
    print("W/A/S/D = manual | SPACE = stop | Q = quit")
    print("Auto resumes after 1 second.\n")

    while True:
        now = perf_counter()

        # Manual control
        key = get_key()

        if key == "q":
            break

        if key in ("w", "a", "s", "d", " "):
            last_manual = now
            auto_action = "drive"

            if key == "w":
                forward(1.0)
                manual_command = "FORWARD"

            elif key == "s":
                backward(1.0)
                manual_command = "BACKWARD"

            elif key == "a":
                turn_left()
                manual_command = "LEFT"

            elif key == "d":
                turn_right()
                manual_command = "RIGHT"

            else:
                stop()
                manual_command = "STOP"

        # Read one sensor at a time
        if now >= next_sensor:

            if sensor == 0:
                left = distance(lt, le, SIDE_OFFSET)

            elif sensor == 1:
                center = distance(ct, ce, FRONT_OFFSET)

            else:
                right = distance(rt, re, SIDE_OFFSET)

            sensor = (sensor + 1) % 3
            next_sensor = perf_counter() + SENSOR_GAP

        manual_active = perf_counter() - last_manual < MANUAL_TIMEOUT
        now = perf_counter()

        # Autonomous control
        if not manual_active:

            if auto_action == "drive":

                if center <= FRONT_STOP:
                    stop()
                    backward()
                    auto_action = "reverse"
                    action_end = now + REVERSE_TIME

                elif left <= SIDE_STOP:
                    turn_right()
                    auto_action = "side_turn"
                    action_end = now + SIDE_TURN_TIME

                elif right <= SIDE_STOP:
                    turn_left()
                    auto_action = "side_turn"
                    action_end = now + SIDE_TURN_TIME

                else:
                    forward()

            elif auto_action == "reverse":

                backward()

                if now >= action_end:
                    stop()

                    if left > right:
                        turn_direction = "left"
                        turn_left()
                    else:
                        turn_direction = "right"
                        turn_right()

                    auto_action = "front_turn"
                    action_end = now + FRONT_TURN_TIME

            elif auto_action == "front_turn":

                if turn_direction == "left":
                    turn_left()
                else:
                    turn_right()

                if now >= action_end:
                    stop()
                    auto_action = "drive"

            elif auto_action == "side_turn":

                if now >= action_end:
                    stop()
                    auto_action = "drive"

        # Display
        if now - last_display >= 0.10:

            if manual_active:
                status = f"MANUAL {manual_command:<8}"
            else:
                status = f"AUTO {auto_action:<10}"

            print(
                f"\r{status} | "
                f"L {left:5.1f} cm | "
                f"F {center:5.1f} cm | "
                f"R {right:5.1f} cm     ",
                end="",
                flush=True
            )

            last_display = now

        sleep(0.001)

except KeyboardInterrupt:
    pass

finally:
    stop()
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    print("\nStopped.")
