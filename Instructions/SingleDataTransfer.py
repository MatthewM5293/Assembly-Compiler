from Instruction import Instruction


class SingleDataTransfer(Instruction):
    def __init__(self, data):
        super().__init__()
        self.condition = super().set_condition_code(data[0])
        self.I = "0"  # Immediate offset (I)
        self.Offset = "000000000000"  # Offset
        self.Rd = super().processes_register(data[1].strip("R"))  # Source/Destination register (Rd)
        self.Rn = super().processes_register(data[2].strip("R"))  # Base register (Rn)
        self.Type = data[0]
        self.L = "0"  # Load/Store bit (L)
        self.W = "0"  # Write-back bit (W)
        self.B = "0"  # Byte/Word bit (B)
        self.U = "0"  # Up/Down bit (U)
        self.P = "0"  # Pre/Post indexing bit (P)
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
