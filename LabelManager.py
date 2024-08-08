import re


# check if there's a label in the line
# keep track of which step it's in
# return the proper offset when the end label is found

class LabelManager:
    def __init__(self):
        self.label_positions = {}
        self.processed_lines = []
        self.line_counter = 0
        self.processed_labels = set()

    def parse_assembly_code(self, data):
        # Look for start labels at the end of the line
        match = re.search(r'<([a-zA-Z_][a-zA-Z0-9_]*)', data)
        if match:
            label = match.group(1)
            if label not in self.label_positions:
                self.label_positions[label] = self.line_counter
        self.processed_lines.append(data)
        self.line_counter += 1

        for i, line in enumerate(self.processed_lines):
            matches = re.finditer(r'<([a-zA-Z_][a-zA-Z0-9_]*)', line)
            for match in matches:
                label = match.group(1)
                if label in self.label_positions and label not in self.processed_labels:
                    offset = self.label_positions[label] - i - 2
                    offset = self.int_to_hex(offset)
                    line = line.replace(f'<{label}', f'{offset}')
                    self.processed_labels.add(label)

            matches = re.finditer(r'>([a-zA-Z_][a-zA-Z0-9_]*)', line)
            for match in matches:
                label = match.group(1)
                if label in self.label_positions:
                    offset = self.label_positions[label] - i - 2
                    offset = self.int_to_hex(offset)
                    line = line.replace(f'>{label}', f'{offset}')

            self.processed_lines[i] = line

    def int_to_hex(self, n):
        return "0x" + '{:04X}'.format(n & ((1 << 24) - 1))

