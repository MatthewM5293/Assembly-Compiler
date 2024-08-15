from Instruction import Instruction, hex_to_binary


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
        return f"{self.condition}101{self.L}{hex_to_binary(self.Offset, 24)}"
