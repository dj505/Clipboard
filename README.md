# Clipboard
A macropad made to make copy/paste easier  
![Fully assembled Clipboard](/Photos/Clipboard.jpg "Clipboard")

## Isn't this basically just a small macropad?
Yes! There's no reason you have to use this exclusively for copy/pasting, or other common shortcuts. You can do whatever you want with it, really. I was comissioned to design this by a friend who does a lot of copy/pasting at work. As he would like to save himself from a perpetually sore wrist, it was designed to the specifications he provided, right down to the specific intended use case. Since it's meant to be used for copying and pasting in an office-like environment, "Clipboard" just so happened to be a good play on words. (Shoutouts to clue for pointing that out!)

## RP2040-Zero Branch
The RP2040 Zero is significantly cheaper than the Tiny2040 and has more IO. Those extra pins aren't connected on the PCB itself, but you can solder wires to them easily enough if you want to add extra peripherals to the Clipboard. The firmware should also work without any changes as the pinout is nearly identical!

# Bill of Materials

|       Part       |      Package      | Qty |
|------------------|-------------------|-----|
| 100nF Capacitor  | 0805              | 3   |
| 1N4148 Diode     | DO-35             | 4   |
| SK6812MINI-E     | MINI-E            | 3   |
| Keyboard Switch  | MX-style          | 3   |
| Rotary Encoder   | PEC12R-4215F-S0024| 1   |
| RP2040-Zero      | N/A               | 1   |
| SN74LV1T34DBV    | SOT-23-5          | 1   |

# Firmware
This board was developed using [KMK Firmware](https://github.com/KMKfw/kmk_firmware). Instructions for setting up KMK on your board can be found in the [Getting Started](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md) docs.

After KMK itself is set up, delete the existing `code.py` or `main.py` on the CIRCUITPY drive, and copy the `code.py` file in this repository's "keymap" directory to the root of the drive.

You're done!

## Notes on the firmware
- By default, it does a lot. Maybe too much. *Probably* too much, actually. Please feel free to edit it down for your own use case! The [KMK docs](http://kmkfw.io/docs/) are your friend.
- The OLED code used here is currently undocumented. It's fully reworked from example code I found on a GitHub issue thread that I can't seem to find again. It should be straightforward enough to understand, though!

## Required CircuitPython libraries
CircuitPython libraries can be found [here.](https://circuitpython.org/libraries)  
This project will require the following libraries from the "lib" folder of the library bundle:
* neopixel.mpy
* adafruit_displayio_ssd1306.mpy (required for OLED)
* adafruit_display_text (required for OLED)  
Copy these files and folders into the "lib" folder on your CIRCUITPY drive.

## Connecting an OLED display
Clipboard is made with an I2C 128x64 SSD1306 OLED display in mind. If you have a different display with a different resolution, you will have to edit `code.py` accordingly. The underside of the board has the appropriate pins marked, with **SDA on GP26** and **SCL on GP27**. The VCC (or VDD (or 3.3V)) pin on the OLED should be wired to the +3V3 pin on the Clipboard.

# Credits
* [Tiny2040 Symbol & Footprint](https://github.com/chinatsu/tiny2040) by [chinatsu](https://github.com/chinatsu) - Licensed under Creative Commons Attribution-ShareAlike 3.0 Unported. License can be found in `rp2040` directory. The following changes were made to the pcbnew footprint for this project:
    * "U1" and "Tiny2040" text on silkscreen layer have been moved
    * Rectangular pads were added to the front copper layer to allow for surface mounting
    * Silkscreen outline was changed so as to not overlap with the rectangular pads
* [marbastlib](https://github.com/ebastler/marbastlib) by [ebastler](https://github.com/ebastler) - Licensed under the CERN Open Hardware Licence Version 2 - Permissive.
* [MX_V2](https://github.com/ai03-2725/MX_V2) and [MX_Alps_Hybrid](https://github.com/ai03-2725/MX_Alps_Hybrid) by [ai03](https://github.com/ai03-2725) - Both licensed under the MIT License.
