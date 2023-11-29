
# Function for tokenize
def tokenize(line):
    return line.strip().split()

# Function to build a symbol table with labels and their corresponding line numbers
def build_symbol_table(program_lines):
    symbol_table = {}
    line_number = 0
    for line in program_lines:
        if line.endswith(':'):  # Label definition
            label = line[:-1]  # Remove colon
            symbol_table[label] = line_number
        else:
            line_number += 1
    return symbol_table

# Function for translate_line
def translate_line(instruction, operand, symbol_table):
    if operand and operand in symbol_table:
        operand = symbol_table[operand]
    elif operand and operand.isdigit():
        operand = int(operand)
    return (instruction.upper(), operand) if operand is not None else (instruction.upper(),)

# Function for parse_line
def parse_line(line, symbol_table):
    tokens = tokenize(line)
    if not tokens or line.endswith(':'):  # Ignore label definitions
        return None, None
    instruction = tokens[0]
    operand = tokens[1] if len(tokens) > 1 else None
    return translate_line(instruction, operand, symbol_table)

# Function for translate_program
def translate_program(program_lines):
    symbol_table = build_symbol_table(program_lines)
    symbol_table = build_symbol_table(program_lines)
    translated_program = []

    for line in program_lines:
        instruction, operand = parse_line(line, symbol_table)
        if instruction is not None:
            translated_program.append((instruction, operand))

    return translated_program
