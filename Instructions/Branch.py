from Instruction import Instruction


class Branch(Instruction):
    def __init__(self, data):
        super().__init__()
        self.condition = super().set_condition_code(data[0])  # Condition
        self.L = "0"  # LinkBit (L)
        self.Offset = super().hex_to_binary(data[1], 24)  # Offset
        self.check_linked(data[0])

    def check_linked(self, data):
        if data == "L":
            self.L = "1"

    def generate_binary(self):
        return f"{self.condition}101{self.L}{self.Offset}"
