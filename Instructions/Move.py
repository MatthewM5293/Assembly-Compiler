# import Instruction


class Move:
    def __init__(self, condition, movetype, Rd, offset):
        self.condition = condition  # 1110
        self.MoveType = movetype  # "0000"
        self.Imm4 = offset[:4]  # "0000"
        self.Rd = Rd  # Source/Destination register (Rd)
        self.Imm12 = offset[4:]  # "0000 0000 0000"
#
# Imm12

    def generate_binary(self):
        if self.MoveType == "MOVW":
            return f"{self.condition}00110000{self.Imm4}{self.Rd}{self.Imm12}"
        elif self.MoveType == "MOVT":
            return f"{self.condition}00110100{self.Imm4}{self.Rd}{self.Imm12}"
