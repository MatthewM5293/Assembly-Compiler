import re


# check if there's a label in the line
# keep track of which step it's in
# return the proper offset when the end label is found

class LabelManager:
    def __init__(self):
        self.label_positions = {}
        self.processed_lines = []
        self.line_counter = 0

    def parse_assembly_code(self, data):
        # Look for start labels at the end of the line
        match = re.search(r'<([a-zA-Z_][a-zA-Z0-9_]*)', data)
        if match:
            label = match.group(1)
            self.label_positions[label] = self.line_counter
        self.processed_lines.append(data)
        self.line_counter += 1

        # Second pass: replace label references with calculated offsets
        for i, line in enumerate(self.processed_lines):
            # Replace start labels
            matches = re.finditer(r'<([a-zA-Z_][a-zA-Z0-9_]*)', line)
            for match in matches:
                label = match.group(1)
                if label in self.label_positions:
                    offset = self.label_positions[label] - i - 2
                    # convert number to binary
                    offset = self.int_to_hex(offset)
                    line = line.replace(f'<{label}', f'{offset}')

            # Replace end labels to point to start label offset
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

