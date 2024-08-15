import re


def hex_to_binary(hex_value, fill):
    return bin(int(hex_value, 16))[2:].zfill(fill)


def set_write_back_bit(data):
    if '!' in data:
        return True
    else:
        return False


def processes_register(data: str):
    data = data.strip("R!")
    binary_str = ""
    if "{" not in data:
        binary_str = format(int(data), 'b').zfill(4)
        return binary_str
    else:
        index = 0
        data = data.strip("{}")
        data = data.split("-")  # data[0] (start num) data[1] (end num)
        startR = 0
        endR = 0
        if len(data) >= 2:
            for char in data:
                data[index] = char.strip("R")
                index += 1
            startR = int(data[0])
            endR = int(data[1])
        else:
            startR = 0
            endR = int(data[0])
        # process list of registers here (16 bits) starting from right to left
        while endR > startR:
            binary_str += "1"
            endR -= 1
        binary_str = binary_str.zfill(16)
    return binary_str


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
