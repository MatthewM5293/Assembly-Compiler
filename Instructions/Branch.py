class Branch:
    def __init__(self, condition, L, Offset):
        self.condition = condition  # Condition
        self.L = L  # LinkBit (L)
        self.Offset = Offset  # Offset

    def generate_binary(self):
        return f"{self.condition}101{self.L}{self.Offset}"
