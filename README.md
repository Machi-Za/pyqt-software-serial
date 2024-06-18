# python-software-serial

A GUI program using PyQt5 to perform serial communication between the GUI and a microcontroller. Serial communication allows for writing to or reading from the microcontroller.

### Installation

The establishment is exceptionally straightforward you fair ought to have PyQt5 and pyserial introduced which can be introduced with this command:

```Bash
pip install pyserial
pip install PyQt5
pip install PyQt5-Qt5
pip install PyQt5Designer
```

### Usage

After that fair duplicate the library to your venture and grant the record a title (e.g. 'IO.py').

```Python
# Initialize the Port object from the IO module
import IO
Port = IO.Ports()

# to send a message through the serial port
if Port.serial.is_open:
    Port.Write(message)

Port.ReadExisting.connect(main.DataReceived)    # to handle data received from the serial port

Port.BaudRate   # to update the list of baud rates
port.portName()   # to update the list of available ports

```

For a more complete usage example, refer to 'main.py'.
To run the above source code, follow these steps:

1. Upload the program located at 'arduino/softwareserial/softwareserial.ino' to the microcontroller.
2. Next, run program.py.
3. Select the port and baud rate.
4. Once selected, press the connect button.
5. The application should now be operational.