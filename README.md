# computer-architecture-CC
Computer Architecture Portfolio Project for Codecademy's Computer Science Career Path

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
