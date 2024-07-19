import re


class DataProcessing:
    condition_codes = {
        "AND": "0000", "EOR": "0001", "SUB": "0010", "RSB": "0011", "ADD": "0100",
        "ADC": "0101", "SBC": "0110", "RSC": "0111", "TST": "1000", "TEQ": "1001",
        "CMP": "1010", "CMN": "1011", "ORR": "1100", "MOV": "1101", "BIC": "1110", "MVN": "1111"
    }

    def __init__(self, condition, OpCode, Rn, Rd, Operand2):
        self.condition = condition
        self.I = "0"  # Immediate Operand (I)
        self.OpCode = OpCode  # Operation Code (OpCode)
        self.S = "0"  # Set condition codes (S)
        self.Rn = Rn  # 1st operand register (Rn)
        self.Rd = Rd  # Destination register (Rd)
        self.Operand2 = Operand2  # Operand 2
        self.set_immediate()
        self.set_condition_codes()
        self.__set_operation_code()

    def __set_operation_code(self):
        regex = r'([A-Z]+)'
        match = re.search(regex, self.OpCode)
        if match:
            self.OpCode = self.condition_codes.get(match.group(1), "0000")
        # self.OpCode = "0000"

    def set_immediate(self):
        self.Operand2.lstrip("0x")
        if self.Operand2 != "":
            self.I = "1"

    def set_condition_codes(self):
        if "{S}" in self.OpCode:
            self.S = "1"

    def generate_binary(self):
        return f"{self.condition}00{self.I}{self.OpCode}{self.S}{self.Rn}{self.Rd}{self.Operand2}"
