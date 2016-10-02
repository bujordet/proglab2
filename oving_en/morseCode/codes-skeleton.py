__author__ = 'keithd'

import arduino_connect


# Codes for the 5 signals sent to this level from the Arduino

_dot = 0
_dash = 1
_symbol_pause = 2
_word_pause = 4
_reset = 3


# Morse Code Class
class Mocoder():

    serial_port = ""
    current_symbol = ""
    current_word = ""

# Note: the codes for dot and dash coming to Python via the serial port are 1 and 2, respectively, since those were most
# convenient at the Arduino level. However, I've switched to 0 and 1 in this dictionary, since it is a lot easier to
# read.  So O = dot, 1 = dash in the _morse_codes dictionary below.  You will need to remember that when looking
# up letters and digits in this dictionary.

    morse_codes = {'01':'a','1000':'b','1010':'c','100':'d','0':'e','0010':'f','110':'g','0000':'h','00':'i','0111':'j',
               '101':'k','0100':'l','11':'m','10':'n','111':'o','0110':'p','1101':'q','010':'r','000':'s','1':'t',
               '001':'u','0001':'v','011':'w','1001':'x','1011':'y','1100':'z','01111':'1','00111':'2','00011':'3',
               '00001':'4','00000':'5','10000':'6','11000':'7','11100':'8','11110':'9','11111':'0'}


    def __init__(self, sport=True):
        if sport:
            self.serial_port = arduino_connect.basic_connect()
        self.reset()

    def reset(self):
        self.current_message = ''
        self.current_word = ''
        self.current_symbol = ''

    # This should receive an integer in range 0-4 from the Arduino via a serial port
    def read_one_signal(self, port=None):
        connection = port if port else self.serial_port
        while True:
            # Reads the input from the arduino serial connection
            data = connection.readline()
            if data:
                return data

    # The signal returned by the serial port is one (sometimes 2) bytes, that represent characters of a string.  So,
    # a 2 looks like this: b'2', which is one byte whose integer value is the ascii code 50 (ord('2') = 50).  The use
    # of function int on the string converts it automatically.   But, due to latencies, the signal sometimes
    # consists of 2 ascii codes.  In that case, we need to pull out each of the codes and convert them separately using
    # chr (and then int).

    def decoding_loop(self):
        while True:
            s = self.read_one_signal(self.serial_port)
            print(s)
            if len(s) == 2:
                self.process_signal(int(chr(s[0])))
                self.process_signal(int(chr(s[1])))
            else:
                self.process_signal(int(s))

    def decoding_signal(self, signal):
        this.s = signal
        if s <= 1:
            update_current_signal(signal)
        elif s == 2:
            handle_symbol_end(signal)
        elif s > 2:
            handle_word_end(signal)

    def update_current_signal(self, signal):
        current_symbol += signal

    def handle_symbol_end(self):
        update_current_word(morse_codes(current_symbol))
        current_symbol = ""

    def update_current_word(self, symbol):
        current_word = symbol

    def handle_word_end(self):
        handle_symbol_end()
        print(current_word)
        current_word = ""

test = Mocoder()
test.decoding_loop()