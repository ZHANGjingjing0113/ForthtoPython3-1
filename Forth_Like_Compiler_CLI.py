import sys
from Enhanced_Translator import translate_program
from Enhanced_Machine import Machine

def read_program_from_console():
    print("Enter your program code (type 'END' to execute, 'EXIT' to finish):")
    program_lines = []
    while True:
        line = input()
        if line.upper() == "END":
            break
        program_lines.append(line)
    return program_lines

def main():
    while True:
        program_lines = read_program_from_console()
        # Rest of the code for processing the input
        try:
            print("Forth-Like Compiler and Machine Simulator")
            symbol_table = {}  # Placeholder for future symbol table implementation
            translated_program = translate_program(program_lines)

            for instruction, operand in translated_program:
                print(f"{instruction} {operand}")
            machine = Machine(translated_program)
            machine.run()
            machine.display_state()
            # ... Machine execution code ...
            print("\nProgram executed successfully.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
