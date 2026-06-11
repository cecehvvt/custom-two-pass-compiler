from semantic_analyzer import SemanticAnalyzer
from parser import Parser
from lexer import tokenize
from symbol_table import SymbolTable
from gui import CompilerGUI
import tkinter as tk

root = tk.Tk()
app = CompilerGUI(root)
root.mainloop()

source_code = """
RUN 100;

NAT x
NAT y
COMMA result
TWINAT total
TWINCO average

TAKE <- "Enter x"
TAKE <- "Enter y"

result [ x PLUS y BUMP 2]
total [ x PLUS y]
average [ result CUT 2.0]

THIS (result > 15) {
    GIVE -> "Result is large"
} OR {
    GIVE -> "Result is small"
}

WHEN (x > 0) {
    EX x
}

CYC (NAT i = 0, 5, NEXT) {
    GIVE -> "Loop running"
}

STOP;

z BY 5
x BY 3.14
result BY "hello"
"""

tokens, errors = tokenize(source_code)


def tokens_until_stop(tokens):
    effective_tokens = []
    include_stop_semicolon = False
    for token in tokens:
        effective_tokens.append(token)
        if include_stop_semicolon:
            break
        if token["type"] == "KEYWORD" and token["value"] == "STOP":
            include_stop_semicolon = True
    return effective_tokens


effective_tokens = tokens_until_stop(tokens)


def find_take_target(prompt_token, symbol_table):
    if prompt_token["type"] == "IDENTIFIER" and symbol_table.lookup(prompt_token["value"]):
        return prompt_token["value"]

    words = str(prompt_token["value"]).replace(":", " ").replace(",", " ").split()
    for word in reversed(words):
        if symbol_table.lookup(word):
            return word
    return None


def convert_take_value(value, symbol, line, semantic_errors):
    data_type = symbol["type"]
    try:
        if data_type == "NAT":
            return str(int(value))
        if data_type in ["COMMA", "TWINCO"]:
            return str(float(value))
        if data_type == "TWINAT":
            return str(int(value))
    except ValueError:
        semantic_errors.append(
            f"Line {line}: TAKE value '{value}' is not valid for {data_type} variable '{symbol['name']}'"
        )
        return None

    return value


def handle_take_inputs(tokens, symbol_table, semantic_errors):
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token["type"] == "KEYWORD" and token["value"] == "TAKE":
            if (
                i + 2 < len(tokens)
                and tokens[i + 1]["type"] == "OPERATOR"
                and tokens[i + 1]["value"] == "<-"
            ):
                prompt_token = tokens[i + 2]
                prompt = prompt_token["value"]
                target_name = find_take_target(prompt_token, symbol_table)

                if target_name is None:
                    semantic_errors.append(
                        f"Line {token['line']}: TAKE prompt must reference a declared variable"
                    )
                    i += 1
                    continue

                symbol = symbol_table.lookup(target_name)
                entered_value = input(f"{prompt}: ")
                converted_value = convert_take_value(entered_value, symbol, token["line"], semantic_errors)
                if converted_value is not None:
                    symbol_table.set_value(target_name, converted_value)

        i += 1

print("TOKENS:")
for token in tokens:
    print(f"Line {token['line']} | {token['type']} | {token['value']}")

print("\nLEXICAL ERRORS:")
for error in errors:
    print(error)


# Symbol Table oluşturma
symbol_table = SymbolTable()
semantic_errors = []

i = 0
scope_stack = ["global"]

while i < len(effective_tokens):
    token = effective_tokens[i]

    if token["type"] == "KEYWORD" and token["value"] in ["THIS", "OR", "WHEN", "CYC"]:
        scope_stack.append(token["value"])

    if token["type"] == "DELIMITER" and token["value"] == "}":
        if len(scope_stack) > 1:
            scope_stack.pop()

    current_scope = scope_stack[-1]

    if token["type"] == "KEYWORD" and token["value"] in ["NAT", "COMMA", "TWINAT", "TWINCO"]:
        data_type = token["value"]

        if i + 1 < len(effective_tokens) and effective_tokens[i + 1]["type"] == "IDENTIFIER":
            variable_name = effective_tokens[i + 1]["value"]
            line = effective_tokens[i + 1]["line"]

            error = symbol_table.add_symbol(variable_name, data_type, current_scope, line)

            if error:
                semantic_errors.append(error)

    i += 1

handle_take_inputs(effective_tokens, symbol_table, semantic_errors)

print("\nSYMBOL TABLE:")
print("Name\tType\tScope\tMemory\tLine\tValue")
for symbol in symbol_table.display():
    print(
        f"{symbol['name']}\t"
        f"{symbol['type']}\t"
        f"{symbol['scope']}\t"
        f"{symbol['memory_location']}\t"
        f"{symbol['line']}\t"
        f"{symbol.get('value', '')}"
    )

semantic_analyzer = SemanticAnalyzer(effective_tokens, symbol_table)
semantic_errors.extend(semantic_analyzer.analyze())

print("\nSEMANTIC ERRORS:")
for error in semantic_errors:
    print(error)

parser = Parser(effective_tokens)
ast, syntax_errors = parser.parse()

print("\nAST:")
print(ast.display())

print("\nSYNTAX ERRORS:")
for error in syntax_errors:
    print(error)
