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

## 4 - Checking the Wiring

Before installing the batteries, check all of the wiring carefully.

### 4.1 - Checking for Shorts

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

### 4.2 - Checking the Grounds

Check continuity between:

```text
Pi pin 6  <-> DRV1 GND
Pi pin 34 <-> DRV2 GND
```

Both connections should have continuity.

### 4.3 - Final Wiring Check

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

## 5 - Testing the Motors

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

## 8 - Final Checks

Before regularly driving the car, make sure:

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

The robot car is now ready to drive!
