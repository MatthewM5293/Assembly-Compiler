class SingleDataTransfer:
    def __init__(self, condition, P, U, B, W, Type, Rn, Rd, Offset):
        self.condition = condition
        self.I = "0"  # Immediate offset (I)
        self.Offset = Offset  # Offset
        self.Rd = Rd  # Source/Destination register (Rd)
        self.Rn = Rn  # Base register (Rn)
        self.Type = Type
        self.L = "0"  # Load/Store bit (L)
        self.W = W  # Write-back bit (W)
        self.B = B  # Byte/Word bit (B)
        self.U = U  # Up/Down bit (U)
        self.P = P  # Pre/Post indexing bit (P)
        self.set_immediate()
        self.set_load_bit()

    def set_immediate(self):
        if self.Offset.lstrip("0") != "":
            self.I = "1"

    def set_load_bit(self):
        if self.Type == "LDR":
            self.L = "1"
        pass

    def generate_binary(self):
        return f"{self.condition}01{self.I}{self.P}{self.U}{self.B}{self.W}{self.L}{self.Rn}{self.Rd}{self.Offset}"
