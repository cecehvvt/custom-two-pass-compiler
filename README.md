![Compiler GUI](images/compiler_gui.png)
# Two-Pass Compiler Project

A Python-based two-pass compiler developed for the System Programming course. The project implements a custom programming language and demonstrates the fundamental stages of compiler design, including lexical analysis, syntax analysis, semantic analysis, symbol table management, and Abstract Syntax Tree (AST) generation.

The compiler is implemented entirely from scratch without using compiler-generator tools such as Lex, Yacc, PLY, or ANTLR. A graphical user interface was developed using Tkinter to visualize compiler outputs.

## Features

* Custom-designed programming language
* Lexical Analysis (Lexer)
* Syntax Analysis (Parser)
* Semantic Analysis
* Symbol Table Generation
* Abstract Syntax Tree (AST) Generation
* Error Detection and Reporting
* Interactive Tkinter GUI
* Multiple demonstration programs

## Project Structure

```text
├── lexer.py                # Lexical analyzer
├── parser.py               # Syntax analyzer and AST generator
├── semantic_analyzer.py    # Semantic analysis
├── symbol_table.py         # Symbol table management
├── ast_nodes.py            # AST node definitions
├── gui.py                  # Tkinter graphical interface
├── main.py                 # Application entry point
└── sample_input.txt        # Example source code
```

## Compiler Workflow

### Pass 1 – Lexical Analysis

The lexer reads the source code character by character and produces a token stream.

Supported token categories:

* Keywords
* Identifiers
* Operators
* Delimiters
* Integer Literals
* Float Literals
* String Literals

The lexer also detects lexical errors such as:

* Invalid characters
* Malformed numbers
* Unclosed string literals

### Pass 2 – Syntax & Semantic Analysis

The parser processes the generated tokens according to the language grammar and creates an Abstract Syntax Tree (AST).

The semantic analyzer performs:

* Variable declaration checks
* Duplicate declaration checks
* Type compatibility checks
* Undefined variable detection
* Expression validation

## Language Overview

Program execution begins with:

```text
RUN 100;
```

and ends with:

```text
STOP;
```

### Variable Types

| Keyword | Description      |
| ------- | ---------------- |
| NAT     | Integer          |
| COMMA   | Float            |
| TWINAT  | Extended Integer |
| TWINCO  | Extended Float   |

### Assignment

```text
NAT x
x BY 10
```

### Arithmetic Expressions

```text
result [ x PLUS y BUMP 2 ]
```

Supported operators:

| Operator | Meaning        |
| -------- | -------------- |
| PLUS     | Addition       |
| MINUS    | Subtraction    |
| BUMP     | Multiplication |
| CUT      | Division       |

### Conditional Statements

```text
THIS (result > 15) {
    GIVE -> "Result is large"
} OR {
    GIVE -> "Result is small"
}
```

### Loops

```text
WHEN (x > 0) {
    EX x
}
```

```text
CYC (NAT i = 0, 5, NEXT) {
    GIVE -> "Loop running"
}
```

## GUI Features

The application interface includes:

* Source Code Editor
* Token Stream Viewer
* Symbol Table Viewer
* Syntax Tree Viewer
* Error Reporting Panel
* Language Guide Section

## Error Handling

The compiler reports three categories of errors:

### Lexical Errors

* Invalid characters
* Malformed numbers
* Unclosed strings

### Syntax Errors

* Missing brackets
* Invalid expressions
* Unexpected tokens

### Semantic Errors

* Undefined variables
* Duplicate declarations
* Type mismatch errors

## Running the Project

Clone the repository and run:

```bash
python main.py
```

or

```bash
python gui.py
```

## Technologies Used

* Python
* Tkinter
* Custom Lexer
* Custom Parser
* Abstract Syntax Tree (AST)
* Symbol Table Management

## Course Information

**Course:** System Programming
**Project Type:** Compiler Design Project
**Language:** Python
**GUI Framework:** Tkinter

## License

This project is released under the MIT License.
