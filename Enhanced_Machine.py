
from Enhanced_ISA import MachineState

class Machine:
    def __init__(self, program):
        self.state = MachineState()
        self.program = program  # Program is a list of (instruction, operand) tuples

    def load_program(self, program):
        self.program = program

    def run(self):
        try:
            while self.state.pc < len(self.program):
                print(f"Executing PC: {self.state.pc}, Accumulator: {self.state.accumulator}")
                current_pc = self.state.pc
                instruction, operand = self.program[self.state.pc]
                print(f"Executing instruction:{instruction},Operand:{operand}")
                if instruction == 'HALT':
                    break
                if hasattr(self.state, instruction):
                    func = getattr(self.state, instruction)
                    if operand is not None:
                        func(operand)
                    else:
                        func()
                    print(f"PC: {self.state.pc}, Accumulator: {self.state.accumulator}")
                self.state.update_flags()  # Update flags after each instruction
                if self.state.pc == current_pc:
                    self.state.pc += 1
                # Check if the instruction is a jump instruction
                executed_jump = instruction in ['JMP', 'JZ', 'JNZ', 'JE', 'JNE']
                if not executed_jump:
                    self.state.pc += 1  # Increment program counter if not a jump instruction
                print(f"PC: {self.state.pc}, Accumulator: {self.state.accumulator}")
        except Exception as e:
            print(f"Error during execution: {e}")

    def display_state(self):
        print(f"Accumulator: {self.state.accumulator}")
        print(f"Program Counter: {self.state.pc}")
        print(f"Flags: {self.state.flags}")
        print(f"Memory: {self.state.memory[:10]}")  # Display first 10 memory locations
