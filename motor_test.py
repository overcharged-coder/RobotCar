from gpiozero import Motor
from time import sleep

fl = Motor(forward=27, backward=17)
fr = Motor(forward=23, backward=24)
rl = Motor(forward=6, backward=5)
rr = Motor(forward=16, backward=20)

motors = [
    ("Front Left", fl),
    ("Front Right", fr),
    ("Rear Left", rl),
    ("Rear Right", rr)
]

try:
    for name, motor in motors:
        print(f"{name}: direction 1")
        motor.forward(1.0)
        sleep(1)
        motor.stop()
        sleep(0.5)

        print(f"{name}: direction 2")
        motor.backward(1.0)
        sleep(1)
        motor.stop()
        sleep(0.5)

    print("Motor test complete.")

finally:
    fl.stop()
    fr.stop()
    rl.stop()
    rr.stop()
