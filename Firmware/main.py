import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros

from kmk.extensions.display import Display, TextEntry
from kmk.extensions.LED import LED, AnimationModes
from kmk.extensions.display.ssd1306 import SSD1306


col_0 = board.GP00
col_1 = board.GP01
col_2 = board.GP08
col_3 = board.GP09
col_4 = board.GP012
col_5 = board.GP013
col_6 = board.GP016
col_7 = board.GP017
col_8 = board.GP026


row_0 = board.GP02
row_1 = board.GP03
row_2 = board.GP06
row_3 = board.GP07
row_4 = board.GP010
row_5 = board.GP011
row_6 = board.GP014
row_7 = board.GP015
row_8 = board.GP018
row_9 = board.GP019

d_pin = board.GP8

oled_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

oled_driver = SSD1306(i2c=oled_bus, device_address=0x3C);

display = Display(
    display=oled_driver,
    width=128,
    height=32, 
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
);

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW # the stripe (+) points towards the row 

keyboard.col_pins = (col_0, col_1, col_2, col_3);
keyboard.row_pins = (row_0, row_1, row_2, row_3);

keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12],
    
    [KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC],
    
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH],
    
    [KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER],
    
    [KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT],
    
    [KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.RALT, KC.RGUI, KC.APP, KC.RCTRL],
    #Home/arrow keys/macros ???

]


if __name__ == '__main__':
    keyboard.go()