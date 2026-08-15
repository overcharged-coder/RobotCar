# 🤖 RobotCar

A Raspberry Pi-powered four-wheel robot car with manual control and autonomous obstacle avoidance.

The car uses two DRV8833 motor drivers, four DC motors, and three ultrasonic sensors to detect obstacles and navigate around them.

## Features

* 🚗 Four-wheel motor control
* 🎮 Keyboard/manual driving
* 📡 Left, center, and right ultrasonic sensors
* 🤖 Autonomous obstacle avoidance
* 🔄 Automatic turning and reversing
* 🕹 Manual override while autonomous mode is running

## Hardware

* Raspberry Pi 4B
* 4 × DC gear motors
* 2 × DRV8833 motor drivers
* 3 × HC-SR04 ultrasonic sensors
* 2 × motor battery packs
* Robot chassis and wheels

See [Parts List](docs/PARTS.md) for the complete parts list.

## Quick Start

Clone the repository:

```bash
git clone https://github.com/overcharged-coder/RobotCar.git
cd RobotCar
```

Install the required Raspberry Pi package:

```bash
sudo apt update
sudo apt install -y python3-gpiozero
```

### Test the Motors

```bash
python3 motor_test.py
```

### Test the Ultrasonic Sensors

```bash
python3 ultrasonic_test.py
```

### Manual Driving

```bash
python3 drive.py
```

Controls:

| Key     | Action  |
| ------- | ------- |
| `W`     | Forward |
| `S`     | Reverse |
| `A`     | Left    |
| `D`     | Right   |
| `SPACE` | Stop    |
| `Q`     | Quit    |

### Autonomous Mode

```bash
python3 autonomous.py
```

The car drives forward while monitoring all three ultrasonic sensors.

If an obstacle is detected, it can:

* Stop
* Reverse
* Compare the available space
* Turn toward the clearer direction
* Continue driving

Manual controls can also temporarily override autonomous mode.

## Documentation

* 📦 [Parts List](docs/PARTS.md)
* 🔧 [Build & Wiring Guide](docs/BUILD.md)
* 💻 [Software Setup](docs/SOFTWARE.md)
* 🔌 [Wiring Diagram](docs/drawings/pi-wiring.png)

## Project Updates

Current development work, planned features, and known issues are tracked here:

* 📋 [RobotCar Project Board](https://github.com/users/overcharged-coder/projects/2)
* 🛠 [Open Issues](https://github.com/overcharged-coder/RobotCar/issues)
* ✅ [Closed Issues](https://github.com/overcharged-coder/RobotCar/issues?q=is%3Aissue%20state%3Aclosed)

The Project Board is the main place to see what is currently being worked on, what is planned next, and what has been completed.


## Future Development

The next stage of RobotCar will add camera-based navigation so the car can identify driveable floor and make smarter navigation decisions instead of relying only on ultrasonic sensors.
