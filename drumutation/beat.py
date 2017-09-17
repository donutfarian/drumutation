#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Lilypond note dictionary
_NOTES_ly = {
    "sn": "sn",            # snare (snare)
    "sa": "sn->",          # snare accent
    "sg": "\parenthesize sn",  # snare ghost note
    "ss": "ss",            # snare cross stick (sidestick)

    "hh": "hh",            # hi-hat (hihat)
    "hhc": "hhc",          # hi-hat closed (closedhihat)
    "hho": "hho",          # hi-hat open (openhihat)
    "hhho": "hhho",        # hi-hat half-open (halfopenhihat)
    "hhp": "hhp",          # hi-hat pedal (pedalhihat)
    "hhs": "hhp_\open",    # hi-hat splash

    "bd": "bd",            # bass drum (bassdrum)
    "bd2": "tomfl",        # bass drum 2 (lowfloortom)

# 4 piece kit
    "t1": "tomh",          # high rack tom (hightom)
    "t2": "toml",          # floor tom (lowtom)
# 5 piece kit
    "t3": "tommh",         # high rack tom (himidtom)
    "t4": "tomml",         # low rack tom (lowmidtom)
    "t5": "tomfh",         # high floor tom (highfloortom)

    "cymr": "cymr",        # ride (ridecymbal)
    "rb": "rb",            # ride bell (ridebell)
    "cymc": "cymc",        # crash (crashcymbal)
    "cyms": "cyms",        # splash (splashcymbal)
    "cymch": "cymch",      # china (chinesecymbal)
    "cb": "cb",            # cow bell (cowbell)

    "s": "s",              # space
    "r": "r"               # rest
}

class Beat(list):
    """Beat class."""

    def __init__(self, notes, sticking=None):
        """Beat constructor."""

        self.subdivision = len(notes)
        self.sticking = sticking if sticking else [None]*len(notes)

        for n in notes:
            self.append(n)

    def ly(self):
        """Return beat using Lilypond syntax."""

        notes = []
        for n, s in zip(self, self.sticking):
            if s:
                notes.append('{0}^"{1}"'.format(_NOTES_ly[n], s))
            else:
                notes.append(_NOTES_ly[n])

        if self.subdivision == 1:    # quarter notes
            x = "{0[0]}4".format(notes)

        elif self.subdivision == 2:  # eighth notes
            x = "{0[0]}8 {0[1]}8".format(notes)

        elif self.subdivision == 3:  # eighth note triplets
            if notes == ["r", "r", "r"]:
                x = "r4"
            elif notes[1:] == ["r", "r"]:
                x = "{0[0]}4".format(notes)
            else:
                x = "\\tuplet 3/2 {" + "{0[0]}8 {0[1]}8 {0[2]}8".format(notes) + "}"

        elif self.subdivision == 4:  # sixteenth notes
            if notes == ["r", "r", "r", "r"]:
                x = "r4"
            elif notes[0:3] == ["r", "r", "r"]:
                x = "r8." + "{}16".format(notes[3])
            elif notes[1:] == ["r", "r", "r"]:
                x = "{}16".format(notes[0]) + "r8."
            elif notes[0:2] == ["r", "r"]:
                x = "r8" + "{0[2]}16 {0[3]}16".format(notes)
            elif notes[2:] == ["r", "r"]:
                x = "{0[0]}16 {0[1]}16".format(notes) + "r8"
            else:
                x = "{0[0]}16 {0[1]}16 {0[2]}16 {0[3]}16".format(notes)
        else:
            raise AssertionError("subdivision not implemented")

        # correct accent and sticking placement
        x = re.sub(r'->(\^".*?")(\d+)', r"\2->\1", x)
        x = re.sub(r"->(\d+)", r"\1->", x)
        x = re.sub(r'(\^".*?")(\d+)', r"\2\1", x)
        x = re.sub(r'hhp_\\open(\d+)', r"hhp\1_\open", x)


        return x
