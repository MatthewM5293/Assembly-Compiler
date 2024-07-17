from Instruction import Instruction


class Move(Instruction):
    def __init__(self, movetype, imm4, rd, imm12):
        super().condition
        self.MoveType = movetype  # "0000"
        self.Imm4 = imm4  # "0000"
        self.Rd = rd  # "0000"
        self.Imm12 = imm12  # "0000 0000 0000"
# Imm4
# Source/Destination register (Rd)
# Imm12
    def __str__(self):
        result = f'{super().condition()}0011'
        if self.MoveType == "MOVT":
            result += "0100"
        elif self.MoveType == "MOVW":
            result += "0000"
        result += f"{self.Imm4}{self.Rd}{self.Imm12}"

