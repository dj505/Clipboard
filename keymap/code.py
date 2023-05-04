import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.modules.encoder import EncoderHandler
from kmk.modules.power import Power
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.LED import LED
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.oled import (
    Oled,
    TextEntry,
    ImageEntry
)

keyboard = KMKKeyboard()

# Custom "Keys"
PAINT = simple_key_sequence(
    (
        KC.LGUI(KC.R),
        KC.MACRO_SLEEP_MS(500),
        KC.M,
        KC.S,
        KC.P,
        KC.A,
        KC.I,
        KC.N,
        KC.T,
        KC.ENTER
    )
)
TASKMGR = KC.LCTRL(KC.LSHIFT(KC.ESC))
LOCK = KC.LGUI(KC.L)

tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules.append(tapdance)

power = Power()
keyboard.modules.append(power)

i2c_bus = busio.I2C(board.GP27, board.GP26)

oled_ext = Oled(
    entries=[
        TextEntry(text='CLIPBOARD', x=128, y=0, x_anchor='R'),
        TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='COPY/PASTE', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='UNDO/REDO', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='SCREENSHOT', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='MISC SYSTEM', x=40, y=32, y_anchor='B', layer=3),
        TextEntry(text='MEDIA', x=40, y=32, y_anchor='B', layer=4),
        TextEntry(text='RGB', x=40, y=32, y_anchor='B', layer=5),
        TextEntry(text='SETTINGS', x=40, y=32, y_anchor='B', layer=6),
        TextEntry(text='0123456', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=6, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=12, y=4, inverted=True, layer=2),
        TextEntry(text='3', x=18, y=4, inverted=True, layer=3),
        TextEntry(text='4', x=24, y=4, inverted=True, layer=4),
        TextEntry(text='5', x=30, y=4, inverted=True, layer=5),
        TextEntry(text='6', x=36, y=4, inverted=True, layer=6),

        # Rotary encoder labels
        TextEntry(text='L/R', x=64, y=42, layer=0),
        TextEntry(text='VOLUME', x=64, y=42, layer=1),
        TextEntry(text='ZOOM', x=64, y=42, layer=2),
        TextEntry(text='PNT ZOOM', x=64, y=42, layer=3),
        TextEntry(text='VOLUME', x=64, y=42, layer=4),
        TextEntry(text='RGB HUE', x=64, y=42, layer=5),
        TextEntry(text='UNUSED', x=64, y=42, layer=6),

        # Key labels
        TextEntry(text='SELECT', x=0, y=42, layer=0),
        TextEntry(text='COPY', x=0, y=54, layer=0),
        TextEntry(text='PASTE', x=64, y=54, layer=0),
        TextEntry(text='MUTE', x=0, y=42, layer=1),
        TextEntry(text='UNDO', x=0, y=54, layer=1),
        TextEntry(text='REDO', x=64, y=54, layer=1),
        TextEntry(text='RST ZOOM', x=0, y=42, layer=2),
        TextEntry(text='ALT+PRTSC', x=0, y=54, layer=2),
        TextEntry(text='SNIP TOOL', x=64, y=54, layer=2),
        TextEntry(text='PAINT', x=0, y=42, layer=3),
        TextEntry(text='TASK MNGR', x=0, y=54, layer=3),
        TextEntry(text='LOCK SCRN', x=64, y=54, layer=3),
        TextEntry(text='PLAY/PAUSE', x=0, y=42, layer=4),
        TextEntry(text='PREV SONG', x=0, y=54, layer=4),
        TextEntry(text='NEXT SONG', x=64, y=54, layer=4),
        TextEntry(text='RGB TGL', x=0, y=42, layer=5),
        TextEntry(text='SPD-', x=0, y=54, layer=5),
        TextEntry(text='SPD+', x=64, y=54, layer=5),
        TextEntry(text='DEBUG TGL', x=0, y=42, layer=6),
        TextEntry(text='RESET', x=0, y=54, layer=6),
        TextEntry(text='RELOAD', x=64, y=54, layer=6),
    ],
    i2c=i2c_bus,
    device_address=0x3C,
    width=128,
    height=64,
    flip=False,
    flip_left=False,
    flip_right=True,
    dim_time=10,
    dim_target=0.1,
    off_time=120,
    powersave_dim_time=5,
    powersave_dim_target=0.1,
    powersave_off_time=15,
    brightness=1,
    brightness_step=0.1,
)
keyboard.extensions.append(oled_ext)

leds = LED(led_pin=[board.LED_R, board.LED_G, board.LED_B])
# Num lock = red
# Caps lock = green
# Scroll lock = blue

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if not self.get_num_lock():
            leds.set_brightness(100, leds=[0])
        else:
            leds.set_brightness(0, leds=[0])

        if not self.get_caps_lock():
            leds.set_brightness(100, leds=[1])
        else:
            leds.set_brightness(0, leds=[1])

        if not self.get_scroll_lock():
            leds.set_brightness(100, leds=[2])
        else:
            leds.set_brightness(0, leds=[2])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)
        if self.report_updated:
            self.set_lock_leds()

keyboard.extensions.append(leds)
keyboard.extensions.append(LEDLockStatus())

keyboard.col_pins = (board.GP1, board.GP0)
keyboard.row_pins = (board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
keyboard.modules.append(layers)

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

keyboard.keymap = [
    [   # Layer 1 - Copy/Paste
        KC.TD(KC.LSHIFT, KC.LCTRL(KC.A)), KC.TD(KC.TO(1), KC.TO(6)), # Shift/Ctrl+A, Toggle layer 2,
        KC.LCTRL(KC.C),                   KC.LCTRL(KC.V)             # Ctrl+C, Ctrl+V
    ],
    [
        # Layer 2 - Undo/Redo
        KC.MUTE,                          KC.TD(KC.TO(2), KC.TO(0)), # Mute, Toggle layer 3,
        KC.LCTRL(KC.Z),                   KC.LCTRL(KC.Y)             # Ctrl+Z, Ctrl+Y
    ],
    [
        # Layer 3 - Screenshots
        KC.LCTRL(KC.N0),                  KC.TD(KC.TO(3), KC.TO(1)), # CTRL+0, Toggle layer 4,
        KC.LALT(KC.PSCREEN),              KC.LGUI(KC.LSHIFT(KC.S))   # PrtSc, Alt+PrtSc
    ],
    [
        # Layer 4 - Misc System
        PAINT,                            KC.TD(KC.TO(4), KC.TO(2)), # MS Paint, Toggle layer 5,
        TASKMGR,                          LOCK                       # task manager, Win+L
    ],
    [
        # Layer 5 - Media Controls
        KC.MPLY,                          KC.TD(KC.TO(5), KC.TO(3)), # Mute, Toggle layer 6,
        KC.MPRV,                          KC.MNXT                    # Next song, previous song
    ],
    [   # Layer 6 - RGB Settings
        KC.RGB_TOG,                       KC.TD(KC.TO(6), KC.TO(4)), # toggle RGB, Toggle layer 1,
        KC.RGB_AND,                       KC.RGB_ANI                 # decrease animation speed, increase animation speed
    ],
    [   # Layer 7 - KMK Settings
        KC.DEBUG,                         KC.TD(KC.TO(0), KC.TO(5)), # Toggle power saving, toggle RGB,
        KC.RESET,                         KC.RELOAD                  # reset, reload
    ]

]

encoder_handler = EncoderHandler()
encoder_handler.divisor = 4
encoder_handler.pins = ((board.GP4, board.GP5, None),)

encoder_handler.map = [
    [( KC.LEFT,             KC.RIGHT)],            # Layer 1 (Left, right arrows)
    [( KC.VOLD,             KC.VOLU)],             # Layer 2 (Also volume down, volume up)
    [( KC.LCTRL(KC.MINUS),  KC.LCTRL(KC.EQUAL) )], # Layer 3 (Ctrl +, Ctrl -)
    [( KC.LCTRL(KC.PGDOWN), KC.LCTRL(KC.PGUP) )],  # Layer 4 (Paint zoom in, zoom out)
    [( KC.VOLD,             KC.VOLU)],             # Layer 5 (Once again, volume down, volume up)
    [( KC.RGB_HUD,          KC.RGB_HUI )]          # Layer 6 (RGB hue decrease, increase)
]

keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
