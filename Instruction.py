import re


class Instruction:
    condition_codes = {
        "EQ": "0000", "NE": "0001", "CS": "0010", "CC": "0011", "MI": "0100",
        "PL": "0101", "VS": "0110", "VC": "0111", "HI": "1000", "LS": "1001",
        "GE": "1010", "LT": "1011", "GT": "1100", "LE": "1101", "AL": "1110"
    }

    def __init__(self, data):
        self.data = data
        self.instructions = [part.strip(",()") for part in data.split(" ")]
        self.condition = self.__set_condition_code(data)

    def __set_condition_code(self, data):
        regex = r'\{(.*?)\}'
        match = re.search(regex, data)
        if match:
            return self.condition_codes.get(match.group(1), "1110")
        return "1110"

    def get_type(self):
        result = ""
        if "MOVW" in self.instructions[0] or "MOVT" in self.instructions[0]:
            from Instructions.Move import Move
            result = Move(condition=self.condition, movetype=self.instructions[0], Rd=self.processes_register(self.instructions[1].strip("R")), offset=self.hex_to_binary(self.instructions[2], 16)).generate_binary()
        elif any(instr in self.instructions[0] for instr in ["ADD", "SUB", "ORR", "AND"]):
            from Instructions.DataProcessing import DataProcessing
            result = DataProcessing(condition=self.condition, OpCode=self.instructions[0], Rn=self.processes_register(self.instructions[2].strip("R")), Rd=self.processes_register(self.instructions[1].strip("R")), Operand2=self.hex_to_binary(self.instructions[3], 12)).generate_binary()
        elif "LDR" in self.instructions[0] or "STR" in self.instructions[0]:
            from Instructions.SingleDataTransfer import SingleDataTransfer
            result = SingleDataTransfer(condition=self.condition, P=0, U=0, B=0, W=0, L=0, Rn=self.processes_register(self.instructions[2].strip("R")), Rd=self.processes_register(self.instructions[1].strip("R")), Offset="000000000000").generate_binary()
        elif 'B' in self.instructions[0]:
            from Instructions.Branch import Branch
            result = Branch(condition=self.condition,L=0, Offset=self.hex_to_binary(self.instructions[1], 24)).generate_binary()
        return result

    def processes_register(self, data):
        binary_str = format(int(data), 'b').zfill(4)
        return binary_str

    def hex_to_binary(self, hex_value, fill):
        hex_value = hex_value.lstrip("0x")
        if hex_value == "":
            hex_value = "0"
        scale = 16
        return bin(int(hex_value, scale))[2:].zfill(fill)
