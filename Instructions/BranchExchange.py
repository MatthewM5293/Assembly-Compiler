from Instruction import Instruction


class BranchExchange(Instruction):
    def __init__(self, data):
        super().__init__()
        self.condition = super().set_condition_code(data[0])  # Condition
        # self.Offset = data[1]  # Offset
        self.Offset = super().processes_register(data[1])  # Offset

    def generate_binary(self):
        return f"{self.condition}000100101111111111110001{self.Offset}"
