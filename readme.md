# PythonEV3

Control a Lego EV3 motors via Python CLI.

This was a project I began in my Sophomore year in High School, and never got around to finishing. I found the HEX values in some lego document, that I can not locate (I am writing this over 2 years after I actually started this)

Essentially, when ever you run a file similar to test.py, the EV3 moves around by listening to the HEX codes that sent to it over a Bluetooth Serial Port.

I wanted to build a tool for more advanced students in a robotics class that I was teaching. It does work, I think one student actually tried to use this, I set up the CLI, and he just played around with the commands.

Only the commands move_time and motor_stop work.

```
move_time(ports='cb', power=75, time=5)
stop_motor = motor_stop(ports='abcd')
```

* Ports must be set to characters between 'a' and 'd' (you can combine them like 'ab')
* Power is the % output of the motor, it is an integer between -100 and 100
* Time is the duration that the action will happen, it is an float greater than 0
