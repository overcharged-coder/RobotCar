# Software and Code

> Software and code you need to put into your Raspberry Pi

1. Download the Raspberry Pi Imager [here](https://www.raspberrypi.com/software/)
2. Insert the microSD card into the adapter and plug it into the laptop
3. Run the Imager and follow the steps given, make sure to use the microSD's drive, enable SSH and Internet!
4. Take the microSD out of the adapter and plug it into the Raspberry Pi
5. Plug in the Raspberry Pi Power Supply, then wait for the green dot to blink occasionally
6. Go to your Command Prompt, and run `ssh [Device Name]@[User Name].local`. Replace `[Device Name]` and `[User Name]` with the device name and user name you set up in the Imager
7. Enter the password, which you set up in the Imager
8. Run `nano car.py` in the terminal, copy the code from [this file](./car.py) and paste it into nano via right click
