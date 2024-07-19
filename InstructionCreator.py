import re


class InstructionCreator:
    condition_codes = {
        "EQ": "0000", "NE": "0001", "CS": "0010", "CC": "0011", "MI": "0100",
        "PL": "0101", "VS": "0110", "VC": "0111", "HI": "1000", "LS": "1001",
        "GE": "1010", "LT": "1011", "GT": "1100", "LE": "1101", "AL": "1110"
    }

    def __init__(self, data):
        self.data = data
        self.instructions = [part.strip(",") for part in data.split(" ")]
        self.condition = self.__set_condition_code(data)
        self.__create_type()

    def __set_condition_code(self, data):
        regex = r'\{(.*?)\}'
        match = re.search(regex, data)
        if match:
            return self.condition_codes.get(match.group(1), "1110")
        return "1110"

    def __create_type(self):
        if "MOVW" in self.instructions or "MOVT" in self.instructions:
            from Instructions.Move import Move
            return Move(condition=self.condition, movetype=self.instructions[0], rd = self.processes_register(self.instructions[2]), offset=self.hex_to_binary(self.instructions[3]))
        elif any(instr in self.instructions for instr in ["ADD", "SUB", "ORR", "AND"]):
            from Instructions.DataProcessing import DataProcessing
            return DataProcessing(self.instructions, self.condition, self.instructions)
        elif self.instructions in ["STR", "LDR"]:
            from Instructions.SingleDataTransfer import SingleDataTransfer
            return SingleDataTransfer(self.instructions, self.condition, self.instructions)
        elif "B" in self.instructions:
            from Instructions.Branch import Branch
            return Branch(self.instructions, self.condition, self.instructions)
        else:
            pass
            # raise ValueError(f"Unknown instruction: {instruction}")

    def processes_register(self, data):
        return self.hex_to_binary(re.findall(r'\d+', data))

    def hex_to_binary(self, hex_value):
        hex_value = hex_value.lstrip("0x")
        scale = 16
        return bin(int(hex_value, scale))[2:].zfill(16)