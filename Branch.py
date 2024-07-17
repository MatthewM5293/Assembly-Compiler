from Instruction import Instruction


class Branch(Instruction):
    def __init__(self):
        super().__init__()
        self._101 = '101'
        self.L = '0'                                    # LinkBit (L)
        self.Offset = "0000 0000 0000 0000 0000 0000"   # Offset

    def __str__(self):
        return self.condition + self._101 + self.L + self.Offset
