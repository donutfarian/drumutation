# drumutation

Create [LilyPond][1] sheet music for drum permutations.

Usage
-----

    usage: drumutation [-h] [--key] [--nsub NSUB] [--nbeat NBEAT] [--nbar NBAR] [-s STICKS] [drums [drums ...]]

    Create LilyPond sheet music for drum  permutation.

    positional arguments:
      drums                 drum elements to permute

    optional arguments:
      -h, --help            show this help message and exit
      --key                 drum notation key
      --nsub NSUB           number of subdivisions
      --nbeat NBEAT         number of beats
      --nbar NBAR           number of bars (measures)
      -s STICKS, --sticking STICKS
                            drum sticking elements to permute

Example: Stick Control
----------------------

The first few pages (5-7) of George Lawrence Stone's *Stick Control:
For the Snare Drummer* are permutations of two bar, right (R) and left
(L) hand sticking patterns over 16th notes.

These exercises can be generated using the following command.

    $ drumutation --nsub 4 --nbeat 2 --sticking RL sn sn > stick-control.ly

* `--nsub 4`: The subdivision of each beat (pulse) is 4, i.e., 16th notes
* `--nbeat 2`: Find all two beat permutations (eight 16th notes)
* `--sticking RL sn sn`: Permutate the snare (sn) with R and L hand sticking combinations

There are 256 possible two bar patterns. Drumutation outputs
[LilyPond][1] sheet music that can be rendered using

    $ lilypond stick-control.ly

The output is the seven page PDF [stick-control.pdf](docs/stick-control.pdf).



## Drum Elements

The following drum elements can be permuted. The syntax mostly follows
[LilyPond's percussion notation][2].

![Drum Notation Key](docs/key.svg)

Symbol | Description
-------|------------
 sn    | Snare
 sa    | Snare Accent
 sg    | Snare Ghost Note
 ss    | Snare Side Stick (Cross Stick)
 hh    | Hi-Hat
 hhc   | Hi-Hat Closed
 hho   | Hi-Hat Open
 hhho  | Hi-Hat Half-Open
 cymr  | Ride Cymbal
 rb    | Ride Bell
 bd    | Bass Drum
 bd2   | Bass Drum 2
 hhp   | Hi-Hat Pedal (*chick*)
 hhs   | Hi-Hat Splash
 t1    | Rack Tom
 t2    | Floor Tom
 t3    | High Rack Tom
 t4    | Low Rack Tom
 t5    | Floor Tom
 cymc  | Crash Cymbal
 cyms  | Splash Cymbal
 cymch | China Cymbal
 cb    | Cowbell

A four piece drum kit is usually notated using `t1` and `t2`, and a
five piece kit with `t3`, `t4`, and `t5`.

License
-------

[MIT](LICENSE)


[1]: http://lilypond.org/
[2]: http://lilypond.org/doc/v2.18/Documentation/notation/common-notation-for-percussion
