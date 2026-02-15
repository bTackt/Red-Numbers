# Red Numbers Documentation

*This has the same information as the README, but in a more extended, wordy format explaining my design decisions.*
 
This is a system I designed with the goal of reducing the strokes needed to write numbers in a court reporting context. The base idea comes from the number pad method of writing numbers in Lapwing, but the functionality is extended.

Court reporting numbers, by default, use the number bar combined with the top row keys as well as `A` and `O` to create the 10 digits. This system does not seem to have been majorly improved or innovated by any currently taught professional theories, beyond perhaps a key to flip double digit numbers.

Numbers are used in court reporting in many contexts, including time, money, years, figures, and more. When I started learning numbers in theory class, I found that we had to program each decimal point, each colon, each comma, each p.m., etc. manually with its own stroke. I thought it would be far faster to be able to write these number accessories in combined strokes, saving strokes and time.

The issue with the default system for numbers on the court reporting layout is that there isn’t a lot of room to add more customization. Apart from `E` and `U`, the remaining keys cannot be combined with all possible number inputs. For example, `#3W` may be hard to write as the most natural way to type `#3` is with the middle finger on both the `#` key and `P` key. This complicates combining `W` as now the writer must switch the finger writing the `#` key to something else. When considering two digit numbers, then the selection for the finger pressing `#` gets even more irregular and requires more calculation and hesitation to input.

Since the primary goal of theory is to have a system that takes little effort to recall, is quick to input, and lends itself ultimately to speed, I have redesigned the numbers completely.

The general layout has the left middle finger pressing the number bar, the left fingers left open by that constraint controlling modifiers, and the right hand writing the number. Additionally, `D` and `Z` are used as modifiers as well.

## Left middle finger pressing the number bar

This choice was made in order to standardize the options available for left hand modifiers. For example, with this setup, `W` is not accessible as a modifier key, but `S`, `T`, `P`, and `H` are. `R` and `K` are also accessible for select modifiers. I chose left middle finger as it is the longest and compared to left pointer finger on number bar and folding the middle finger to reach `W`, left middle finger on number bar and reaching down to hit `R` is easier.

If you want to use a different finger for number bar, you may customize the left hand modifiers to accommodate your choice. I do not foresee any right finger being an option, however. Overall, I recommend choosing one finger for the number bar and sticking to it; it will create the highest potential for speed with this number theory.

## Right fingers writing the number

This system draws from the Lapwing number pad.

Personally, this appealed to me since I already have muscle memory for typing numbers on a number pad. However, that doesn’t mean I couldn’t also learn to type default court reporting numbers at speed with enough practice. I chose this system for the reasons mentioned above, and the potential to combine modifiers. That is why, if the access to modifiers appeals to you, I encourage you to try learning the number pad if you don’t know it yet. At best, the muscle memory for court reporting numbers is arbitrary and is learnable, so number pad numbers can be learned by the same logic. 

The first three fingers on the right hand are used to control a three-column number pad.

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

Combining any of the single digit numbers with a zero key affixes that number of zeroes to that digit. This has similar functionality to the `O` key in default numbers.

All numbers include glue, so you should already be able to type any number you want digit by digit. If you find extended functionality too hard to grasp, there is nothing wrong with using this much only. However, you can unlock a lot more power by learning to type two-digit numbers.

This is a function that default court reporting numbers has, but Lapwing does not. By typing two numbers at the same time in default numbers, the corresponding two digit number appears in ascending order. Some court reporters customize their dictionary by adding a flip key, such as `E` or `R` to reverse the order of the digits.

In my system, you can form two digit numbers by typing any two digits at the same time on the number pad. For example, `FR` and `P` at the same time produces 48. However, instead of ascending order, Red Numbers outputs the digits in left to right order. So, `FR` and `B` at the same time outputs 42, not 24.

In order to flip the digits backwards, use the `O` key at the same time as a two digit number from the first three right fingers (that is, zeroes do not count for two digits. They are additional and calculated after the flip). So to input 24, type `FR`, `B`, and `O`.

As a spatial learner, I found this left-to-right system more intuitive than ascending order in the context of the number pad. After practicing for a few months, I can confirm it is easy to recall and works well. If you really dislike left-to-right and prefer ascending order, you can customize the code.

You may have noticed that some numbers cannot be input at the same time, such as 4 and 7 or 3 and 9. There are two options at this point. I have created the ability to write these two digit numbers using the `T` and `S` keys, which is not quite as intuitive as it has been so far, which you can learn. Personally, I was able to learn it without too much work. If you find it too hard to learn, you can stick to writing these numbers digit by digit. However, you miss out on 25, which I see as a pretty central and popular number.

To write a two-digit number that consists of two numbers from the same column, write the first one as usual on the number pad, then combine it with `T`, `TS`, or `S`, based on the row in which the second digit resides. So for example, to type 25, `B` should be combined with `TS` since 5 is from the middle row.

For these numbers that include `T`, `TS`, and `S`, flipping them is disabled by default, because their order is already included. That is to say, the intended method of writing 52 is `PB` with `S`, not `B` with `TS` and flipped. If you want the ability to flip these numbers turned on, you can customize the code.

Lastly, to write double digit numbers consisting of the same digit, that is, multiples of 11, combine `O` with a single digit number typed on the right hand. So to write 55, `PB` should be combined with `O`.

You may point out that `O` was used for flipping; however, that is for two-digit numbers. `O` with a two-digit number flips, while `O` with a one-digit number doubles.

(As a sidenote: Why did I not go with Harri numbers’ dual number pad system, which can input two digits at once? Although it contains the most theoretical raw power, I do not see it as being intuitive and conducive to speed. Typing on a two-column number pad is not as intuitive as a three-column number pad in my opinion, and I believe that it requires a lot of extra calculation to be able to accurately and quickly input two digits on two separate number pads. Once fully trained, theory should be completely mindless, and I don’t see the dual number pads as a system that could become mindless for me personally. If you do, I encourage you to try Harri numbers instead as the edge cases for two-digit numbers in my system are slightly convoluted.)

You should now be equipped to write any number from 0 to 99 in one stroke, as well as those numbers with anywhere from none to three zeroes on the end. Already, this system should provide more power than default court reporting numbers. The only feature that court reporting numbers has that this system doesn’t is the ability to type three digit numbers or more; however, I don’t see that as a big loss as you can only type multiple digits in ascending order anyway.

## Left fingers controlling modifiers and DZ

In addition to the number bar and `O`, the rest of the keys on the left side and `*` are used for additional modifiers to the number typed by the right hand.

Function|Steno|Comments
-----|-----|-----
word converter|`A`|
a.m. suffix|`-D`|
p.m. suffix|`-Z`|
o'clock suffix|`-DZ`|
`-` suffix|`H`|always sticks to the following word
`:` prefix|`HR`|
`.` prefix|`P`|
`$` prefix|`PH`|alternate money sign available on `PH*`
`'` prefix|`PHR`|for abbreviated years
`%` suffix|`R`|this is not court reporting canon
`percent` suffix|`RA`|the number is not converted, only percent
`s` suffix|`S`|for '20s and 1920s  and 10s and 20s
`19` prefix|`TP`|
`20` prefix|`TH`|
`,` suffix|`T`|because million, thousand, verbally comes after a number not before the next
ordinal conversion|`ST`|
ordinal + word conversion|`STA`|
`$` and `,` suffix|`TPH`|
`'` + `s`|`SPHR`|
`.` and `%`|`PR`|
`.` and `percent`|`PRA`|

These modifiers have been designed based on my court reporting education and the priorities of transcripts, as well as the words typically spoken to represent these punctuation marks. As mentioned before, this system is designed with court reporting in mind, so it is made in consideration of how dictation would work. This is in contrast to Lapwing, which can be optimized for general typing. However, since I still want the ability to use my theory for general typing, I have included some things not in the court reporting canon, such as the percent symbol, which is comically banned in court reporting school.

Lastly, most of these modifiers work on their own in a single stroke, so if you fail to include it in a stroke together, you can still add it on in another stroke with no problem.

These are highly customizable and you can modify them to your liking in the code.

Here is a contrast of my theory and the one I was taught in school.

Output|Court Reporting School (strokes)|Red Numbers (strokes)
-----|-----|-----
$1,000,000,042|`TKHR*/1/WR-RB/0/0/0/WR-RB/0/0/0/WR-RB/0/4/2` (14)	|`#EUR/#EU/#E/-6RB/34` (5)
4:35 p.m.|`4/KHR*/35/P*PL` (4)|`-6R/4R07BGZ` (2)
23,461|`23/WR-RB/46/1` (4)|`2-BG/-6R8G/#-R` (3)
$8.91|`TKHR*/8/P-P/9/1` (4)|`347/30R8` (2)
1998|`19/9/8` (3)|`23078` (1)