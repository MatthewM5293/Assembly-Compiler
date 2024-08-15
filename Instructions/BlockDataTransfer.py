from Instruction import Instruction, set_write_back_bit, processes_register


class BlockDataTransfer(Instruction):
    def __init__(self, data):
        super().__init__()
        self.condition = super().set_condition_code(data[0])
        self.register_list = processes_register(data[2])  # Offset
        self.Rn = processes_register(data[1])  # Base register (Rn)
        self.Type = data[0]
        self.L = "0"  # Load/Store bit (L)
        self.W = "0"  # Write-back bit (W)
        self.S = "0"  # PSR & force user bit (B)
        self.U = "0"  # Up/Down bit (U)
        self.P = "0"  # Pre/Post indexing bit (P)
        self.set_load_bit()
        self.set_write_bit(data)

    def set_load_bit(self):
        if self.Type == "LDMEA":
            self.L = "1"
            self.P = "1"
        elif self.Type == "STMEA":
            self.U = "1"

    def set_write_bit(self, data):
        if set_write_back_bit(data[1]):
            self.W = "1"

    def generate_binary(self):
        return f"{self.condition}100{self.P}{self.U}{self.S}{self.W}{self.L}{self.Rn}{self.register_list}"
