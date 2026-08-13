# Building Steps

> Follow these steps to build the robot car. Before starting, make sure you have all the required [parts](./PARTS.md) and have completed the [software setup](./SOFTWARE.md).

## 1 - Attaching Everything to the Chassis

### 1.1 - Motors

1. Take one motor and one wheel.
2. Align the motor's D-shaped shaft with the wheel's D-shaped slot.
3. Press the wheel firmly onto the shaft until it fits snugly.
4. Repeat steps 1-3 for the other three motors and wheels.
5. Position one motor at each corner of the chassis:

   * Front left
   * Front right
   * Rear left
   * Rear right
6. Make sure all four wheels are aligned and can rotate without rubbing against the chassis.
7. Hot glue each motor securely to the chassis.

### 1.2 - Battery Holders

1. Take one battery holder.
2. Position it in the center-left area of the chassis with its wires facing forward.
3. Mark the two outer mounting holes at the bottom of the holder.
4. Drill through the chassis at the marked locations.
5. Fit M3 screws through the holes and secure the battery holder.
6. Take the second battery holder.
7. Position it in the center-right area of the chassis with its wires facing backward.
8. Mark the two outer mounting holes at the bottom.
9. Drill through the chassis at the marked locations.
10. Fit M3 screws through the holes and secure the battery holder.

### 1.3 - Breadboards

1. Take one breadboard.
2. Peel off the protective backing from the adhesive underneath it.
3. Place it horizontally above the battery holders.
4. Align the center of the breadboard with the gap between the two battery holders.
5. Press it firmly onto the chassis.
6. Take the second breadboard.
7. Peel off its protective backing.
8. Place it horizontally below the battery holders.
9. Align its center with the gap between the two battery holders.
10. Press it firmly onto the chassis.

### 1.4 - Raspberry Pi

1. Take the Raspberry Pi.
2. Position it at the rear center of the chassis.
3. Make sure the power, USB, Ethernet, and GPIO connections remain accessible.
4. Mark the Raspberry Pi's mounting holes on the chassis.
5. Drill the marked holes.
6. Fit M2.5 screws through the mounting holes and secure the Raspberry Pi.


### 1.5 - HC-SR04 Ultrasonic Sensors

The car uses three HC-SR04 ultrasonic distance sensors:

```text
Left sensor   -> Points directly left
Center sensor -> Points directly forward
Right sensor  -> Points directly right
```

For this setup you will need:

* Three HC-SR04 ultrasonic sensors
* Three 1 kΩ resistors
* Three 2 kΩ resistors
* Female-to-male and female-to-female DuPont wires
* Electrical tape for the two side sensors

#### 1.5.1 - Center Sensor

The center HC-SR04 is mounted directly in the front breadboard.

1. Locate rows 17-20 on the `A-E` side of the front breadboard.
2. Hold the HC-SR04 so its two round ultrasonic transducers point straight toward the front of the car.
3. Check the labels printed next to the sensor pins. For the standard `VCC`, `TRIG`, `ECHO`, `GND` order used in this build, insert the pins as follows:

```text
A17 -> VCC
A18 -> TRIG
A19 -> ECHO
A20 -> GND
```

4. Press the sensor in firmly without bending the header pins.
5. Make sure the sensor points straight forward and does not touch the wheels or other components.

> Always verify the labels on your own HC-SR04 before applying power. If its pin order differs, follow the labels printed on the sensor rather than the row order above.

#### 1.5.2 - Left Sensor

The left HC-SR04 is mounted directly to the left side of the chassis rather than plugged into a breadboard.

1. Position the sensor so the two round ultrasonic transducers point directly to the left of the car.
2. Keep the sensor level and clear of the left wheels.
3. Secure the sensor to the chassis with electrical tape.
4. Place the tape over the back or edges of the sensor board. Do not cover either ultrasonic transducer or the four-pin header.
5. Leave enough of the four header pins exposed for the DuPont wires.

#### 1.5.3 - Right Sensor

Mount the right HC-SR04 the same way on the opposite side.

1. Position the sensor so the ultrasonic transducers point directly to the right.
2. Keep it level and clear of the right wheels.
3. Secure it firmly with electrical tape without covering the ultrasonic transducers or header pins.

In this build, the face of the center sensor is approximately 30 mm behind the front edge of the chassis, and the faces of the side sensors are approximately 18 mm inward from the corresponding side edges. These offsets can later be accounted for in the autonomous-driving software when calculating clearance from the chassis itself.

## 2 - Preparing the Wires

### 2.1 - Preparing the Motor Wires

You will need four red and four black motor wires with male DuPont connectors on one end.

1. Take one loose red wire.
2. Strip about 2 mm of insulation from one end.
3. Take a male DuPont wire.
4. Cut it about 2-3 inches from the male connector.
5. Strip about 2 mm of insulation from the cut end.
6. Twist the exposed ends of the two wires together.
7. Solder the connection.
8. Cover the solder joint with heat-shrink tubing or electrical tape.
9. Repeat this process until you have four red wires and four black wires.

You should now have eight motor wires, each with a male DuPont connector on one end and a loose wire end on the other.

### 2.2 - Preparing the Battery Wires

Each battery holder needs a male DuPont connector on both its positive and negative wires.

1. Select one battery holder.
2. Strip about 2 mm of insulation from the end of its red wire.
3. Strip about 2 mm of insulation from the end of its black wire.
4. Take a male DuPont wire.
5. Cut it about 2-3 inches from the male connector.
6. Strip about 2 mm of insulation from the cut end.
7. Twist the exposed end together with the battery holder's red wire.
8. Solder the connection.
9. Insulate the joint with heat-shrink tubing or electrical tape.
10. Repeat the process with another DuPont wire and the battery holder's black wire.
11. Repeat steps 2-10 for the second battery holder.

All four battery wires should now end in male DuPont connectors.

> Do not install batteries in the holders while preparing or wiring the car.

## 3 - Wiring

> Keep the Raspberry Pi powered off and both battery holders empty while completing this section.

### 3.1 - Motor Wires

1. Take one prepared red wire and one prepared black wire.
2. Solder them to the two terminals of the front-left motor.
3. Take another red and black wire and solder them to the front-right motor.
4. Repeat the process for the rear-left motor.
5. Repeat the process for the rear-right motor.
6. Insulate any exposed solder joints with heat-shrink tubing or electrical tape.

The order of the red and black wires on each motor does not matter because the motor direction can be configured later in software.

### 3.2 - Installing the DRV8833 Motor Drivers

You will use two DRV8833 motor driver modules:

```text
DRV1 -> Front two motors
DRV2 -> Rear two motors
```

#### 3.2.1 - DRV8833 Pin Layout

The DRV8833 modules used in this build have the following layout:

```text
EEP   OUT1   OUT2   OUT3   OUT4   ULT
IN4   IN3    GND    VCC    IN2    IN1
```

The two motor output pairs are:

```text
OUT1 + OUT2 -> Motor 1
OUT3 + OUT4 -> Motor 2
```

Do not connect a motor between `OUT2` and `OUT3`.

#### 3.2.2 - Installing DRV1

1. Take one DRV8833.
2. Place it across the center gap of the front breadboard.
3. Make sure each row of DRV pins is on a different side of the breadboard's center gap.
4. Press the module firmly into the breadboard.
5. Make sure none of the pins are accidentally offset by one breadboard row.

> Check the labels printed on the DRV8833 itself rather than relying only on breadboard row numbers.

#### 3.2.3 - Installing DRV2

1. Take the second DRV8833.
2. Place it across the center gap of the rear breadboard.
3. Press it firmly into place.
4. Double-check that every pin is in the intended breadboard row.

Leave `EEP` and `ULT` disconnected.

### 3.3 - Connecting the Motors

#### 3.3.1 - Front Motors

DRV1 controls the two front motors.

```text
Front Left Motor  -> DRV1 OUT1 + OUT2
Front Right Motor -> DRV1 OUT3 + OUT4
```

1. Connect the two front-left motor DuPont wires to the breadboard rows containing `DRV1 OUT1` and `DRV1 OUT2`.
2. Connect the two front-right motor wires to the rows containing `DRV1 OUT3` and `DRV1 OUT4`.

#### 3.3.2 - Rear Motors

DRV2 controls the two rear motors.

```text
Rear Left Motor  -> DRV2 OUT1 + OUT2
Rear Right Motor -> DRV2 OUT3 + OUT4
```

1. Connect the rear-left motor wires to `DRV2 OUT1` and `DRV2 OUT2`.
2. Connect the rear-right motor wires to `DRV2 OUT3` and `DRV2 OUT4`.

### 3.4 - Connecting DRV1 to the Raspberry Pi

Connect DRV1 using the Raspberry Pi's physical pin numbers.

| DRV1 Pin |     Raspberry Pi Pin |
| -------- | -------------------: |
| IN1      |                   11 |
| IN2      |                   13 |
| IN3      |                   16 |
| IN4      |                   15 |
| GND      |                    6 |
| VCC      | Do not connect to Pi |

```text
DRV1 IN1 -> Pi pin 11
DRV1 IN2 -> Pi pin 13
DRV1 IN3 -> Pi pin 16
DRV1 IN4 -> Pi pin 15
DRV1 GND -> Pi pin 6
```

Do not connect `DRV1 VCC` to the Raspberry Pi.

### 3.5 - Connecting DRV2 to the Raspberry Pi

Connect DRV2 using the following physical pin numbers.

| DRV2 Pin |     Raspberry Pi Pin |
| -------- | -------------------: |
| IN1      |                   29 |
| IN2      |                   31 |
| IN3      |                   36 |
| IN4      |                   38 |
| GND      |                   34 |
| VCC      | Do not connect to Pi |

```text
DRV2 IN1 -> Pi pin 29
DRV2 IN2 -> Pi pin 31
DRV2 IN3 -> Pi pin 36
DRV2 IN4 -> Pi pin 38
DRV2 GND -> Pi pin 34
```

Do not connect `DRV2 VCC` to the Raspberry Pi.

### 3.6 - Connecting the Batteries

Each DRV8833 is powered by its own 6 V battery pack.

#### 3.6.1 - DRV1 Battery

```text
Battery 1 positive (+) -> DRV1 VCC
Battery 1 negative (-) -> DRV1 GND
Pi pin 6               -> DRV1 GND
```

Both the battery negative wire and the Raspberry Pi ground wire connect to `DRV1 GND`.

#### 3.6.2 - DRV2 Battery

```text
Battery 2 positive (+) -> DRV2 VCC
Battery 2 negative (-) -> DRV2 GND
Pi pin 34              -> DRV2 GND
```

Both the battery negative wire and the Raspberry Pi ground wire connect to `DRV2 GND`.

> Never connect the positive side of either 6 V motor battery directly to the Raspberry Pi.


### 3.7 - Connecting the HC-SR04 Ultrasonic Sensors

The Raspberry Pi GPIO pins operate at 3.3 V, but a standard HC-SR04 `ECHO` output is approximately 5 V. **Never connect an HC-SR04 ECHO pin directly to a Raspberry Pi GPIO pin.** Each sensor needs its own 1 kΩ / 2 kΩ voltage divider on the ECHO line.

#### 3.7.1 - Powering the Sensor Rails

Use the power rails on the front breadboard for all three HC-SR04 sensors.

```text
Pi physical pin 2  (5V)  -> Front breadboard + rail
Pi physical pin 14 (GND) -> Front breadboard - rail
```

If the breadboard power rails are split into two electrically separate sections, bridge the matching sections with jumper wires.

> These are the **sensor power rails**. Do not connect either 6 V motor-battery positive wire to the sensor + rail. Leave the existing DRV8833 battery wiring unchanged.

All three HC-SR04 sensors may share this 5 V rail and GND rail.

#### 3.7.2 - Center Sensor Wiring

The center sensor is already plugged into the front breadboard at rows 17-20:

```text
A17 -> VCC
A18 -> TRIG
A19 -> ECHO
A20 -> GND
```

Connect it as follows:

1. Connect `B17` to the front breadboard `+` rail. This powers the center sensor from 5 V.
2. Connect `B18` to Raspberry Pi physical pin `32` (`GPIO12`). This is the center `TRIG` signal.
3. Connect `B20` to the front breadboard `-` rail. This is the center sensor ground.
4. Put a 1 kΩ resistor from `B19` to `B21`.
5. Connect `C21` to Raspberry Pi physical pin `35` (`GPIO19`).
6. Put a 2 kΩ resistor from `D21` to the front breadboard `-` rail.

The center ECHO path is therefore:

```text
Center ECHO -> 1 kΩ -> junction -> Pi pin 35
                           |
                          2 kΩ
                           |
                          GND
```

#### 3.7.3 - Left Sensor Wiring

The left HC-SR04 remains mounted on the side of the chassis. Attach DuPont wires directly to its four male header pins.

1. Connect left `VCC` to the front breadboard `+` rail.
2. Connect left `GND` to the front breadboard `-` rail.
3. Connect left `TRIG` directly to Raspberry Pi physical pin `22` (`GPIO25`).
4. Connect left `ECHO` to breadboard hole `J24`.
5. Put a 1 kΩ resistor from `I24` to `I26`.
6. Connect `H26` to Raspberry Pi physical pin `33` (`GPIO13`).
7. Put a 2 kΩ resistor from `G26` to the front breadboard `-` rail.

The left ECHO path is:

```text
Left ECHO -> J24 -> 1 kΩ -> row 26 junction -> Pi pin 33
                                      |
                                     2 kΩ
                                      |
                                     GND
```

#### 3.7.4 - Right Sensor Wiring

Attach DuPont wires directly to the four male header pins on the right HC-SR04.

1. Connect right `VCC` to the front breadboard `+` rail.
2. Connect right `GND` to the front breadboard `-` rail.
3. Connect right `TRIG` directly to Raspberry Pi physical pin `37` (`GPIO26`).
4. Connect right `ECHO` to breadboard hole `J30`.
5. Put a 1 kΩ resistor from `I30` to `I32`.
6. Connect `H32` to Raspberry Pi physical pin `40` (`GPIO21`).
7. Put a 2 kΩ resistor from `G32` to the front breadboard `-` rail.

The right ECHO path is:

```text
Right ECHO -> J30 -> 1 kΩ -> row 32 junction -> Pi pin 40
                                       |
                                      2 kΩ
                                       |
                                      GND
```

#### 3.7.5 - Ultrasonic GPIO Summary

| Sensor | Signal | Raspberry Pi Physical Pin | BCM GPIO |
| ------ | ------ | -------------------------: | -------: |
| Left   | TRIG   |                         22 |       25 |
| Left   | ECHO   |                         33 |       13 |
| Center | TRIG   |                         32 |       12 |
| Center | ECHO   |                         35 |       19 |
| Right  | TRIG   |                         37 |       26 |
| Right  | ECHO   |                         40 |       21 |

The Raspberry Pi physical pins used for sensor power are:

```text
Pin 2  -> 5V sensor rail
Pin 14 -> Sensor GND rail
```

> Remember that the `TRIG` lines may connect directly to the Raspberry Pi, but every `ECHO` line must pass through its own 1 kΩ / 2 kΩ voltage divider first.

## 4 - Checking the Wiring (Optional)

> **Optional:** You may skip this entire checking section and continue to the hardware-testing steps. However, these checks are strongly recommended, especially before powering the car for the first time, because they can help catch wiring mistakes or shorts before they damage a component.

If you choose to perform the checks, keep the Raspberry Pi powered off and both battery holders empty while working through this section.

### 4.1 - Checking for Shorts (Optional)

1. Make sure the Raspberry Pi is powered off.
2. Remove the batteries from both battery holders.
3. Set a multimeter to continuity mode.
4. Check each input pin against GND on DRV1:

```text
IN1 <-> GND
IN2 <-> GND
IN3 <-> GND
IN4 <-> GND
```

5. Repeat the same checks on DRV2.

None of the input pins should produce a near-zero-resistance continuous beep to GND.

6. Check `VCC` against `GND` on each motor driver.

There should not be a direct short between `VCC` and `GND`.

### 4.2 - Checking the Grounds (Optional)

Check continuity between:

```text
Pi pin 6  <-> DRV1 GND
Pi pin 34 <-> DRV2 GND
```

Both connections should have continuity.

### 4.3 - Final Wiring Check (Optional)

Before applying power, verify every connection one more time.

```text
DRV1

IN1 -> Pi pin 11
IN2 -> Pi pin 13
IN3 -> Pi pin 16
IN4 -> Pi pin 15
GND -> Pi pin 6 + Battery 1 negative
VCC -> Battery 1 positive


DRV2

IN1 -> Pi pin 29
IN2 -> Pi pin 31
IN3 -> Pi pin 36
IN4 -> Pi pin 38
GND -> Pi pin 34 + Battery 2 negative
VCC -> Battery 2 positive
```


### 4.4 - Checking the Ultrasonic Sensor Wiring (Optional)

Before powering the sensors, verify the following:

```text
Sensor + rail -> Pi pin 2 (5V)
Sensor - rail -> Pi pin 14 (GND)

Left TRIG   -> Pi pin 22
Left ECHO   -> 1 kΩ / 2 kΩ divider -> Pi pin 33

Center TRIG -> Pi pin 32
Center ECHO -> 1 kΩ / 2 kΩ divider -> Pi pin 35

Right TRIG  -> Pi pin 37
Right ECHO  -> 1 kΩ / 2 kΩ divider -> Pi pin 40
```

Check that:

1. Each HC-SR04 `VCC` connects to the 5 V sensor rail.
2. Each HC-SR04 `GND` connects to the sensor ground rail.
3. Each sensor has its own separate ECHO voltage divider.
4. The Pi GPIO wire is connected to the junction between the 1 kΩ and 2 kΩ resistors, not directly to the HC-SR04 ECHO pin.
5. No 6 V motor-battery positive wire is connected to the sensor power rail.
6. The left and right sensor wires are secured so they cannot reach the wheels.
7. Electrical tape does not cover either ultrasonic transducer.

## 5 - Testing the Hardware

Before placing the car on the ground, lift the chassis so that all four wheels can rotate freely.

### 5.1 - Powering the Car for the First Time

1. Check all wiring one final time.
2. Make sure no exposed wires are touching each other.
3. Install the batteries in both battery holders.
4. Power on the Raspberry Pi.
5. Wait a few seconds before running any motor code.
6. Immediately disconnect power if:

   * A motor starts unexpectedly
   * The Raspberry Pi becomes unusually hot
   * A DRV8833 becomes extremely hot
   * You smell burning
   * You see smoke

### 5.2 - Individual Motor Test

Test each motor individually in both directions before trying to drive all four at once.

```text
DRV1 OUT1/OUT2 -> Front Left
DRV1 OUT3/OUT4 -> Front Right

DRV2 OUT1/OUT2 -> Rear Left
DRV2 OUT3/OUT4 -> Rear Right
```

Each motor should:

1. Rotate in one direction.
2. Stop.
3. Rotate in the opposite direction.
4. Stop.

If a motor rotates in the wrong physical direction, leave the wiring alone. Its direction can be reversed in the software.


### 5.3 - Ultrasonic Sensor Test

After the motor test succeeds, test all three HC-SR04 sensors before running autonomous-driving software.

Create a file named `ultrasonic_test.py` containing:

```python
from gpiozero import OutputDevice, DigitalInputDevice
from time import sleep, perf_counter

left_trig = OutputDevice(25)
left_echo = DigitalInputDevice(13)
center_trig = OutputDevice(12)
center_echo = DigitalInputDevice(19)
right_trig = OutputDevice(26)
right_echo = DigitalInputDevice(21)


def get_distance(trig, echo):
    trig.off()
    sleep(0.000002)
    trig.on()
    sleep(0.00001)
    trig.off()

    timeout = perf_counter() + 0.03
    while not echo.value:
        if perf_counter() > timeout:
            return None

    start = perf_counter()
    timeout = start + 0.03
    while echo.value:
        if perf_counter() > timeout:
            return None

    return (perf_counter() - start) * 34300 / 2


try:
    while True:
        left = get_distance(left_trig, left_echo)
        sleep(0.06)
        center = get_distance(center_trig, center_echo)
        sleep(0.06)
        right = get_distance(right_trig, right_echo)
        sleep(0.06)

        left_text = f"{left:.1f} cm" if left is not None else "NO ECHO"
        center_text = f"{center:.1f} cm" if center is not None else "NO ECHO"
        right_text = f"{right:.1f} cm" if right is not None else "NO ECHO"

        print(
            f"LEFT: {left_text:>10} | "
            f"CENTER: {center_text:>10} | "
            f"RIGHT: {right_text:>10}"
        )

except KeyboardInterrupt:
    print("\nStopped.")
```

Run it with:

```bash
python3 ultrasonic_test.py
```

Test the sensors one at a time:

1. Move your hand toward and away from the left sensor. The `LEFT` reading should change.
2. Move your hand in front of the center sensor. The `CENTER` reading should change.
3. Move your hand toward and away from the right sensor. The `RIGHT` reading should change.
4. Make sure moving your hand near one sensor does not consistently cause another sensor's reading to change instead.
5. Press `Ctrl+C` to stop the test.

The test code triggers the sensors one at a time with a short delay between them to reduce ultrasonic interference.

> The displayed values are measured from the sensor faces. The autonomous-driving software can subtract approximately 3.0 cm from the center reading and 1.8 cm from each side reading when it needs clearance from the chassis edge instead.

## 6 - Running the RC Program

Follow the instructions in [SOFTWARE.md](./SOFTWARE.md) to install the required software and place the RC program on the Raspberry Pi.

Run the program with:

```bash
python3 drive.py
```

The controls are:

```text
W       Forward
S       Backward
A       Turn left
D       Turn right
SPACE   Stop
Q       Quit
```

### 6.1 - First RC Test

1. Lift the chassis so all four wheels are off the ground.
2. Start the RC program.
3. Press `W`.
4. Confirm all four wheels rotate in the physical forward direction.
5. Press `S`.
6. Confirm all four wheels rotate in the physical backward direction.
7. Press `A`.
8. Confirm the left and right sides rotate in the correct directions to turn left.
9. Press `D`.
10. Confirm the left and right sides rotate in the correct directions to turn right.
11. Press `SPACE` and confirm all four motors stop.
12. Press `Q` to exit the program.

If one or more wheels rotate backward when they should rotate forward, adjust their direction in the software rather than changing the physical wiring.

## 7 - Ground Test

Once the lifted test works correctly:

1. Place the car on a flat, open surface.
2. Make sure there are no obstacles immediately in front of or behind the car.
3. Start the RC program.
4. Briefly drive forward.
5. Confirm the car travels straight.
6. Test backward movement.
7. Test left turns.
8. Test right turns.
9. Use `SPACE` whenever you need to immediately stop the motors.

Because all four wheels are fixed in position, the car uses skid steering. The wheels may need to slide slightly sideways while turning.

## 8 - Final Checks (Optional)

> **Optional:** This final checklist is not required to continue using the robot car. It is provided as a quick way to catch loose connections, mounting problems, or wiring mistakes.

If you choose to do the final check, make sure:

* All four motors are firmly attached to the chassis.
* All four wheels are securely fitted to their shafts.
* The wheels do not rub against the chassis.
* Both battery holders are firmly mounted.
* Both breadboards are firmly attached.
* Both DRV8833 modules are fully seated in their breadboards.
* Neither DRV8833 is offset by one breadboard row.
* Each motor is connected to either `OUT1/OUT2` or `OUT3/OUT4`.
* Battery positive is connected to the appropriate DRV8833 `VCC`.
* Battery negative is connected to the appropriate DRV8833 `GND`.
* Each DRV8833 shares a ground connection with the Raspberry Pi.
* Neither battery's positive wire is connected directly to the Raspberry Pi.
* All DuPont connections are secure.
* All solder joints are insulated.
* No loose wires can become caught in the wheels.
* All four motors work in both directions.
* Forward, backward, left, right, stop, and quit controls work correctly.
* The Raspberry Pi is securely mounted.
* The center HC-SR04 is firmly seated in the front breadboard and points straight forward.
* The left HC-SR04 is securely taped to the left side and points left.
* The right HC-SR04 is securely taped to the right side and points right.
* No electrical tape covers an ultrasonic transducer.
* All three HC-SR04 VCC pins are connected to the 5 V sensor rail.
* All three HC-SR04 GND pins are connected to the sensor GND rail.
* Each HC-SR04 ECHO line passes through its own 1 kΩ / 2 kΩ voltage divider before reaching the Raspberry Pi.
* All three sensors return sensible distance readings in `ultrasonic_test.py`.
* Side-sensor wiring is secured away from the wheels.

The robot car is now ready to drive and sense obstacles!
