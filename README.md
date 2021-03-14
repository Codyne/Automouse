# Automouse

Records automatically or manually set mouse movements and clicks, then plays them back until the escape key is pressed.

Requires `keyboard` and `mouse` modules which you can get from `pip install`

## Record in Realtime

Select "Record Input" and then perform the actions you wish to automate. When you're done, right click. To play back that action on a loop, select "Playback Input" button beneath the "Record Input" button. Pressing escape will end the loop and finish the last iteration of mouse movement, then cancel.

**NOTE**: On Windows, while recording your input in real time, the application will get set as "not responding". IGNORE THIS, it is working and will begin "responding" after you right click.

## Record Input Manually
Press the "Add click" button, then click where on the screen you want to click. If you want a delay between clicks, type the number of seconds in the "Delay" field, then add your click. If no delay is present, it will perform the clicks as fast as your OS will allow. Repeat for each click, Select "Playback Input" beneath "Add Click" to begin to play back the list of actions on a loop. Pressing escape will end the loop and finish the last iteration of mouse movement, then cancel.


All loop iterations pause for 0.5 seconds at the end of each iteration before looping again. You can change this to 0 in the source if you want to spam click as fast as possible on something.


## Pyinstaller
You can make an executable from this easily with pyinstaller but you need to provide the path so it can find the `keyboard` and `mouse` modules

`pyinstaller --onefile --paths=/path/to/site-packages  automouse.py`
