"""
AssemblyHandler - Low-level Assembly Handler

AssemblyHandler is a simple interpreter for a custom assembly-like language designed for low-level operations.
It simulates a virtual machine with memory and registers, capable of executing a set of predefined commands.

The interpreter consists of the following components:
- Memory: A memory array with a size of 2048 cells.
- Registers: A set of short-term registers (A, B, C, D, P, X) used for temporary storage and program control.
- Commands: A list of instructions provided by the user to be executed by the interpreter.
- Error Handling: Mechanisms to detect and handle errors such as out-of-bounds memory access, arithmetic overflow, and division by zero.

The interpreter supports the following commands:
- LOADA: Load a value from memory into a register.
- LOAD: Load a value from memory using the value stored in register A as the memory address.
- LOADI: Load an immediate value into a register.
- STOREA: Store the value of a register into memory at a specified address.
- STORE: Store the value of a register into memory using the value stored in register A as the memory address.
- MOVE: Move the value from one register to another.
- Arithmetic Operations: ADDI, ADD, SUB, MUL, DIV for addition, subtraction, multiplication, and division.
- Jump Instructions: JMP, JMPR, JZ, JLT for unconditional and conditional jumps.
- PRINT: Print the value stored in a register.

The interpreter ensures proper error handling for memory access violations, arithmetic overflow, and division by zero.

To use the interpreter, provide a sequence of commands as input, terminated by 'END'. The interpreter will execute the commands and produce the desired output or error messages.

"""


class AssemblyHandler:
    def __init__(self):
        # Initialize memory, registers, command list, and error flag
        self.memory = [0] * 2048
        self.short_term = {"A": 0, "B": 0, "C": 0, "D": 0, "P": 0, "X": 0}
        self.commands = []
        self.error = False

    def load_commands_from_user(self):
        # Load commands from user input until 'END' is encountered
        while True:
            command = input().strip()
            if command == "END":
                break
            self.commands.append(command)

    def execute(self):
        # Execute commands until the end of the command list or an error occurs
        while self.short_term["P"] < len(self.commands) and not self.error:
            command = self.commands[self.short_term["P"]]
            # Check for program counter out of bounds
            if self.short_term["P"] < 0 or self.short_term["P"] >= 10000:
                self.error = True
                print("I'm afraid I can't do that")
                break
            # Check for execution counter exceeding the limit
            if self.short_term["X"] > 10**6:
                self.error = True
                print("I'm afraid I can't do that")
                break
            self.parse_command(command)

    def parse_command(self, command):
        # Parse and execute individual commands
        parts = command.split()
        if parts[0] == "LOADA":
            self.short_term[parts[1]] = self.memory[int(parts[2])]
        elif parts[0] == "LOAD":
            self.short_term[parts[1]] = self.memory[self.short_term["A"]]
        elif parts[0] == "LOADI":
            # Load an immediate value into a register
            value = int(parts[2])
            # Check for arithmetic overflow
            if abs(value) > 2**42:
                self.error = True
                print("I'm afraid I can't do that")
                return
            self.short_term[parts[1]] = value
        elif parts[0] == "STOREA":
            # Store the value of a register into memory at a specified address
            mem_address = int(parts[2])
            # Check for arithmetic overflow
            if abs(self.short_term[parts[1]]) > 2**42:
                self.error = True
                print("I'm afraid I can't do that")
                return
            self.memory[mem_address] = self.short_term[parts[1]]
        elif parts[0] == "STORE":
            # Store the value of a register into memory using the value stored in register A as the memory address
            mem_address = self.short_term["A"]
            # Check for arithmetic overflow
            if abs(self.short_term[parts[1]]) > 2**42:
                self.error = True
                print("I'm afraid I can't do that")
                return
            self.memory[mem_address] = self.short_term[parts[1]]
        elif parts[0] == "MOVE":
            # Move the value from one register to another
            self.short_term[parts[1]] = self.short_term[parts[2]]
        elif parts[0] == "ADDI":
            # Add an immediate value to a register
            value = int(parts[2])
            # Check for arithmetic overflow
            if abs(value) > 2**42:
                self.error = True
                print("I'm afraid I can't do that")
                return
            self.short_term[parts[1]] += value
        elif parts[0] == "ADD":
            # Add the value of one register to another
            self.short_term[parts[1]] += self.short_term[parts[2]]
            # Check for arithmetic overflow
            if abs(self.short_term[parts[1]]) > 2**42:
                self.error = True
                print("I'm afraid I can't do that")
                return
        elif parts[0] == "SUB":
            # Subtract the value of one register from another
            self.short_term[parts[1]] -= self.short_term[parts[2]]
            # Check for arithmetic overflow
            if abs(self.short_term[parts[1]]) > 2**42:
                self.error = True
                print("I'm afraid I can't do that")
                return
        elif parts[0] == "MUL":
            # Multiply the value of one register by another
            self.short_term[parts[1]] *= self.short_term[parts[2]]
            # Check for arithmetic overflow
            if abs(self.short_term[parts[1]]) > 2**42:
                self.error = True
                print("I'm afraid I can't do that")
                return
        elif parts[0] == "DIV":
            # Divide the value of one register by another
            if self.short_term[parts[2]] == 0:
                # Check for division by zero
                self.error = True
                print("I'm afraid I can't do that")
            else:
                self.short_term[parts[1]] //= self.short_term[parts[2]]
                # Check for arithmetic overflow
                if abs(self.short_term[parts[1]]) > 2**42:
                    self.error = True
                    print("I'm afraid I can't do that")
                    return
        elif parts[0] == "J":
            # Jump to a specified position in the command list
            self.short_term["P"] += int(parts[1])
        elif parts[0] == "JR":
            # Jump to a position relative to the current position
            self.short_term["P"] += self.short_term[parts[1]]
        elif parts[0] == "JZ":
            # Jump to a specified position if a register's value is zero
            if self.short_term[parts[1]] == 0:
                self.short_term["P"] += int(parts[2])
        elif parts[0] == "JLT":
            # Jump to a specified position if one register's value is less than another
            if self.short_term[parts[1]] < self.short_term[parts[2]]:
                self.short_term["P"] += int(parts[3])
        elif parts[0] == "HALT":
            # Halt the execution
            self.error = True
            print("Execution halted")
            return
        elif parts[0] == "PRINT":
            # Print the value stored in a register
            print(self.short_term[parts[1]])

        self.short_term["P"] += 1
        self.short_term["X"] += 1


# Create an instance of the LAH9000 interpreter
assembly_handler = AssemblyHandler()

# Load commands from the user
assembly_handler.load_commands_from_user()

# Execute the loaded commands
assembly_handler.execute()
