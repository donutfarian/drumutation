#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Score(list):
    """Score class."""

    def __init__(self, measures, time_signature="4/4", repeat=False):
        """Score constructor."""

        self.time_signature = "4/4"
        self.repeat = repeat

        for m in measures:
            self.append(m)

    def ly(self):
        """Return score using Lilypond syntax."""

        print('\\version "2.18.0"')
        print()
        print("#(define drumkey '(")
        print("  (ridecymbal    cross    #f   6)")
        print("  (crashcymbal   xcircle  #f   6)")
        print("  (splashcymbal  slash    #f   6)")
        print("  (chinesecymbal harmonic #f   6)")
        print("  (ridebell      triangle #f   6)")
        print("  (cowbell       triangle #f   3)")
        print("  (hihat         cross    #f   5)")
        print('  (closedhihat   cross "stopped"  5)')
        print('  (openhihat     cross "open"     5)')
        print('  (halfopenhihat cross "halfopen" 5)')
        print("  (pedalhihat    cross    #f  -5)")
        print("  (snare         default  #f   1)")
        print("  (sidestick     cross    #f   1)")
        print("  (lowtom        default  #f  -1)")
        print("  (hightom       default  #f   3)")
        print("  (himidtom    default  #f   2)")
        print("  (lowmidtom     default  #f   0)")
        print("  (highfloortom  default  #f  -2)")
        print("  (lowfloortom   default  #f  -4)")
        print("  (bassdrum      default  #f  -3)")
        print("))")
        print("up = \\drummode {")
        print("\\stemUp")
        print("\\override Beam #'positions = #'(5 . 5)")
        print("\n".join([m.ly() for m in self]))
        print("}")
        print()
        print("down = \\drummode {")
        print("\\override Beam #'positions = #'(-5 . -5)")
        print("}")
        print()
        print("\\score { <<")
        print("\\time", self.time_signature)
        print("  \\new DrumStaff <<")
        print("  \\set DrumStaff.drumStyleTable = #(alist->hash-table drumkey)")
        if self.repeat:
            print("\\repeat volta 2 { \\up } >>")
        else:
            print("  \\up >>")
        # print("    \\new DrumVoice { \\voiceOne \\up }")
        # print("    \\new DrumVoice { \\voiceTwo \\down }")
        # print("  >>")
        print(">> }")
