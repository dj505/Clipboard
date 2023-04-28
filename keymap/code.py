print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
layers = Layers()
mediakeys = MediaKeys()
rgb = RGB(pixel_pin=board.GP13, num_pixels=3)

keyboard.modules = [layers, encoder_handler, mediakeys, rgb]

keyboard.col_pins = (board.GP1, board.GP0)
keyboard.row_pins = (board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [   # Layer 1
        KC.TO(1),       KC.MUTE,
        KC.LCTRL(KC.C), KC.LCTRL(KC.V)
    ],
    
    [   # Layer 2
        KC.TO(0),   KC.LCTRL(KC.N0),
        KC.PSCREEN, KC.LALT(KC.PSCREEN)
    ]
    
]

encoder_handler.pins = ((board.GP4, board.GP5, None))

encoder_handler.map = [
    (( KC.VOLD,            KC.VOLU)), # Layer 1
    (( KC.LCTRL(KC.EQUAL), KC.LCTRL(KC.MINUS) )) # Layer 2
]

if __name__ == '__main__':
    keyboard.go()