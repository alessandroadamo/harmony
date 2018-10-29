import numpy as np


class Harmonizer():
    __notes = ["C", "Db", "D", "Eb", "E", "F",
               "Gb", "G", "Ab", "A", "Bb", "B"]

    __major = [0, 2, 4, 5, 7, 9, 11]
    __melodic = [0, 2, 3, 5, 7, 9, 11]
    __harmonic_minor = [0, 2, 3, 5, 7, 8, 11]
    __harmonic_major = [0, 2, 4, 5, 7, 8, 11]
    __double_harmonic = [0, 1, 4, 5, 7, 8, 11]

    __modes = {

        "major": __major,
        "ionian": __major,
        "dorian": __major[1:] + __major[:1],
        "phrigian": __major[2:] + __major[:2],
        "lydian": __major[3:] + __major[:3],
        "mixolydian": __major[4:] + __major[:4],
        "aeolian": __major[5:] + __major[:5],
        "natural minor": __major[5:] + __major[:5],
        "locrian": __major[6:] + __major[:6],

        "melodic minor": __melodic,
        "dorian #7": __melodic,
        "phrigian #6": __melodic[1:] + __melodic[:1],
        "lydian #5": __melodic[2:] + __melodic[:2],
        "mixolydian #4": __melodic[3:] + __melodic[:3],
        "aeolian #3": __melodic[4:] + __melodic[:4],
        "locrian #2": __melodic[5:] + __melodic[:5],
        "ionian #1": __melodic[6:] + __melodic[:6],

        "harmonic minor": __harmonic_minor,
        "aeolian #7": __harmonic_minor,
        "locrian #6": __harmonic_minor[1:] + __harmonic_minor[:1],
        "ionian #5": __harmonic_minor[2:] + __harmonic_minor[:2],
        "dorian #4": __harmonic_minor[3:] + __harmonic_minor[:3],
        "phrygian #3": __harmonic_minor[4:] + __harmonic_minor[:4],
        "lydian #2": __harmonic_minor[5:] + __harmonic_minor[:5],
        "mixolydian #1": __harmonic_minor[6:] + __harmonic_minor[:6],

        "harmonic major": __harmonic_major,
        "ionian b6": __harmonic_major,
        "dorian b5": __harmonic_major[1:] + __harmonic_major[:1],
        "phrigian b4": __harmonic_major[2:] + __harmonic_major[:2],
        "lydian b3": __harmonic_major[3:] + __harmonic_major[:3],
        "mixolydian b2": __harmonic_major[4:] + __harmonic_major[:4],
        "lydian augmented #2": __harmonic_major[5:] + __harmonic_major[:5],
        "locrian bb7": __harmonic_major[6:] + __harmonic_major[:6],

        "double harmonic": __double_harmonic,
        "lydian #2 #6": __double_harmonic[1:] + __double_harmonic[:1],
        "phrygian b4 bb7": __double_harmonic[2:] + __double_harmonic[:2],
        "Lydian #3 #6": __double_harmonic[3:] + __double_harmonic[:3],
        "mixolydian b2 b5": __double_harmonic[4:] + __double_harmonic[:4],
        "ionian #2 #5": __double_harmonic[5:] + __double_harmonic[:5],
        "locrian bb3 bb7": __double_harmonic[6:] + __double_harmonic[:6]

    }

    def __init__(self,
                 root="C",
                 mode="major"):

        assert root in self.__notes
        assert mode in self.__modes.keys()

        self.root = root
        self.mode = mode

    def get_scale(self):
        """
        Get the specified scale from a specified root.

        :return: scale array
        """

        root_idx = self.__notes.index(self.root)
        scale = [self.__notes[(root_idx + i) % 12] for i in self.__modes[self.mode]]
        scale.append(scale[0])

        return scale

    def get_intervals(self):
        """

        :return:
        """
        scale_idx = [x if x >= 0 else (12 + x) for x in
                     [(x - self.__modes[self.mode][0]) for x in self.__modes[self.mode]]]
        scale_idx.append(scale_idx[0] + 12)

        def check_interval(x):
            swt = {
                1: "S",
                2: "T",
                3: "T1/2"
            }
            return swt.get(x, "Invalid interval")

        scale_int = [check_interval(x) for x in np.diff(scale_idx)]

        return scale_int

    def __check_chord(self, root, x):

        if len(x) == 4:

            ####################### Maj7 ##############################

            if x[0] == 0 and x[1] == 4 and x[2] == 7 and x[3] == 11:
                return root + " Maj7"

            if x[0] == 4 and x[1] == 7 and x[2] == 11 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 4) % 12]
                return root + "/" + drop + " Maj7"

            if x[0] == 7 and x[1] == 11 and x[2] == 0 and x[3] == 4:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " Maj7"

            if x[0] == 11 and x[1] == 0 and x[2] == 4 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 11) % 12]
                return root + "/" + drop + " Maj7"

            ###################### Maj7(#5) ###########################

            if x[0] == 0 and x[1] == 4 and x[2] == 8 and x[3] == 11:
                return root + " Maj7(#5)"

            if x[0] == 4 and x[1] == 8 and x[2] == 11 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 4) % 12]
                return root + "/" + drop + " Maj7(#5)"

            if x[0] == 8 and x[1] == 11 and x[2] == 0 and x[3] == 4:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 8) % 12]
                return root + "/" + drop + " Maj7(#5)"

            if x[0] == 11 and x[1] == 0 and x[2] == 4 and x[3] == 8:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 11) % 12]
                return root + "/" + drop + " Maj7(#5)"

            ########################## 7 ##############################

            if x[0] == 0 and x[1] == 4 and x[2] == 7 and x[3] == 10:
                return root + " 7"

            if x[0] == 4 and x[1] == 7 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 4) % 12]
                return root + "/" + drop + " 7"

            if x[0] == 7 and x[1] == 10 and x[2] == 0 and x[3] == 4:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " 7"

            if x[0] == 10 and x[1] == 0 and x[2] == 4 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + " 7"

            ########################## 7(b5 ##############################

            if x[0] == 0 and x[1] == 4 and x[2] == 6 and x[3] == 10:
                return root + " 7(b5)"

            if x[0] == 4 and x[1] == 6 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 4) % 12]
                return root + "/" + drop + " 7(b5)"

            if x[0] == 6 and x[1] == 10 and x[2] == 0 and x[3] == 4:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " 7(b5)"

            if x[0] == 10 and x[1] == 0 and x[2] == 4 and x[3] == 6:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + " 7(b5)"

            ########################## sus2 ###########################

            if x[0] == 0 and x[1] == 2 and x[2] == 7 and x[3] == 10:
                return root + " sus2"

            if x[0] == 2 and x[1] == 7 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 2) % 12]
                return root + "/" + drop + " sus2"

            if x[0] == 7 and x[1] == 10 and x[2] == 0 and x[3] == 2:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " sus2"

            if x[0] == 10 and x[1] == 0 and x[2] == 2 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + " sus2"

            ########################## sus2 6 ###########################

            if x[0] == 0 and x[1] == 2 and x[2] == 7 and x[3] == 9:
                return root + " sus2 6"

            if x[0] == 2 and x[1] == 7 and x[2] == 9 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 2) % 12]
                return root + "/" + drop + " sus2 6"

            if x[0] == 7 and x[1] == 9 and x[2] == 0 and x[3] == 2:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " sus2 6"

            if x[0] == 9 and x[1] == 0 and x[2] == 2 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 9) % 12]
                return root + "/" + drop + " sus2 6"

            ########################## sus2(b5) ###########################

            if x[0] == 0 and x[1] == 2 and x[2] == 6 and x[3] == 10:
                return root + " sus2(b5)"

            if x[0] == 2 and x[1] == 6 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 2) % 12]
                return root + "/" + drop + " sus2(b5)"

            if x[0] == 6 and x[1] == 10 and x[2] == 0 and x[3] == 2:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 6) % 12]
                return root + "/" + drop + " sus2(b5)"

            if x[0] == 10 and x[1] == 0 and x[2] == 2 and x[3] == 6:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + " sus2(b5)"

            ########################## sus2 6(b5) ###########################

            if x[0] == 0 and x[1] == 2 and x[2] == 6 and x[3] == 9:
                return root + " sus2 6(b5)"

            if x[0] == 2 and x[1] == 6 and x[2] == 9 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 2) % 12]
                return root + "/" + drop + " sus2 6(b5)"

            if x[0] == 6 and x[1] == 9 and x[2] == 0 and x[3] == 2:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 6) % 12]
                return root + "/" + drop + " sus2 6(b5)"

            if x[0] == 9 and x[1] == 0 and x[2] == 2 and x[3] == 6:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 9) % 12]
                return root + "/" + drop + " sus2 6(b5)"

            ########################## sus7 ###########################

            if x[0] == 0 and x[1] == 5 and x[2] == 7 and x[3] == 10:
                return root + " sus7"

            if x[0] == 5 and x[1] == 7 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 5) % 12]
                return root + "/" + drop + " sus7"

            if x[0] == 7 and x[1] == 10 and x[2] == 0 and x[3] == 5:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " sus7"

            if x[0] == 10 and x[1] == 0 and x[2] == 5 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + " sus7"

            ########################## sus7(b5) ###########################

            if x[0] == 0 and x[1] == 5 and x[2] == 6 and x[3] == 10:
                return root + " sus7(b5)"

            if x[0] == 5 and x[1] == 6 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 5) % 12]
                return root + "/" + drop + " sus7(b5)"

            if x[0] == 6 and x[1] == 10 and x[2] == 0 and x[3] == 5:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 6) % 12]
                return root + "/" + drop + " sus7(b5)"

            if x[0] == 10 and x[1] == 0 and x[2] == 5 and x[3] == 6:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + " sus7(b5)"

            ########################## sus6 ###########################

            if x[0] == 0 and x[1] == 5 and x[2] == 7 and x[3] == 9:
                return root + " sus6"

            if x[0] == 5 and x[1] == 7 and x[2] == 9 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 5) % 12]
                return root + "/" + drop + " sus6"

            if x[0] == 7 and x[1] == 9 and x[2] == 0 and x[3] == 5:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " sus6"

            if x[0] == 9 and x[1] == 0 and x[2] == 5 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 9) % 12]
                return root + "/" + drop + " sus6"

            ########################## sus6(b5) ###########################

            if x[0] == 0 and x[1] == 5 and x[2] == 6 and x[3] == 9:
                return root + " sus6(b5)"

            if x[0] == 5 and x[1] == 6 and x[2] == 9 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 5) % 12]
                return root + "/" + drop + " sus6(b5)"

            if x[0] == 6 and x[1] == 9 and x[2] == 0 and x[3] == 5:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 6) % 12]
                return root + "/" + drop + " sus6(b5)"

            if x[0] == 9 and x[1] == 0 and x[2] == 5 and x[3] == 6:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 9) % 12]
                return root + "/" + drop + " sus6(b5)"

            ########################## 6 ##############################

            if x[0] == 0 and x[1] == 4 and x[2] == 7 and x[3] == 9:
                return root + "6"

            if x[0] == 4 and x[1] == 7 and x[2] == 9 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 4) % 12]
                return root + "/" + drop + "6"

            if x[0] == 7 and x[1] == 9 and x[2] == 0 and x[3] == 4:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + "6"

            if x[0] == 9 and x[1] == 0 and x[2] == 4 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 9) % 12]
                return root + "/" + drop + "6"

            ########################## min(Maj7) ######################

            if x[0] == 0 and x[1] == 3 and x[2] == 7 and x[3] == 11:
                return root + " min(Maj7)"

            if x[0] == 3 and x[1] == 7 and x[2] == 11 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 3) % 12]
                return root + "/" + drop + " min(Maj7)"

            if x[0] == 7 and x[1] == 11 and x[2] == 0 and x[3] == 3:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + " min(Maj7)"

            if x[0] == 11 and x[1] == 0 and x[2] == 3 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 11) % 12]
                return root + "/" + drop + " min(Maj7)"

            ########################## min7 ###########################

            if x[0] == 0 and x[1] == 3 and x[2] == 7 and x[3] == 10:
                return root + " min7"

            if x[0] == 3 and x[1] == 7 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 3) % 12]
                return root + "/" + drop + "min7"

            if x[0] == 7 and x[1] == 10 and x[2] == 0 and x[3] == 3:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + "min7"

            if x[0] == 10 and x[1] == 0 and x[2] == 3 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + "min7"

            ########################## min6 ###########################

            if x[0] == 0 and x[1] == 3 and x[2] == 7 and x[3] == 9:
                return root + " min6"

            if x[0] == 3 and x[1] == 7 and x[2] == 9 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 3) % 12]
                return root + "/" + drop + "min6"

            if x[0] == 7 and x[1] == 9 and x[2] == 0 and x[3] == 3:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 7) % 12]
                return root + "/" + drop + "min6"

            if x[0] == 9 and x[1] == 0 and x[2] == 3 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 9) % 12]
                return root + "/" + drop + "min6"

            ########################## min7(b5) #######################

            if x[0] == 0 and x[1] == 3 and x[2] == 6 and x[3] == 10:
                return root + " min7(b5)"

            if x[0] == 3 and x[1] == 6 and x[2] == 10 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 3) % 12]
                return root + "/" + drop + " min7(b5)"

            if x[0] == 6 and x[1] == 10 and x[2] == 0 and x[3] == 3:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 6) % 12]
                return root + "/" + drop + " min7(b5)"

            if x[0] == 10 and x[1] == 0 and x[2] == 3 and x[3] == 6:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 10) % 12]
                return root + "/" + drop + " min7(b5)"

            ########################## dim7 #######################

            if x[0] == 0 and x[1] == 3 and x[2] == 6 and x[3] == 9:
                return root + " dim7"

            if x[0] == 3 and x[1] == 6 and x[2] == 9 and x[3] == 0:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 3) % 12]
                return root + "/" + drop + " dim7"

            if x[0] == 6 and x[1] == 9 and x[2] == 0 and x[3] == 3:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 6) % 12]
                return root + "/" + drop + " dim7"

            if x[0] == 9 and x[1] == 0 and x[2] == 3 and x[3] == 7:
                root_idx = self.__notes.index(root)
                drop = self.__notes[(root_idx + 9) % 12]
                return root + "/" + drop + " dim7"

        return "NA"

    def check_chord(self, root, x):
        """

        :param root:
        :param x:
        :return:
        """
        return self.__check_chord(root, x)

    def harmonize(self):
        """

        :return:
        """
        sc = self.get_scale()
        sc = sc[:-1]

        h = []
        for i, x in enumerate(sc):
            chrd = [sc[y] for y in [i, (i + 2) % len(sc), (i + 4) % len(sc), (i + 6) % len(sc)]]
            root = chrd[0]
            idx = [self.__notes.index(c) for c in chrd]
            idx = [c if c >= 0 else (12 + c) for c in [(c - idx[0]) for c in idx]]

            h.append({ self.__check_chord(root, idx): chrd })

        return h

    def modes(self):
        return self.__modes.keys()

    def modes(self):
        return self.__modes.keys()


if __name__ == "__main__":
    h = Harmonizer(root="C", mode="harmonic minor")

    m = h.modes()
    s = h.get_scale()

    hh = h.harmonize()
    print(hh)

