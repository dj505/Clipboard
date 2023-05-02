print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP1, board.GP0)
keyboard.row_pins = (board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
encoder_handler = EncoderHandler()
encoder_handler.pins = (board.GP4, board.GP5, None)
keyboard.modules = [layers, encoder_handler]

media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

frontglow = RGB(
    pixel_pin=board.GP3,
    num_pixels=3,
    val_limit=100,
    val_default=25,
    animation_mode=AnimationModes.RAINBOW,
)
keyboard.extensions.append(frontglow)

keyboard.SCL = board.GP27
keyboard.SDA = board.GP26
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.LAYER,1:["LYR 1","LYR 2"]},
        corner_two={0:OledReactionType.LAYER,1:["MEDIA","ZOOM"]},
        corner_three={0:OledReactionType.LAYER,1:["COPY","PRNT"]},
        corner_four={0:OledReactionType.LAYER,1:["PASTE","ALTPRNT"]},
    ),
    oWidth=128,
    oHeight=64,	
    toDisplay=OledDisplayMode.TXT,
    flip=False
)
keyboard.extensions.append(oled_ext)

keyboard.debug_enabled = True

keyboard.keymap = [
    [   # Layer 1
        KC.TO(1),       KC.MUTE,       # Toggle layer 2, Mute,
        KC.LCTRL(KC.C), KC.LCTRL(KC.V) # Ctrl+C, Ctrl+V
    ],

    [   # Layer 2
        KC.TO(0),   KC.LCTRL(KC.N0),    # Toggle layer 1, CTRL+0,
        KC.PSCREEN, KC.LALT(KC.PSCREEN) # PrtSc, Alt+PrtSc
    ]

]

encoder_handler.map = [
    [( KC.VOLD,            KC.VOLU)],            # Layer 1 (Volume down, volume up)
    [( KC.LCTRL(KC.EQUAL), KC.LCTRL(KC.MINUS) )] # Layer 2 (Ctrl +, Ctrl -)
]

if __name__ == '__main__':
    keyboard.go()

