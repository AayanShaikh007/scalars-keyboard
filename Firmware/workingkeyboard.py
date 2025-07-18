import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros

# from kmk.extensions.display import Display, TextEntry
# from kmk.extensions.LED import LED, AnimationModes
# from kmk.extensions.display.ssd1306 import SSD1306


col_0 = board.GP0  # Column0
col_1 = board.GP1  # Column1
col_2 = board.GP8  # Column2
col_3 = board.GP9  # Column3
col_4 = board.GP12 # Column4
col_5 = board.GP13 # Column5
col_6 = board.GP16 # Column6
col_7 = board.GP17 # Column7
col_8 = board.GP26


row_0 = board.GP2
row_1 = board.GP3
row_2 = board.GP6
row_3 = board.GP7
row_4 = board.GP10
row_5 = board.GP11
row_6 = board.GP14
row_7 = board.GP15
row_8 = board.GP18
row_9 = board.GP19

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW # the stripe (+) points towards the row 

keyboard.col_pins = (col_0, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8);
keyboard.row_pins = (row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9);


keyboard.keymap = [
    [KC.ESC, KC.KP_ASTERISK, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.DELETE, KC.KP_4, KC.KP_5, KC.KP_6, KC.KP_3, KC.KP_2, KC.KP_1, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.RBRACKET, KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.P, KC.LBRACKET, KC.SCOLON, KC.QUOTE, KC.SLASH, KC.LALT, KC.LEFT, KC.DOWN, KC.RIGHT, KC.KP_7, KC.UP, KC.KP_9, KC.LCTRL, KC.LGUI, KC.RALT, KC.RGUI, KC.RCTRL, KC.TAB, KC.BSLASH, KC.MENU, KC.CAPSLOCK, KC.BSPC, KC.ENTER, KC.LSHIFT, KC.RSHIFT, KC.SPACE, KC.KP_MINUS],  # Row 0
    [KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.GRAVE, KC.N1, KC.N2, KC.N3],  # row 1 test
    [KC.F1]*9,
    [KC.NO, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.NO, KC.NO, KC.NO],
    [KC.F2]*9,
    [KC.F3]*9,
    [KC.F4]*9,
    [KC.F5]*9,
    [KC.F6]*9,
    [KC.F7]*9,
]


if __name__ == '__main__':
    keyboard.go()





# d_pin = board.GP8

# oled_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

# oled_driver = SSD1306(i2c=oled_bus, device_address=0x3C);

# display = Display(
#     display=oled_driver,
#     width=128,
#     height=32, 
#     dim_time=10,
#     dim_target=0.2,
#     off_time=1200,
#     brightness=0.8
# );