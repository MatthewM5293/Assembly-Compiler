from Instructions.Move import Move
from Instructions.DataProcessing import DataProcessing
from Instructions.SingleDataTransfer import SingleDataTransfer
from Instructions.Branch import Branch


class InstructionCreator:
    def __init__(self, data):
        self.data = data
        self.instructions = [part.strip(",()") for part in data.split(" ")]

    def get_type(self):
        result = ""
        if "MOVW" in self.instructions[0] or "MOVT" in self.instructions[0]:
            result = Move(data=self.instructions).generate_binary()
        elif any(instr in self.instructions[0] for instr in ["ADD", "SUB", "ORR", "AND"]):
            result = DataProcessing(data=self.instructions).generate_binary()
        elif "LDR" in self.instructions[0] or "STR" in self.instructions[0]:
            result = SingleDataTransfer(data=self.instructions).generate_binary()
        elif 'B' in self.instructions[0]:
            result = Branch(data=self.instructions).generate_binary()
        return result
