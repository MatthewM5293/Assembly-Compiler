from Instruction import Instruction


class SingleDataTransfer(Instruction):
    def __init__(self):
        super().__init__()
        self._1 = "01"
        self.I = "0"                    # Immediate offset (I)
        self.Offset = "0000 0000 0000"  # Offset
        self.Rd = "0000"                # Source/Destination register (Rd)
        self.Rn = "0000"                # Base register (Rn)
        self.L = "0"                    # Load/Store bit (L)
        self.W = "0"                    # Write-back bit (W)
        self.B = "0"                    # Byte/Word bit (B)
        self.U = "0"                    # Up/Down bit (U)
        self.P = "0"                    # Pre/Post indexing bit (P)

    def __str__(self):
        return "SingleDataTransfer"

    def to_hex(self):
        pass

    def to_reverse_hex(self):
        pass









