from machine import Pin
from time import sleep

def dot(signal, period=1):
    """Represents a 'dot' in Morse code."""
    signal.value(1)
    sleep(period)
    signal.value(0)
    
def dash(signal, period=1):
    """Represents a 'dash' in Morse code."""
    signal.value(1)
    sleep(period*3)
    signal.value(0)
    
def s(_signal=None, period=1):
    """A short pause used within encoded characters"""
    sleep(period)
    
def m(_signal=None, period=1):
    """A medium pause used between characters in a word"""
    sleep(period*3)
    
def l(_signal=None, period=1):
    """A long pause used between words"""
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
    '!': [dash, s, dot, s, dash, s, dot, s, dash, s, dash],
    '&': [dot, s, dash, s, dot, s, dot, s, dot],
    ';': [dash, s, dot, s, dash, s, dot, s, dash, s, dot],
    '_': [dot, s, dot, s, dash, s, dash, dot, s, dash],
    '$': [dot, s, dot, s, dot, s, dash, s, dot, s, dot, s, dash]
    }

def string_to_morse(string):
    """
    Converts a string to an executable list of Morse functions.

    :param string: The string to translate to Morse code.
    :return: A list of elementary Morse functions.
    """
    morse = []
    string = string.lower()
    for character in string:
        morse.append(string_to_morse_dict[character] + [m])
    
    return [signal for character in morse
            for signal in character]

def transmit(morse, output, period=0.2):
    """
    Transmit Morse code through the output by sequentially executing the functions in the arg "morse".

    :param morse: A list of executable functions representing Morse code.
    :param output: The device to which the Morse should be output. This script is written assuming that
                   the output is a Raspberry Pi Pico W.
    :param period: The base speed of transmission in seconds (using Pico W MicroPython time.sleep).
    """
    for code in morse:
        code(output, period=period)


def validate(output):
    """Used for debugging to transmit every possible character."""
    validation_characters = "abcdefghijklmnopqrstuvwxyz1234567890 .,?\'/():=+-\"@!&;_$"
    morse_validation = string_to_morse(validation_characters)
    transmit(morse_validation, output)
    print("Validation complete.")


def send_morse(input_string, output_device, period=0.2):
    """Translate the input string to Morse code then outputs the code to output_device."""
    morse_list = string_to_morse(input_string)
    transmit(morse_list, output_device, period=period)


device = Pin('LED', Pin.OUT)
device.value(0)
validate(device)
