"""
author: jack adam collins
date: 22-08-24

___.                .__        _____              __    
\_ |______________  |__| _____/ ____\_ __   ____ |  | __
 | __ \_  __ \__  \ |  |/    \   __\  |  \_/ ___\|  |/ /
 | \_\ \  | \// __ \|  |   |  \  | |  |  /\  \___|    < 
 |___  /__|  (____  /__|___|  /__| |____/  \___  >__|_ \
     \/           \/        \/                 \/     \/

brainfuck interpreter and shell

this module contains a Brainfuck interpreter and shell interface
for writing and running Brainfuck. this can execute Brainfuck commands, 
manipulate the tape, handle loops, and processing both input and output.

all 8 commands are supported:
- `>`: move the tape pointer one cell to the right.
- `<`: move the tape pointer one cell to the left.
- `+`: increment the value at the current cell by 1.
- `-`: decrement the value at the current cell by 1.
- `.`: output the value at the current cell as an ASCII character.
- `,`: read a byte of input and store it in the current cell.
- `[`: begin a loop.
- `]`: end a loop.

"""

def brainfuck_interpreter(code, input_data=""):
    """executes code, returns the output

    Parameters
    ----------
        code (str): the brainfuck to be executed.
        input_data (str): input data for the program (if any).

    Returns
    -------
        str: the generated output.

    """
    tape = [0] * 10000  # number of cells in the tape (10,000)
    pointer = 0  # points to current cell in tape
    code_ptr = 0  # points to current command
    loop_stack = []  # handle loop ([ and ]) positions
    input_ptr = 0  # track input data
    output = ""  # store output

    # trigger each command in the code
    while code_ptr < len(code):
        command = code[code_ptr]

        if command == ">":
            pointer = (pointer + 1) % len(tape)  # right
        elif command == "<":
            pointer = (pointer - 1) % len(tape)  # left
        elif command == "+":
            tape[pointer] = (tape[pointer] + 1) % 256  # increment cell value
        elif command == "-":
            tape[pointer] = (tape[pointer] - 1) % 256  # decrement cell value
        elif command == ".":
            output += chr(tape[pointer])  # output cell value as ASCII
        elif command == ",":
            if input_ptr < len(input_data):
                tape[pointer] = ord(input_data[input_ptr])  # input as ASCII
                input_ptr += 1
            else:
                tape[pointer] = 0  # assume null byte (0)
        elif command == "[":
            if tape[pointer] == 0:
                # skip loop if cell is 0
                loop_counter = 1
                while loop_counter > 0:
                    code_ptr += 1
                    if code[code_ptr] == "[":
                        loop_counter += 1
                    elif code[code_ptr] == "]":
                        loop_counter -= 1
            else:
                loop_stack.append(code_ptr)  # save position '['
        elif command == "]":
            if tape[pointer] != 0:
                # back to '['
                code_ptr = loop_stack[-1]
            else:
                loop_stack.pop()  # loop finished

        code_ptr += 1  # next command

    return output


def brainfuck_shell():
    """
    brainfuck shell interface to write and run code.

    the shell provides the following:
    - `:run`: execute the accumulated code.
    - `:clear`: clear the accumulated code.
    - `:exit`: exit the shell.
    """
    
    print("welcome to brainfuck!")
    print(
        "type your code below. enter ':run' to execute, ':clear' to clear the code, or ':exit' to quit."
    )

    code = []
    while True:
        # get input
        user_input = input("Brainfuck> ")

        if user_input == ":run":
            # join code lines and run them
            bf_code = "".join(code)
            if not bf_code:
                print("no code to run.")
            else:
                output = brainfuck_interpreter(bf_code)
                print(f"output: {output}")
        elif user_input == ":clear":
            # clear accumulated code
            code = []
            print("code cleared.")
        elif user_input == ":exit":
            # exit the shell
            print("exiting Brainfuck interpreter.")
            break
        else:
            # add input to current
            code.append(user_input)


if __name__ == "__main__":
    brainfuck_shell()
