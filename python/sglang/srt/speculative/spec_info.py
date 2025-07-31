from enum import IntEnum, auto


class SpeculativeAlgorithm(IntEnum):
    NONE = auto()
    EAGLE = auto()
    EAGLE3 = auto()
    SEAGLE = auto()

    def is_none(self):
        return self == SpeculativeAlgorithm.NONE

    def is_eagle(self):
        return (
            self == SpeculativeAlgorithm.EAGLE
            or self == SpeculativeAlgorithm.EAGLE3
            or self == SpeculativeAlgorithm.SEAGLE
        )

    def is_eagle3(self):
        return self == SpeculativeAlgorithm.EAGLE3 or self == SpeculativeAlgorithm.SEAGLE

    def is_seagle(self):
        return self == SpeculativeAlgorithm.SEAGLE

    @staticmethod
    def from_string(name: str):
        name_map = {
            "EAGLE": SpeculativeAlgorithm.EAGLE,
            "EAGLE3": SpeculativeAlgorithm.EAGLE3,
            "SEAGLE": SpeculativeAlgorithm.SEAGLE,
            None: SpeculativeAlgorithm.NONE,
        }
        if name is not None:
            name = name.upper()
        return name_map[name]
