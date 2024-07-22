from Instruction import Instruction


class Move(Instruction):
    def __init__(self, data):
        super().__init__()
        self.Offset = super().hex_to_binary(data[2], 16)
        self.condition = super().set_condition_code(data[0])  # 1110
        self.MoveType = data[0]  # "0000"
        self.Imm4 = self.Offset[:4]  # "0000"
        self.Rd = super().processes_register(data[1].strip("R"))  # Source/Destination register (Rd)
        self.Imm12 = self.Offset[4:]  # "0000 0000 0000"
#
# Imm12

    def generate_binary(self):
        if self.MoveType == "MOVW":
            return f"{self.condition}00110000{self.Imm4}{self.Rd}{self.Imm12}"
        elif self.MoveType == "MOVT":
            return f"{self.condition}00110100{self.Imm4}{self.Rd}{self.Imm12}"
