import re


class Instruction:
    def __init__(self, data):
        #self.condition = "AL"  # "\{(.*?)\}" # Regex for how to catch the condition code in the txt file
        self.condition = "1110"  # default
        self.data = data
        self.instructions = []
        for part in data.split(" "):
            self.instructions.append(part.strip(","))

    def create_instructions_from_data(self, data):
        for instruction in self.instructions:
            self.__get_type(instruction)

    def __set_condition_code(self, data):
        regex = r'\{(.*?)\}'
        cond = re.findall(regex, data)
        if cond == "AL":
            pass
        elif cond == "EQ":
            self.binary = "0000"
        elif cond == "NE":
            self.binary = "0001"
        elif cond == "CS":
            self.binary = "0010"
        elif cond == "CC":
            self.binary = "0011"
        elif cond == "MI":
            self.binary = "0100"
        elif cond == "PL":
            self.binary = "0101"
        elif cond == "VS":
            self.binary = "0110"
        elif cond == "VC":
            self.binary = "0111"
        elif cond == "HI":
            self.binary = "1000"
        elif cond == "LS":
            self.binary = "1001"
        elif cond == "GE":
            self.binary = "1010"
        elif cond == "LT":
            self.binary = "1011"
        elif cond == "GT":
            self.binary = "1100"
        elif cond == "LE":
            self.binary = "1101"

        # Code Sfx Flag Meaning
        # 0000 EQ Z set equal
        # 0001 NE Z clear not equal
        # 0010 CS C set unsigned higher or same
        # 0011 CC C clear unsigned lower
        # 0100 MI N set negative
        # 0101 PL N clear positive or zero
        # 0110 VS V set overflow
        # 0111 VC V clear no overflow
        # 1000 HI C set and Z clear unsigned higher
        # 1001 LS C clear or Z set unsigned lower or same
        # 1010 GE N equals V greater or equal
        # 1011 LT N not equal to V less than
        # 1100 GT Z clear AND (N equals V) greater than
        # 1101 LE Z set OR (N not equal to V) less than or equal
        # 1110 AL always

    def __get_type(self, str):
        # based on the instruction create that type and pass in the condition code
        if str == "MOVW" or str == "MOVT":
            # create Move instruction
            self.hex_to_binary(self.instructions[1])
            #Move(self.instructions[0], self.hex_to_binary(self.instructions[1]), self.hex_to_binary(self.instructions[2]))
            pass
        if '''str ==''' "ADD" in str or str == "SUB" or str == "ORR" or str == "AND":
            # create DataProcessing instruction
            pass
        if str == "STR" or str == "LDR":
            # create SingleDataTransfer instruction
            pass
        if str == "B":
            # create Branch instruction
            pass

    def hex_to_binary(self, hex):
        #Get numbers only
        hex = hex.lstrip("0x")
        scale = 16  ## equals to hexadecimal
        # num_of_bits = 8
        bin(int(hex, scale))[2:]  # .zfill(num_of_bits)
