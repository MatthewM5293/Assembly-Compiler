class SingleDataTransfer:
    def __init__(self, condition, P, U, B, W, L, Rn, Rd, Offset):
        self.condition = condition
        self.I = "0"  # Immediate offset (I)
        self.Offset = Offset  # Offset
        self.Rd = Rd  # Source/Destination register (Rd)
        self.Rn = Rn  # Base register (Rn)
        self.L = L  # Load/Store bit (L)
        self.W = W  # Write-back bit (W)
        self.B = B  # Byte/Word bit (B)
        self.U = U  # Up/Down bit (U)
        self.P = P  # Pre/Post indexing bit (P)

    def set_immediate(self):
        self.Offset.lstrip("0x")
        if self.Offset != "":
            self.I = "1"

    def generate_binary(self):
        return f"{self.condition}01{self.I}{self.P}{self.U}{self.B}{self.W}{self.L}{self.Rn}{self.Rd}{self.Offset}"
