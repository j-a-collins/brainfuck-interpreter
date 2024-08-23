# Brainfuck Interpreter

a simple Python-based **brainfuck interpreter** that executes code and processes input/output.

## Features

- supports all BF commands (`>`, `<`, `+`, `-`, `.`, `,`, `[`, `]`)
- processes user input, handles output
- covers loops and conditional logic

## Commands

all the brainfuck commands:

| Command | Description                                                          |
| ------- | ---------------------------------------------------------------------|
| `>`     | move the pointer to the right                                        |
| `<`     | move the pointer to the left                                         |
| `+`     | increment the byte at the pointer                                    |
| `-`     | decrement the byte at the pointer                                    |
| `.`     | output the byte at the pointer as a character                        |
| `,`     | accept one byte of input, stores value in the current cell           |
| `[`     | jump to the matching `]` if the byte at the pointer is 0             |
| `]`     | jump back to the matching `[` if the byte at the pointer is non-zero |

## How to Use

run brainfuck.py to start the interpreter. enter your code and then use the following commands:

| Command  | Description                                                   |
| -------- | ------------------------------------------------------------- |
| `:run`   | executes the code                                             |
| `:clear` | clears the accumulated code                                   |
| `:exit`  | exits the program                                             |


### Example

hello world example using the interpreter:

```bash 
welcome to brainfuck!
type your code below. enter ':run' to execute, ':clear' to clear the code, or ':exit' to quit.
Brainfuck> >++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.
Brainfuck> :run
output: Hello, World!
```

### Installation and Running

to run the interpreter:

1. clone the repo: 
```
git clone https://github.com/your-username/brainfuck-interpreter.git
```
2. cd into the project:
```
cd brainfuck-interpreter
```
3. run brainfuck.py and write your code
```
python brainfuck.py
```

### Project Structure

    brainfuck.py: contains the core implementation of the interpreter.
    README.md: docs.

### Contributing

contributions welcome.
