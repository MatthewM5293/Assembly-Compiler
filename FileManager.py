from Instruction import Instruction

list_instructions = []


# Read in file
def read_file(filename):
    with open(filename, "r") as F:
        for line in F:
            print(line)
            # convert read lines into a list of instructions
            inst = Instruction(line.rstrip())
            list_instructions.append(inst)


#  export file based on data sent in
def export_file(filename):
    with open(filename, "wb") as F:
        for inst in list_instructions:
            F.write(inst)
            F.close()
