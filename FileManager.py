import array
from textwrap import wrap

from InstructionCreator import InstructionCreator

list_instructions = []


# Read in file
def read_file(filename):
    with open(filename, "r") as F:
        for line in F:
            if len(line.strip()) > 0:
                inst = InstructionCreator(line.rstrip()).get_type()
                list_instructions.append(inst)
                # print(f"{line} :  {inst}")


#  export file based on data sent in
def export_file(filename):
    with open(filename, "wb") as F:
        for inst in list_instructions:
            output = hex(int(inst, 2))
            output = wrap(output, 2)[::-1]
            output = f"{output[0]}{output[1]}{output[2]}{output[3]}"
            F.write(bytes.fromhex(output))
        F.close()

