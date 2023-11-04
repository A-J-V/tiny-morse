"""Converts a text string to morse code that can be
executed as a series of signal flashes.

Morse code is represented here by basic functions that transmit or pause
a signal for a specific duration. A text character is encoded in morse
as a list of these basic functions. By executing the list of functions in
order, the morse code of the text character is transmitted. A large text
string is simply a longer list of basic morse functions comprising the
text and necessary signal pauses.

The workflow is to pass a string to the string_to_morse() function to get
a morse code list. Then pass the list of morse code to the transmit()
function to execute it.

This is a minimal script that was written to flash an LED using
a Raspberry Pi Pico. The transmitter here is just a Pico Pin. By modifying
the transmitter to send a different signal than toggling a Pico Pin, this
script can be easily extended to another use case.
"""



from machine import Pin
from time import sleep

def dot(signal, period=1):
    signal.value(1)
    sleep(period)
    signal.value(0)
    
def dash(signal, period=1):
    signal.value(1)
    sleep(period*3)
    signal.value(0)
    
def s(_signal=None, period=1):
    """Used within encoded characters"""
    sleep(period)
    
def m(_signal=None, period=1):
    """Used between characters in a word"""
    sleep(period*3)
    
def l(_signal=None, period=1):
    """Used between words"""
    sleep(period*7)
    
string_to_morse_dict = {
    'a': [dot, s, dash],
    'b': [dash, s, dot, s, dot, s, dot],
    'c': [dash, s, dot, s, dash, s, dot],
    'd': [dash, s, dot, s, dot],
    'e': [dot],
    'f': [dot, s, dot, s, dash, s, dot],
    'g': [dash, s, dash, s, dot],
    'h': [dot, s, dot, s, dot, s, dot],
    'i': [dot, s, dot],
    'j': [dot, s, dash, s, dash, s, dash],
    'k': [dash, s, dot, s, dash],
    'l': [dot, s, dash, s, dot, s, dot],
    'm': [dash, s, dash],
    'n': [dash, s, dot],
    'o': [dash, s, dash, s, dash],
    'p': [dot, s, dash, s, dash, s, dot],
    'q': [dash, s, dash, s, dot, s, dash],
    'r': [dot, s, dash, s, dot],
    's': [dot, s, dot, s, dot],
    't': [dash],
    'u': [dot, s, dot, s, dash],
    'v': [dot, s, dot, s, dot, s, dash],
    'w': [dot, s, dash, s, dash],
    'x': [dash, s, dot, s, dot, s, dash],
    'y': [dash, s, dot, s, dash, s, dash],
    'z': [dash, s, dash, s, dot, s, dot],
    '1': [dot, s, dash, s, dash, s, dash, s, dash],
    '2': [dot, s, dot, s, dash, s, dash, s, dash],
    '3': [dot, s, dot, s, dot, s, dash, s, dash],
    '4': [dot, s, dot, s, dot, s, dot, s, dash],
    '5': [dot, s, dot, s, dot, s, dot, s, dot],
    '6': [dash, s, dot, s, dot, s, dot, s, dot],
    '7': [dash, s, dash, s, dot, s, dot, s, dot],
    '8': [dash, s, dash, s, dash, s, dot, s, dot],
    '9': [dash, s, dash, s, dash, s, dash, s, dot],
    '0': [dash, s, dash, s, dash, s, dash, s, dash],
    ' ': [l],
    '.': [dot, s, dash, s, dot, s, dash, s, dot, s, dash],
    ',': [dash, s, dash, s, dot, s, dot, s, dash, s, dash],
    '?': [dot, s, dot, s, dash, s, dash, s, dot, s, dot],
    '\'':[dot, s, dash, s, dash, s, dash, s, dash, s, dot],
    '/': [dash, s, dot, s, dot, s, dash, s, dot],
    '(': [dash, s, dot, s, dash, s, dash, s, dot],
    ')': [dash, s, dot, s, dash, s, dash, s, dot, s, dash],
    ':': [dash, s, dash, s, dash, s, dot, s, dot, s, dot],
    '=': [dash, s, dot, s, dot, s, dot, s, dash],
    '+': [dot, s, dash, s, dot, s, dash, s, dot],
    '-': [dash, s, dot, s, dot, s, dot, s, dot, s, dash],
    '\"':[dot, s, dash, s, dot, s, dot, s, dash, s, dot],
    '@': [dot, s, dash, s, dash, s, dot, s, dash, s, dot],
    }

def string_to_morse(string):
    morse = []
    string = string.lower()
    for character in string:
        morse.append(string_to_morse_dict[character] + [m])
    
    return [signal for character in morse
            for signal in character]

def transmit(morse, output):
    for signal in morse:
        signal(output, period=0.2)


def validate(output):
    """Used for debugging to transmit every possible character."""
    validation_characters = "abcdefghijklmnopqrstuvwxyz1234567890 .,?\'/():=+-\"@"
    morse_validation = string_to_morse(validation_characters)
    transmit(morse_validation, output)
    print("Validation complete.")

signal = Pin('LED', Pin.OUT)
signal.value(0)
validate(signal)
