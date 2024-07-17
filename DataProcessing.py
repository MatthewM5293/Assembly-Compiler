from Instruction import Instruction


class DataProcessing(Instruction):
    def __init__(self):
        super().__init__()
        self.z = "00"
        self.I = "0"
        self.OpCode = "0000"
        self.S = "0"
        self.Rn = "0000"
        self.Rd = "0000"
        self.Operand2 = "0000 0000 0000"
        # Immediate Operand (I)
        # Operation Code (OpCode)
        # Set condition codes (S)
        # 1st operand register (Rn)
        # Destination register (Rd)
        # Operand 2