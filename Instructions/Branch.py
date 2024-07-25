from Instruction import Instruction


class Branch(Instruction):
    def __init__(self, data):
        super().__init__()
        self.branch_type = data[0]
        self.condition = super().set_condition_code(data[0])  # Condition
        self.L = "0"  # LinkBit (L)
        self.Offset = data[1]  # Offset
        self.check_linked()

    def check_linked(self):
        if "BL" in self.branch_type:
            self.L = "1"

    def generate_binary(self):
        if "BX" in self.branch_type:
            return f"{self.condition}000100101111111111110001{super().processes_register(self.Offset.strip("R"))}"
        else:
            return f"{self.condition}101{self.L}{super().hex_to_binary(self.Offset, 24)}"
