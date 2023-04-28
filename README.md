# Clipboard
A macropad made to make copy/paste easier

## Isn't this basically just a small macropad?
Yes! There's no reason you have to use this exclusively for copy/pasting, or other common shortcuts. You can do whatever you want with it, really. I was comissioned to design this by a friend who does a lot of copy/pasting at work. As he would like to save himself from a perpetually sore wrist, it was designed to the specifications he provided, right down to the specific intended use case. Since it's meant to be used for copying and pasting in an office-like environment, "Clipboard" just so happened to be a good play on words. (Shoutouts to clue for pointing that out!)

## Ok but what about the components?? The Tiny2040 is like $15 alone!
Short answer: Because I already have the parts lol

Long answer: To keep costs down, the deisgn was made to use parts we (myself and the friend who commissioned this board) already own. We both have a spare Tiny2040, I have hundreds of 1N4148 diodes from making keyboards, and I also have tons of leftover Kailh sockets and SK6812MINI-Es from the initial run of the [PicoLX](https://github.com/dj505/PicoLX).

If people actually like and use this thing I might put together a Seeed XIAO RP2040 version to keep costs down, as it has an extremely similar form factor and costs a little less.

# Bill of Materials

|       Part       |      Package      | Qty |
|------------------|-------------------|-----|
| 100nF Capacitor  | 0805              | 3   |
| 1N4148 Diode     | DO-35             | 4   |
| SK6812MINI-E     | MINI-E            | 3   |
| Keyboard Switch  | MX-style          | 3   |
| Rotary Encoder   | PEC12R-4215F-S0024| 1   |
| Pimoroni Tiny2040| N/A               | 1   |
| SN74LV1T34DBV    | SOT-23-5          | 1   |

# Firmware
This board is meant for use with KMK or QMK. I will provide ready-to-use KMK files at a later date, so keep an eye on this section. An OLED display will also be supported. Instructions will be updated here when ready!

# Credits
* [Tiny2040 Symbol & Footprint](https://github.com/chinatsu/tiny2040) by [chinatsu](https://github.com/chinatsu) - Licensed under Creative Commons Attribution-ShareAlike 3.0 Unported. License can be found in `rp2040` directory. The following changes were made to the pcbnew footprint for this project:
    * "U1" and "Tiny2040" text on silkscreen layer have been moved
    * Rectangular pads were added to the front copper layer to allow for surface mounting
    * Silkscreen outline was changed so as to not overlap with the rectangular pads
* [marbastlib](https://github.com/ebastler/marbastlib) by [ebastler](https://github.com/ebastler) - Licensed under the CERN Open Hardware Licence Version 2 - Permissive.
* [MX_V2](https://github.com/ai03-2725/MX_V2) and [MX_Alps_Hybrid](https://github.com/ai03-2725/MX_Alps_Hybrid) by [ai03](https://github.com/ai03-2725) - Both licensed under the MIT License.