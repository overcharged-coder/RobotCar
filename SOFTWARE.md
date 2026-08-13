# Software and Code

> Software and code you need to put onto your Raspberry Pi. Make sure you have the Raspberry Pi 4B, Raspberry Pi power bank, and microSD card with its adapter. All required parts are listed [here](./PARTS.md).

## 1 - Setting Up the Raspberry Pi

1. Download the Raspberry Pi Imager [here](https://www.raspberrypi.com/software/).
2. Insert the microSD card into its adapter and plug the adapter into your computer.
3. Open Raspberry Pi Imager and follow the setup steps.
4. Make sure you:
   * Select the correct microSD card.
   * Set a device name.
   * Set a username and password.
   * Configure your Wi-Fi connection.
   * Enable SSH.
5. Write Raspberry Pi OS to the microSD card.
6. When the process finishes, remove the microSD card from the adapter.
7. Insert the microSD card into the Raspberry Pi.
8. Connect the Raspberry Pi power supply.
9. Wait for the Raspberry Pi to finish starting up.

## 2 - Connecting Through SSH

1. Open Command Prompt on your computer.
2. Run:

   ```bash
   ssh [User Name]@[Device Name].local
   ```

3. Replace `[User Name]` and `[Device Name]` with the username and device name you chose in Raspberry Pi Imager.

   For example:

   ```bash
   ssh om@robotcar.local
   ```

4. If you are asked whether you want to continue connecting, type:

   ```text
   yes
   ```

5. Enter the password you created in Raspberry Pi Imager.

You should now be connected to the Raspberry Pi through SSH.

## 3 - Installing the Required Software

Run:

```bash
sudo apt update
sudo apt install python3-gpiozero
```

The other Python modules used by the programs are included with Python and do not need to be installed separately.

## 4 - Adding the Programs

This project uses four Python programs:

```text
motor_test.py
drive.py
ultrasonic_test.py
autonomous.py
```

`motor_test.py` and `ultrasonic_test.py` are optional testing programs. They are useful for checking the hardware if something is not working correctly.

`drive.py` provides manual RC control.

`autonomous.py` allows the car to drive autonomously while still allowing manual control at any time.

### 4.1 - motor_test.py - Optional

Create the file:

```bash
nano motor_test.py
```

Copy the code from [motor_test.py](./motor_test.py) and paste it into nano by right-clicking.

Press:

```text
Ctrl+X
Y
Enter
```

Run it with:

```bash
python3 motor_test.py
```

This program tests each of the four motors individually in both directions.

### 4.2 - drive.py

Create the file:

```bash
nano drive.py
```

Copy the code from [drive.py](./drive.py) and paste it into nano by right-clicking.

Press:

```text
Ctrl+X
Y
Enter
```

Run it with:

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

### 4.3 - ultrasonic_test.py - Optional

Create the file:

```bash
nano ultrasonic_test.py
```

Copy the code from [ultrasonic_test.py](./ultrasonic_test.py) and paste it into nano by right-clicking.

Press:

```text
Ctrl+X
Y
Enter
```

Run it with:

```bash
python3 ultrasonic_test.py
```

The program continuously displays the distance measured by the left, center, and right HC-SR04 sensors.

Move your hand in front of each sensor individually and make sure the corresponding distance changes.

Press:

```text
Ctrl+C
```

to stop the program.

## 5 - Autonomous Driving

Create the autonomous program:

```bash
nano autonomous.py
```

Copy the code from [autonomous.py](./autonomous.py) and paste it into nano by right-clicking.

Press:

```text
Ctrl+X
Y
Enter
```

Run it with:

```bash
python3 autonomous.py
```

The car will begin driving autonomously.

The three HC-SR04 sensors are used to detect obstacles:

```text
Left sensor    Detects obstacles on the left
Center sensor  Detects obstacles in front
Right sensor   Detects obstacles on the right
```

When the center sensor detects an obstacle, the car:

1. Stops.
2. Reverses briefly.
3. Compares the left and right sensor distances.
4. Turns toward the side with more space.
5. Continues driving.

If one of the side sensors detects an obstacle that is too close, the car turns away from that side.

You can manually control the car at any time using:

```text
W       Forward
S       Backward
A       Turn left
D       Turn right
SPACE   Stop
Q       Quit
```

Manual input temporarily overrides autonomous driving.

After one second without manual input, the car automatically returns to autonomous driving.

The terminal also continuously displays the current sensor distances:

```text
L = Left
F = Front
R = Right
```

## 6 - Adjusting the Autonomous Program

Different cars and driving surfaces may require slightly different settings.

The main values that can be adjusted near the beginning of `autonomous.py` are:

```python
DRIVE_SPEED = 0.85
REVERSE_SPEED = 0.60

FRONT_STOP = 22.0
SIDE_STOP = 7.0

REVERSE_TIME = 0.25
FRONT_TURN_TIME = 0.85
SIDE_TURN_TIME = 0.50
```

`DRIVE_SPEED` controls normal autonomous driving speed.

`REVERSE_SPEED` controls how fast the car reverses while avoiding an obstacle.

`FRONT_STOP` controls how close an obstacle can be in front of the chassis before the car reacts.

`SIDE_STOP` controls how close an obstacle can be to either side before the car turns away.

`REVERSE_TIME` controls how long the car reverses before turning.

`FRONT_TURN_TIME` controls how long the car turns after detecting an obstacle in front.

`SIDE_TURN_TIME` controls how long the car turns away from a side obstacle.

Increase a turn time if the car does not turn far enough. Decrease it if the car turns too far.
