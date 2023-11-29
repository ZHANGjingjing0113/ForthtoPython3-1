
import threading
import queue


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
                instruction, operand = self.program[self.state.pc]
                if instruction == 'HALT':
                    break
                if hasattr(self.state, instruction):
                    func = getattr(self.state, instruction)
                    if operand is not None:
                        func(operand)
                    else:
                        func()
                self.state.update_flags()  # Update flags after each instruction
                if instruction not in ['JMP', 'JZ', 'JNZ', 'JE', 'JNE']:
                    self.state.pc += 1  # Increment program counter if not a jump instruction
        except Exception as e:
            print(f"Error during execution: {e}")

    def display_state(self):
        print(f"Accumulator: {self.state.accumulator}")
        print(f"Program Counter: {self.state.pc}")
        print(f"Flags: {self.state.flags}")
        print(f"Memory: {self.state.memory[:10]}")  # Display first 10 memory locations


class IOThread(threading.Thread):
    def __init__(self, input_queue, output_queue):
        super().__init__()
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.running = True

    def run(self):
        try:
            while self.state.pc < len(self.program):
                instruction, operand = self.program[self.state.pc]
                if instruction == 'HALT':
                    break
                if hasattr(self.state, instruction):
                    func = getattr(self.state, instruction)
                    if operand is not None:
                        func(operand)
                    else:
                        func()
                self.state.update_flags()  # Update flags after each instruction
                # Check if the instruction is a jump instruction
                executed_jump = instruction in ['JMP', 'JZ', 'JNZ', 'JE', 'JNE']
                if not executed_jump:
                    self.state.pc += 1  # Increment program counter if not a jump instruction
        except Exception as e:
            print(f"Error during execution: {e}")

    def stop(self):
        self.running = False
        self.input_queue.put(None)  # Send sentinel value to stop the thread

# Enhancing the Machine class to include I/O operations
class EnhancedMachine(Machine):
    def __init__(self, program):
        super().__init__(program)
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        self.io_thread = IOThread(self.input_queue, self.output_queue)
        self.io_thread.start()

    def run(self):
        super().run()
        self.io_thread.stop()
        self.io_thread.join()

    def input(self, value):
        self.input_queue.put(value)

    def output(self):
        return self.output_queue.get()

