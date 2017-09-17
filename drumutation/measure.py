#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Measure(list):
    """Measure class."""

    def __init__(self, beats):
        """Measure constructor."""

        for b in beats:
            self.append(b)

    def ly(self):
        """Return measure using Lilypond syntax."""

        notes = [b.ly() for b in self]
        return "  " + " ".join(notes)
