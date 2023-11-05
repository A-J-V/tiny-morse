# tiny-morse
## How to use:
* Download tiny_morse.py.
* Replace the final line from validate(device) to send_morse("your_message", device).
* Run the script on a Raspberry Pi Pico W using MicroPython, and behold Morse code flashing on your device!

## What this script can do:
* Convert a string of any standard letter, number, punctuation (and 5 non-standard punctuation marks) to Morse Code.
* Flash that Morse code on a Raspberry Pi Pico W.

## What this script cannot do:
* Work on any arbitrary microcontroller. Every device has specific requirements, you'll likely need to adapt the script to your device if it isn't a RPI Pico W.
* Translate characters that are not in the standard Latin alphabet, or considered standard punctuation in Morse. You cannot include, e.g., emojis, arrows <>, or umlauts.

## What this script can do with a little modification:
* Translate any character if you add the character and the Morse encoding to string_to_morse_dict in the script. This should be fast and easy.
* Work on most microcontrollers if you modify the output device and sleep library to fit your device. To do this:
*   1. Import the correct libraries for your device.
    2. Wrap your device's output in a class that contains a method called value() that takes a single integer arg, 1 to turn on the signal, 0 to turn off the signal.
* Plug into your larger project to teach your robots / sensors to communicate in Morse code.

## Summary of project:
This small script converts a string of text into Morse code and flashes it on a device (script works out-of-the-box on Raspberry Pi Pico W).

For many individuals, flashing an LED on a Raspberry Pi Pico (or similar device) is the first step in learning to program microcontrollers. It is the "hello world" of the microcontroller world.

However, it's boring and not particularly useful. This tiny project aims to make flashing an LED more interesting by giving you something to flash: Morse code.

After you write a MicroPython script to flash an LED, you can use tiny_morse.py to adapt your script to be able to flash Morse code.

This is a great project for people learning to program microcontrollers for themselves or with their children. Morse code is still relevant because it is so minimalistic and portable.

Morse code is also a great way to introduce elementary information theory or cryptography. (If you view a dash as two consecutive dots, a medium rest as two consecutive short rests, and a long rest as 3 consecutive short rests, then Morse code is all dots and rests. In other words, it is binary, and can be encoded with 1s and 0s. That's why I say it could be used to introduce information theory in a fun interactive way.)

https://github.com/A-J-V/tiny-morse/assets/72227828/ed4fd393-4258-4e2b-8288-c25b34c3f371
