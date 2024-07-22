import re


class Instruction:
    condition_codes = {
        "EQ": "0000", "NE": "0001", "CS": "0010", "CC": "0011", "MI": "0100",
        "PL": "0101", "VS": "0110", "VC": "0111", "HI": "1000", "LS": "1001",
        "GE": "1010", "LT": "1011", "GT": "1100", "LE": "1101", "AL": "1110"
    }

    def __init__(self):
        pass

    def set_condition_code(self, data):
        regex = r'\{(.*?)\}'
        match = re.search(regex, data)
        if match:
            return self.condition_codes.get(match.group(1), "1110")
        return "1110"

    def processes_register(self, data):
        binary_str = format(int(data), 'b').zfill(4)
        return binary_str

    def hex_to_binary(self, hex_value, fill):
        hex_value = hex_value.lstrip("0x")
        if hex_value == "":
            hex_value = "0"
        scale = 16
        return bin(int(hex_value, scale))[2:].zfill(fill)
