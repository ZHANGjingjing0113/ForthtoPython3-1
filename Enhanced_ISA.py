
class MachineState:
    def __init__(self):
        self.accumulator = 0
        self.memory = [0] * 256
        self.pc = 0  # Program Counter
        self.flags = {'Z': False, 'S': False, 'O': False}  # Zero, Sign, Overflow flags
        self.stack = []
        self.tick_counter = 0

    # Existing instructions...
    def LD(self, value):
        print(f"LD before: Accumulator = {self.accumulator}")
        self.accumulator = value
        print(f"LD after: Accumulator = {self.accumulator}")

    def ST(self, address):
        self.memory[address] = self.accumulator

    # New mathematical operations
    def ADD(self, value):
        print(f"ADD before: Accumulator = {self.accumulator}")
        self.accumulator += value

        print(f"ADD after: Accumulator = {self.accumulator}")

    def SUB(self, value):
        self.accumulator -= value

    def MUL(self, value):
        self.accumulator *= value

    def DIV(self, value):
        self.accumulator //= value

    # 分支和循环指令
    def CMP(self, value):
        result = self.accumulator - value
        self.flags['Z'] = (result == 0)
        self.flags['S'] = (result < 0)

    def JMP(self, address):
        self.check_memory_address(address)
        self.pc = address

    def JZ(self, address):
        if self.flags['Z']:
            self.pc = address

    def JNZ(self, address):
        if not self.flags['Z']:
            self.pc = address

    def JE(self, address):
        if self.flags['Z']:
            self.pc = address

    def JNE(self, address):
        if not self.flags['Z']:
            self.pc = address

    #else
    def PUSH(self, value):
        self.stack.append(value)

    def POP(self):
        if not self.stack:
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def CALL(self, address):
        self.PUSH(self.pc)
        self.JMP(address)

    def RET(self):
        self.pc = self.POP()

    def INV(self):
        if self.accumulator == 0:
            raise ValueError("Division by zero")
        self.accumulator = 1 / self.accumulator
    # Method to update flags based on accumulator value
    def update_flags(self):
        self.flags['Z'] = (self.accumulator == 0)
        self.flags['S'] = (self.accumulator < 0)
        self.flags['O'] = (self.accumulator > 255 or self.accumulator < -255)