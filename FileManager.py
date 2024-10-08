import array
from textwrap import wrap
from InstructionCreator import InstructionCreator
from LabelManager import LabelManager

list_instructions = []


# Read in file
def read_file(filename):
    label_manager = LabelManager()
    with open(filename, "r") as F:
        for line in F:
            if len(line.strip()) > 0 and "//" not in line.strip():
                label_manager.parse_assembly_code(line.strip())
    for label in label_manager.processed_lines:
        inst = InstructionCreator(label).get_type()
        list_instructions.append(inst)
        # print(f"{label}: {inst}")


#  export file based on data sent in
def export_file(filename):
    with open(filename, "wb") as F:
        for inst in list_instructions:
            output = hex(int(inst, 2))
            output = wrap(output, 2)[::-1]
            output = f"{output[0]}{output[1]}{output[2]}{output[3]}"
            F.write(bytes.fromhex(output))
            print(' '.join(a+b for a,b in zip(output[::2], output[1::2])))
        F.close()


class App:
    def __init__(self, txt_file, output_file):
        self.txtFile = txt_file
        self.outputFile = output_file
        read_file(self.txtFile)
        export_file(self.outputFile)
