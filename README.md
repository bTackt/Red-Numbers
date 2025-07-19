# Red Numbers

Created by Red Sun, based upon ideas from default CR machine numbers, Lapwing numbers, Jeff numbers, and Harri numbers.

Greatly compress your number writing into fewer strokes with a fully customizable dictionary!

### **[Complete Documentation](FULLTHEORY.md)**

## How does Red Numbers save you strokes?

Here is a comparison of Red Numbers and the way my CR school taught numbers.

Output|Court Reporting School (strokes)|Red Numbers (strokes)
-----|-----|-----
$1,000,000,042|`TKHR*/1/WR-RB/0/0/0/WR-RB/0/0/0/WR-RB/0/4/2` (14)	|`#EUR/#EU/#E/-6RB/34` (5)
4:35 p.m.|`4/KHR*/35/P*PL` (4)|`-6R/4R07BGZ` (2)
23,461|`23/WR-RB/46/1` (4)|`2-BG/-6R8G/#-R` (3)
$8.91|`TKHR*/8/P-P/9/1` (4)|`347/30R8` (2)
1998|`19/9/8` (3)|`23078` (1)

## Installation

1. Download your file of choice. (.py is recommended)
2. If using the .py version, be sure to have the plover-python-dictionary plugin installed in Plover.
3. Enjoy!

Note: .json, .dct, and .rtf file formats are also provided for vanilla Plover, Javelin, DigitalCAT, and other CAT users.

## How to learn Red Numbers

This is an entirely modular system; that is, you can stop at any step you like and still enjoy. The more you learn, the more power you unlock, but the learning curve is not steep as it is still completely functional at the beginning level.

The steps are in easiest to hardest order; however, if you are planning to utilize the complete power of this system, you may prefer learning the steps in the order 1, 3, 2, 4.

This is the quick and dirty, but for more details on why certain design choices were made, read the [complete documentation](FULLTHEORY.md).

### Step 1: Basic Number Pad

Every stroke in this dictionary uses the number bar (`#`). On traditional machines, this is the long bar at the top. On most hobbyist layouts, this is the top-row key above initial S.

On a traditional machine, always use your **left middle finger** to hit the number bar in this theory.

Use your right pointer, middle, and ring fingers on `FRPBLG` to type digits 1-9 in a numberpad pattern. (This is the exact same as in Lapwing.)

Digit|Steno
-----|-----
1|`R`
2|`B`
3|`G`
4|`FR`
5|`PB`
6|`LG`
7|`F`
8|`P`
9|`L`

The right thumb is used to type zeroes.

Digit|Steno
-----|-----
0|`E`
00|`U`
000|`EU`

Combining any of the single digit numbers with a zero key affixes that number of zeroes to that digit. This has similar functionality to the O key in default numbers.

For example, `PB` and `U` together (`#UPB`) outputs 500.

All digits typed in this dictionary contain glue; that is, they stick to other consecutive strokes with glue. So to write a multi-digit number, simply type each digit one after another and it will appear without spaces.

### Step 2: Left and Right Hand Modifiers

Left hand modifiers are written using the keys `STPHRA*` and right hand modifiers are written using the keys `DZ`.

Type each of these in combination with a digit from the number pad area and see what happens!

Function|Steno|Comments
-----|-----|-----
word converter|`A`|
a.m. suffix|`-D`|
p.m. suffix|`-Z`|
o'clock suffix|`-DZ`|
`-` suffix|`H`|
`:` prefix|`HR`|
`.` prefix|`P`|
`$` prefix|`PH`|alternate money sign available on `PH*`
`'` prefix|`PHR`|for abbreviated years
`%` suffix|`R`|this is not court reporting canon
`percent` suffix|`RA`|the number is not converted, only percent
`s` suffix|`S`|for '20s and 1920s  and 10s and 20s
`19` prefix|`TP`|intended behavior works with two-digit numbers
`20` prefix|`TH`|intended behavior works with two-digit numbers
`,` suffix|`T`|because million, thousand, verbally comes after a number not before the next
ordinal conversion|`ST`|

Some of these modifiers can be used at the same time to do both at once:

Function|Steno
-----|-----
ordinal + word conversion|`STA`
`$` and `,` suffix|`TPH`
`'` + `s`|`SPHR`
`.` and `%`|`PR`
`.` and `percent`|`PRA`

`a.m.`, `p.m.`, and `o'clock` can also be combined with the `:` prefix.

By typing these modifiers in one stroke with your desired digits, you can save strokes!

If you forget to combine them into one stroke, no problem. Most of these modifiers work as a standalone stroke; for example, typing `#P` will output a period with glue, ready to stick to whatever numbers come before and after it.

Note that the money strokes, `PH` and `PH*` will not output the money symbol when typed alone before a number. It will, however, retroactively add the money symbol and add commas to the entire last number glued when typed alone *after* the number.

### Step 3: Two-Digit Numbers

To type two-digit numbers where neither digit is 0, type any two digits at the same time on the number pad.

For example, `FR` and `P` at the same time produces 48. However, instead of ascending order, the digits will be output in left to right order. So, `FR` and `B` at the same time outputs 42, not 24.

#### Flip 2 digits with O

In order to flip the digits backwards, use the `O` key at the same time as a two-digit number. So to input 24, combine `FR`, `B`, and `O`.

#### Two-digit numbers where the digits are in the same column

Some numbers cannot be input at the same time, such as 4 and 7 or 3 and 9. To write a two-digit number that consists of two numbers from the same column, write the first one as usual on the number pad, then combine it with T, TS, or S, based on the row in which the second digit resides. So for example, to type 25, `B` should be combined with `TS` since 5 is from the middle row.

*This is the least intuitive aspect of Red Numbers. If you dislike it, feel free to stick to writing these numbers digit by digit.*

For these numbers that include T, TS, and S, flipping them is disabled by default, because their order is already included. That is to say, the intended method of writing 52 is PB with S, not B with TS and flipped.

#### Double 1 digit with O

Lastly, to write double digit numbers consisting of the same digit, that is, multiples of 11, combine `O` with a single-digit number typed on the right hand. So to write 55, `PB` should be combined with `O`.

You may point out that O was used for flipping; however, that is for two digit numbers. O with a two digit number flips, while O with a one digit number doubles.

You can now write any number from 0 to 99 in one stroke, as well as those numbers with anywhere from none to three zeroes on the end!

*Red Numbers doesn't support writing three+ digit numbers, where none of those digits are 0, in one stroke.*

### Step 4: Customization

Now that you've learned the system, you've likely learned what works and what doesn't work for you.

In the .py file format on lines 10-78, there are instructions on customizing the code and switching the values of variables to your liking.

#### Flipping behavior

By default, this dictionary outputs two-digit numbers in their physical left-to-right position on the numberpad. If you dislike this behavior and prefer the digits to appear in ascending order by value, you can switch this.

#### Remapping modifiers

You can remap the modifiers to different keys, for example. Red Numbers only uses `STPHRA*` for left hand modifiers because it is assumed that these are the most accessible keys with your left hand while using the left middle finger to press the number bar on a traditional machine.

For example, you may decide that you can also reliably and accurately access the `K` key and work that into the modifiers. Or, you may decide you prefer a different finger than the left middle finger for the number bar, which will change which keys are accessible to use as modifiers.

If you're using a hobbyist layout with split S, you may have access to all of the initial side, `STKPWHRA*` to use for modifiers.

#### Other options

There are also a few options regarding two-digit numbers using `T`, `TS`, and `S`, and what symbols the money modifier outputs.

#### Flattener

If you modify the .py and need to regenerate a new flattened version for Javelin or similar, you can use the provided `red-flattener.py` and it will generate a .json version, which can be loaded into Plover to convert it to a .rtf version.

By default, it points to `red_n` so be sure to rename your file or change the code.

## Tabled and Coming Soon

By coming soon, I mean it's not really coming at all.

Functions not available that I'm currently not interested in adding:
* Roman numerals
* number "or" number (e.g. two or three)

Fixes I should make but I don't feel like it:
* Zero percent (0 percent is not allowed in court reporting)
* Better commas behavior (just like the money sign does retroactive comas, there should be a retroactive commas function in addition/in place of the complete control comma prefix function available currently)

Quality of life upgrades:
* Images to go in the guide/tutorial/documentation
* Interactive drills to help try and understand the system
* Reducing the nonsensical entries (mostly the ones with too many zeroes on the end)
* More file formats to support more CATs, etc.