import json
from red_n import *
from itertools import combinations

digitfield = "EUFRPBLGTS"

DIGITSTENOS = [""] + list("".join(i) for i in combinations(digitfield, 1)) + list("".join(i) for i in combinations(digitfield, 2)) + list("".join(i) for i in combinations(digitfield, 3)) + list("".join(i) for i in combinations(digitfield, 4)) + list("".join(i) for i in combinations(digitfield, 5)) + list("".join(i) for i in combinations(digitfield, 6))

newdict = {}

for function in LEFT_MODIFIERS:
    modifier = LEFT_MODIFIERS[function]
    modifier = modifier + "-"
    for ending in RIGHT_MODIFIERS:
        for digits in DIGITSTENOS:
            steno = "#" + modifier+digits+ending

            #no o version
            if any(char in steno for char in 'AO*EU') or steno == "#-":
                steno = steno.replace('-', '')

            try:
                newdict[steno] = lookup([steno,])
            except KeyError:
                pass

            #o version
            match = re.fullmatch(r'(#S?T?K?P?W?H?R?A?)(\*?-?E?U?F?R?P?B?L?G?T?S?D?Z?)', steno)

            if digits != "" and digits != "E" and digits != "EU" and digits != "U":
                steno = match[1] + "O" + match[2].replace('-', '')

                try:
                    newdict[steno] = lookup([steno,])
                except KeyError:
                    pass

with open("red-numbers.json", "w") as outfile:
    json.dump(newdict, outfile, indent=0)