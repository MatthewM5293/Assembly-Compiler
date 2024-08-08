from Instruction import Instruction


class SingleDataTransfer(Instruction):
    def __init__(self, data):
        super().__init__()
        self.condition = super().set_condition_code(data[0])
        self.I = "0"  # Immediate offset (I)
        self.Offset = super().hex_to_binary(data[3], 12)  # Offset
        self.Rd = super().processes_register(data[1])  # Source/Destination register (Rd)
        self.Rn = super().processes_register(data[2])  # Base register (Rn)
        self.Type = data[0]
        self.L = "0"  # Load/Store bit (L)
        self.W = "0"  # Write-back bit (W)
        self.B = "0"  # Byte/Word bit (B)
        self.U = "0"  # Up/Down bit (U)
        self.P = "0"  # Pre/Post indexing bit (P)
        self.set_immediate()
        self.set_load_bit()
        self.set_ea_bits()
        self.set_write_bit(data)

    def set_immediate(self):
        if self.Offset.lstrip("0") != "":
            self.I = "0"

    def set_load_bit(self):
        if self.Type == "LDR":
            self.L = "1"

    def set_ea_bits(self):
        if self.Type == "LDREA":
            self.L = "1"
            self.P = "1"
        elif self.Type == "STREA":
            self.U = "1"

    def set_write_bit(self, data):
        if super().set_write_back_bit(data[2]):
            self.W = "1"

    def generate_binary(self):
        return f"{self.condition}01{self.I}{self.P}{self.U}{self.B}{self.W}{self.L}{self.Rn}{self.Rd}{self.Offset}"
        # 1110 011
