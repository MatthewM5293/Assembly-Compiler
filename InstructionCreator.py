from Instructions.Move import Move
from Instructions.DataProcessing import DataProcessing
from Instructions.SingleDataTransfer import SingleDataTransfer
from Instructions.Branch import Branch
from Instructions.BranchExchange import BranchExchange


class InstructionCreator:
    def __init__(self, data):
        self.data = data
        self.instructions = [part.strip(",()") for part in data.split(" ")]

    def get_type(self):
        result = ""
        if "MOV" in self.instructions[0]:
            result = Move(data=self.instructions).generate_binary()
        elif any(instr in self.instructions[0] for instr in ["ADD", "SUB", "ORR", "AND"]):
            result = DataProcessing(data=self.instructions).generate_binary()
        elif any(instr in self.instructions[0] for instr in ["LDR", "STR"]):
            result = SingleDataTransfer(data=self.instructions).generate_binary()
        elif 'BX' in self.instructions[0]:
            result = BranchExchange(data=self.instructions).generate_binary()
        elif any(instr in self.instructions[0] for instr in ["B", "BL"]):
            result = Branch(data=self.instructions).generate_binary()
        return result
