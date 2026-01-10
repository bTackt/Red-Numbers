# Red's Numbers dictionary for Plover
# Theory composed by taking inspiration from default CR machine numbers, Lapwing numbers, Harri numbers, Jeff's numbers
# Code heavily based off of Jeff's numbers
# Modular system - all strokes are single blocks
# Release v1.2  - 1/9/26
#
# See README.md for usage details.
import re

##################################### CUSTOMIZATION INSTRUCTIONS #####################################
# 1. Change the default mappings of left-hand modifiers below

LEFT_MODIFIERS = {
    ""                      : "",
    "convertToEnglishWords" : "A",      # Convert to English words
    "periodPrefix"          : "P",      # . prefix
    "commaSuffix"           : "T",      # , suffix
    "hyphenSuffix"          : "H",      # - suffix
    "sSuffix"               : "S",      # s suffix
    "20Prefix"              : "TH",     # 20 prefix
    "19Prefix"              : "TP",     # 19 prefix
    "moneyPrefix"           : "PH",     # $ prefix by default
    "altMoneyPrefix"        : "PH*",    # secondary money sign (€ by default) note: only here for flattener, detected in code through moneyPrefix
    "colonPrefix"           : "HR",     # : prefix
    "apostrophePrefix"      : "PHR",    # ' prefix
    "ordinalSuffix"         : "ST",     # ordinal conversion
    "percentSignSuffix"     : "R",      # % suffix
    "percentWordSuffix"     : "RA",     # 'percent' suffix

    "apostropheAndS"        : "SPHR",   # ' and s
    "20AndS"                : "STH",    # 20 and s
    "19AndS"                : "STP",    # 19 and s
    "ordinalWord"           : "STA",    # ordinal + word
    "moneyAndComma"         : "TPH",    # $ and , suffix
    "periodAndPercentSign"  : "PR",     # . and %
    "periodAndPercentWord"  : "PRA",    # . and percent
    
    #available modifiers: SH, SP, SPH, STPH
    #technically all combos with A although logically I reject making them a separate concept

    #removed for now, application is too infrequent
    #"orBetween"            : "R"       # put 'or' between two single digits (word form)
}

# 2. Change the default translations of right-hand modifiers below
# Beware that these are hard-coded to only work when the number has two digits or less, and can only be combined
# with left-hand modifiers {nothing, colonPrefix}. Additionally, o'clock forces an automatic word conversion on the number.
# To change this behavior, visit lines 340-341
RIGHT_MODIFIERS = {
    ""      : "",
    "D"     : " a.m.",      # a.m. suffix
    "Z"     : " p.m.",      # p.m. suffix
    "DZ"    : " o'clock",   # o'clock suffix
}

# 3. Customize the default money symbols used for PH and PH*
MONEY_SYMBOL_1 = "$"
MONEY_SYMBOL_2 = "€"

# 4. Turn on various functions off by default

# By default, when writing two-digit numbers, the order of the digits is from left to right.
# e.g. FRB = 42, since 4 is on the first column on the left and B follows on the second column. 24 is OFRB.
# To change this behavior so that digits always follow ascending order by value, that is, FRB is 24 and OFRB is 42, switch to False.
# This will NOT change the left-to-right behavior of two-digit numbers that utilize T, TS, and S such as 82, 17, and 36.
TWO_DIGITS_LEFT_TO_RIGHT = True

# Combos of the 3 column numpad with fourth column T, TS, and S in the same row are not allowed.
# e.g. RS = 11, PBTS = 55 are invalid. To make these valid, switch to True.
TS_SAME_ROW = False

# O is used to flip the order of two digits. This is not allowed on two-digit numbers which utilize T, TS, or S
# since these two-digit numbers already contain information about the order of digits.
# e.g. Not allowed to flip BTS = 25 to OBTS = 52 since 52 is PBS.
# To allow flipping like OBTS, switch to True.
TS_FLIP = False

# From here on, no need to change the code unless you would like to dig into it further!
########################################################################################

LONGEST_KEY = 1

DIGITS = {
    #Final-side stroke mapped to digit value, column
    "R": ("1", "1"),
    "B": ("2", "2"),
    "G": ("3", "3"),
    "FR": ("4", "1"),
    "PB": ("5", "2"),
    "LG": ("6", "3"),
    "F": ("7", "1"),
    "P": ("8", "2"),
    "L": ("9", "3"),
    "E": ("0", "0"),
    "U": ("00", "0"),
    "EU": ("000", "0"),
    "T": ("789", "4"),
    "TS": ("456", "4"),
    "S": ("123", "4"),
}

def number_translator(right_stroke, Omod):
    columns = ""
    value = ""
    zeroes = ""
    
    divided = re.split(r'(E?U?)(F?R?)(P?B?)(L?G?)(T?S?)', right_stroke)

    for col in divided:
        if col: #ignore empty matches
            if DIGITS[col][1] == "0": #if in column 0 (thumb column of EU)
                zeroes += DIGITS[col][0]
            else: #concatenate by string (not int value)
                columns += DIGITS[col][1]
                value += DIGITS[col][0]
    
    if len(columns) > 2 or columns == "4": #if there are more than 2 columns used between 1234, not allowed. and if 4 is the only column between 1234, not allowed.
        raise KeyError
    elif len(columns) == 2: #two columns used, 2 digit number
        if "4" in columns: #value is a str len 4
            value = value[0] + value[int(columns[0])] #first digit plus digit in index 1, 2, or 3

            if not TS_FLIP: # false by default, no flipping allowed for 4 columns
                if int(value) % 11 == 0:
                    raise KeyError
            if not TS_SAME_ROW: #false by default
                if Omod:
                    raise KeyError  #I don't support 4th column presses that are in the same row as the other digit eg. RS. You can enable this if you wish
        
        #else value is a str len 2

        if not TWO_DIGITS_LEFT_TO_RIGHT: #true by default (skipped by default)
            if int(value[0]) > int(value[1]):
                value = value[::-1]

        if Omod: #if O pressed, flip.
            value = value[::-1]
    elif len(columns) == 1: #1 digit number
        if Omod: #if O pressed, double
            value = value + value

    #adding on zeroes happens after swapping
    value += zeroes
    
    return value

def lookup(input):
    key = input[0]
    result = ""
    use_glue = True
    default_end = True

    if key == "#":
        raise KeyError

    #convert numbered stroke into letter stroke with # in front
    if any(single_digit_number in "0123456789" for single_digit_number in key):
        key = "#" + key.replace(
            "0", "O").replace(
                "1", "S").replace(
                    "2", "T").replace(
                        "3", "P").replace(
                            "4", "H").replace(
                                "5", "A").replace(
                                    "6", "F").replace(
                                        "7", "P").replace(
                                            "8", "L").replace(
                                                "9", "T")

    match = re.fullmatch(r'#(S?T?K?P?W?H?R?A?)O?\*?-?(E?U?F?R?P?B?L?G?T?S?)(D?Z?)', key)

    # if stroke doesn't have a # character in it, it will fail
    if not match:
        raise KeyError
    
    flipper = True if "O" in key else False # Double single digit, flip two digits

    #match[2] is the number
    stroke_digits = number_translator(match[2], flipper) if match[2] else ""

    if stroke_digits != "":
        result += stroke_digits
        no_number = False
    else:
        no_number = True

    #match[1] is left modifiers
    if match[1]:
        #interpret strokes that combine two functions
        h_apostrophe = False
        h_s      = False
        h_20     = False
        h_19     = False
        h_ord    = False
        h_word   = False
        h_comma  = False
        h_money  = False
        h_nonum  = False
        h_point  = False
        h_prsign = False
        h_prword = False
        if match[1] == LEFT_MODIFIERS["apostropheAndS"]:
            h_apostrophe = True
            h_s = True
            h_nonum = True
        elif match[1] == LEFT_MODIFIERS["20AndS"]:
            h_20 = True
            h_s = True
            h_nonum = True
        elif match[1] == LEFT_MODIFIERS["19AndS"]:
            h_19 = True
            h_s = True
            h_nonum = True
        elif match[1] == LEFT_MODIFIERS["ordinalWord"]:
            h_ord = True
            h_word = True
            h_nonum = True
        elif match[1] == LEFT_MODIFIERS["moneyAndComma"]:
            h_comma = True
            h_money = True
            h_nonum = True
        elif match[1] == LEFT_MODIFIERS["periodAndPercentSign"]:
            h_point  = True
            h_prsign = True
        elif match[1] == LEFT_MODIFIERS["periodAndPercentWord"]:
            h_point  = True
            h_prword = True

        if h_nonum and no_number: #don't work if there is no number
            raise KeyError
            
        #interpret all other strokes as unique modifiers (no confusing H and PH for example), order is intentional in this section
        if match[1] == LEFT_MODIFIERS["periodPrefix"] or h_point:
            result = "." + result
        if match[1] == LEFT_MODIFIERS["commaSuffix"] or h_comma:
            result = add_commas(result, no_number)
        if match[1] == LEFT_MODIFIERS["hyphenSuffix"]:
            result += "-"
            #true prefix (add to words, or for telephone numbers)
        if match[1] == LEFT_MODIFIERS["sSuffix"] or h_s:
            result += "s"
            default_end = False
        if match[1] == LEFT_MODIFIERS["20Prefix"] or h_20:
            #personally I'd rather have an extra if else than convert to int and back to add
            if len(stroke_digits) == 2:
                result = "20" + result
                use_glue = False
                default_end = False
            elif len(stroke_digits) == 1:
                result = "200" + result
                use_glue = False
                default_end = False
            elif len(stroke_digits) == 0:
                result = "20"
            else:
                raise KeyError
        if match[1] == LEFT_MODIFIERS["19Prefix"] or h_19:
            if len(stroke_digits) == 2:
                result = "19" + result
                use_glue = False
                default_end = False
            elif len(stroke_digits) == 1:
                result = "190" + result
                use_glue = False
                default_end = False
            elif len(stroke_digits) == 0:
                result = "19"
            else:
                raise KeyError
        if match[1] == LEFT_MODIFIERS["moneyPrefix"] or h_money:
            munit = MONEY_SYMBOL_2 if "*" in key else MONEY_SYMBOL_1 # 1 is $, 2 is € by default
            if no_number:
                use_glue = False
                result += "{*(" + munit + "c)}" #includes commas which is not intended behavior; must be reprogrammed if the unit comes after the number
            else:
                result = munit + result
        if match[1] == LEFT_MODIFIERS["colonPrefix"]:
            if len(result) == 1:
                result = ":0" + result
            else:
                result = ":" + result
        if match[1] == LEFT_MODIFIERS["apostrophePrefix"] or h_apostrophe:
            #wonder if I should limit this to two digits or not or just allow user error
            result = "'" + result
        if match[1] == LEFT_MODIFIERS["ordinalSuffix"] or h_ord:
            if no_number:
                raise KeyError
            if h_word:
                use_glue = False
                result = toWords(result)
                if result.endswith("ty"):
                    result = result[:-1] + "ieth"
                elif result.endswith("one"):
                    result = result[:-3] + "first"
                elif result.endswith("two"):
                    result = result[:-3] + "second"
                elif result.endswith("three"):
                    result = result[:-5] + "third"
                elif result.endswith("ve"):
                    result = result[:-2] + "fth"
                elif result.endswith("eight"):
                    result += "h"
                elif result.endswith("nine"):
                    result = result[:-1] + "th"
                else:
                    result += "th"
            else:
                default_end = False
                if len(result) >= 1 and result[-1] == "1":
                    result += "th" if len(result) >= 2 and result[-2] == "1" else "st"
                elif len(result) >= 1 and result[-1] == "2":
                    result += "th" if len(result) >= 2 and result[-2] == "1" else "nd"
                elif len(result) >= 1 and result[-1] == "3":
                    result += "th" if len(result) >= 2 and result[-2] == "1" else "rd"
                else:
                    result += "th"
        if match[1] == LEFT_MODIFIERS["percentSignSuffix"] or h_prsign: #not court reporting canon
            result += "%"
            default_end = False
        if match[1] == LEFT_MODIFIERS["percentWordSuffix"] or h_prword:
            if result == "0":
                result = "zero"

            result += " percent"
            default_end = False
        #if match[1] == LEFT_MODIFIERS["orBetween"] or match[1] == "RA": #RA is just a safeguard for the non suggested method
        #    #check if two digits, then split, then convert to words and join with r. otherwise throw error
        #    if len(result) == 2:
        #        use_glue = False
        #        result = toWords(result[0]) + " or " + toWords(result[1])
        #    else:
        #        raise KeyError
        if match[1] == LEFT_MODIFIERS["convertToEnglishWords"]:
            use_glue = False
            result = toWords(result)

    #match[3] is right modifiers
    #only apply when digits are 2 or less
    #only work in combination with no modifier "", : "HR"
    if match[3] and len(stroke_digits) <= 2:
        if match[1] == "" or match[1] == LEFT_MODIFIERS["colonPrefix"]:
            if match[3] == "DZ": # if o'clock is used, the number should be words. CR rule but ruins total control for people who want to write 5 o'clock
                result = toWords(result)
            result += RIGHT_MODIFIERS[match[3]]
            default_end = False
        else:
            raise KeyError
    elif match[3] and len(stroke_digits) > 2:
        raise KeyError
    
    if result == "":
        raise KeyError

    if use_glue:
        result = "{&" + result + "}"
    
    if not default_end:
        result += "{}"

    return result

def add_commas(n, em):
    if em:
        return ","
    elif len(n) <= 3:
        return n + ","
    elif len(n) > 3:
        return "{:,}".format(int(n))
    else:
        return KeyError

# ---- Adapted from https://programsolve.com/python-to-convert-numbers-to-words-with-source-code/

ONE_DIGIT_WORDS = {
    "0": ["zero"],
    "1": ["one"],
    "2": ["two", "twen"],
    "3": ["three", "thir"],
    "4": ["four", "for"],
    "5": ["five", "fif"],
    "6": ["six"],
    "7": ["seven"],
    "8": ["eight"],
    "9": ["nine"],
}

TWO_DIGIT_WORDS = ["ten", "eleven", "twelve"]
HUNDRED = "hundred"
LARGE_SUM_WORDS = ["thousand", "million", "billion", "trillion", "quadrillion",
                   "quintillion", "sextillion", "septillion", "octillion", "nonillion"]

def toWords(n):
    if all(c == "0" for c in n):
        return ONE_DIGIT_WORDS["0"][0]

    word = []

    if len(n) % 3 != 0 and len(n) > 3:
        n = n.zfill(3 * (((len(n)-1) // 3) + 1))

    sum_list = [n[i:i + 3] for i in range(0, len(n), 3)]
    skip = False

    for i, num in enumerate(sum_list):
        if num != "000":
            skip = False

        for _ in range(len(num)):
            num = num.lstrip("0")
            if len(num) == 1:
                if len(word) > 0:
                    if HUNDRED in word[-1] or i == len(sum_list) - 1:
                        word.append("and")
                    elif word[-1] in LARGE_SUM_WORDS:
                        word[-1] = word[-1] + ","
                word.append(ONE_DIGIT_WORDS[num][0])
                num = num[1:]
                break

            if len(num) == 2:
                if num[0] != "0":
                    if len(word) > 0:
                        if HUNDRED in word[-1] or i == len(sum_list) - 1:
                            word.append("and")
                        elif word[-1] in LARGE_SUM_WORDS:
                            word[-1] = word[-1] + ","
                    if num.startswith("1"):
                        if int(num[1]) in range(3):
                            word.append(TWO_DIGIT_WORDS[int(num[1])])
                        else:
                            number = ONE_DIGIT_WORDS[num[1]][1 if int(
                                num[1]) in range(3, 6, 2) else 0]
                            word.append(
                                number + ("teen" if not number[-1] == "t" else "een"))
                    else:
                        word.append(ONE_DIGIT_WORDS[num[0]][1 if int(num[0]) in range(2, 6) else 0] + (
                            "ty" if num[0] != "8" else "y") + ("-" + ONE_DIGIT_WORDS[num[1]][0] if num[1] != "0" else ""))
                    break
                else:
                    num = num[1:]
                    continue

            if len(num) == 3:
                if num[0] != "0":
                    if len(word) > 0:
                        word[-1] = word[-1] + ","
                    word.append(ONE_DIGIT_WORDS[num[0]][0] + " " + HUNDRED)
                    if num[1:] == "00":
                        break
                num = num[1:]

        if len(sum_list[i:]) > 1 and not skip:
            word.append(LARGE_SUM_WORDS[len(sum_list[i:]) - 2])
            skip = True

    return " ".join(map(str.strip, word))

# --------------------------------------------
    
# not in current use

'''
ROMAN_VALUES = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
]
ROMAN_SYMBOLS = [
    'M', 'CM', 'D', 'CD',
    'C', 'XC', 'L', 'XL',
    'X', 'IX', 'V', 'IV',
    'I'
]

def toRoman(num):
    result = ''
    i = 0
    while num > 0:
        for _ in range(num // ROMAN_VALUES[i]):
            result += ROMAN_SYMBOLS[i]
            num -= ROMAN_VALUES[i]
        i += 1
    return result
'''