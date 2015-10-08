# Drive simulator

This project simulates a electric motor drive and the data that could be received/delivered from such device. It has custom messages developed for a electronic fishing boat. The simulators simulate the behavior that the real drive should use.

It is intended to be used with either a serial port or a physical CAN Bus. See above for usage.

The project is at a prototyping state, not intended to be used in production environnement, this tool is intended as an instructional tool on how to use CAN bus on python based code.

## Creator

We are a group of student from [Sherbrooke's university](http://usherbrooke.ca) that tries to do a prototype of a 100% electronic fishing boat. To learn more about us, [visit our website](http://bateaunautilus.ca/).

## Dependencies

* It uses the [python-can](http://python-can.readthedocs.org/en/latest/) library to facilitate CAN Messaging.
* python 3.3
* It uses a float16 representation python implementation taken from the  [David E. Jones website](http://davidejones.com/blog/1413-python-precision-floating-point/)

## Useful commands

Starting the simulator

    sudo python3 main.py

Using the unit tests

    python3 -m unittest

A virtual can bus can be used under linux for testing the application without connecting to a hardware can bus.

    sudo modprobe vcan
    sudo ip link add dev vcan0 type vcan
    sudo ifconfig vcan0 up

## Possible improvements

* Add variation in data (ex:rpm=[4500,5000,5500]).
* Add a state machine for the internal state of the drive and kill-switch (On, Off).
* Receive RPM command and use results.

## License

The project is licensed under the [the MIT License](license.md).

## Support

We don't provide any support for this tool, Open issues for question. We are open to pull-request if you find some improvement that could be made to the tool.

# References / Links
 * Sample Messages can be inspired from NMEA2000, see [CANBOAT PNGs references](https://github.com/canboat/canboat/blob/master/analyzer/pgns.json), there is also information in the [.h file](https://github.com/canboat/canboat/blob/master/analyzer/pgn.h)
 * [python-can](http://python-can.readthedocs.org/en/latest/) Library
 * [can-open object dictionnary](http://www.can-cia.org/index.php?id=506)
