from gpiozero import OutputDevice, DigitalInputDevice
from time import sleep, perf_counter

lt = OutputDevice(25)
le = DigitalInputDevice(13)

ct = OutputDevice(12)
ce = DigitalInputDevice(19)

rt = OutputDevice(26)
re = DigitalInputDevice(21)

def distance(trig, echo):
    trig.off()
    sleep(0.000002)

    trig.on()
    sleep(0.00001)
    trig.off()

    timeout = perf_counter() + 0.03

    while not echo.value:
        if perf_counter() >= timeout:
            return None

    start = perf_counter()
    timeout = start + 0.03

    while echo.value:
        if perf_counter() >= timeout:
            return None

    return (perf_counter() - start) * 34300 / 2

try:
    while True:
        left = distance(lt, le)
        sleep(0.05)

        center = distance(ct, ce)
        sleep(0.05)

        right = distance(rt, re)
        sleep(0.05)

        l = f"{left:.1f} cm" if left is not None else "NO ECHO"
        c = f"{center:.1f} cm" if center is not None else "NO ECHO"
        r = f"{right:.1f} cm" if right is not None else "NO ECHO"

        print(
            f"\rLEFT: {l:<12} | CENTER: {c:<12} | RIGHT: {r:<12}",
            end="",
            flush=True
        )

except KeyboardInterrupt:
    print("\nStopped.")
