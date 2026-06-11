keywords = ["NAT", "COMMA", "TWINAT", "TWINCO", "THIS", "OR", "WHEN", "CYC", "GIVE", "TAKE", "RUN", "STOP"]
word_operators = ["PLUS", "MINUS", "BUMP", "CUT", "NEXT", "EX", "BY"]

operators = ["==", "!=", "<=", ">=", "->", "<-", "&&", "||", "=", "<", ">"]

delimiters = [";", ",", "(", ")", "{", "}", "[", "]"]


def add_token(tokens, token_type, value, line):
    tokens.append({
        "type": token_type,
        "value": value,
        "line": line
    })


def tokenize(source_code):
    tokens = []
    errors = []
    line = 1
    i = 0

    while i < len(source_code):
        char = source_code[i]

        # 1. Boşluk ve tab karakterlerini geç
        if char in [" ", "\t", "\r"]:
            i += 1
            continue

        # 2. Satır sonu kontrolü
        if char == "\n":
            add_token(tokens, "DELIMITER", "NEWLINE", line)
            line += 1
            i += 1
            continue

        # 3. Yorum satırı kontrolü: // yorum
        if char == "/" and i + 1 < len(source_code) and source_code[i + 1] == "/":
            while i < len(source_code) and source_code[i] != "\n":
                i += 1
            continue

        # 4. Identifier veya keyword kontrolü
        if char.isalpha() or char == "_":
            word = ""

            while i < len(source_code) and (source_code[i].isalnum() or source_code[i] == "_"):
                word += source_code[i]
                i += 1

            if word in keywords:
                add_token(tokens, "KEYWORD", word, line)
            elif word in word_operators:
                add_token(tokens, "OPERATOR", word, line)
            else:
                add_token(tokens, "IDENTIFIER", word, line)

            continue

        # 5. Sayı kontrolü: integer veya float
        if char.isdigit():
            number = ""
            dot_count = 0

            while i < len(source_code) and (source_code[i].isdigit() or source_code[i] == "."):
                if source_code[i] == ".":
                    dot_count += 1

                number += source_code[i]
                i += 1

            if dot_count == 0:
                add_token(tokens, "INTEGER_LITERAL", number, line)
            elif dot_count == 1:
                add_token(tokens, "FLOAT_LITERAL", number, line)
            else:
                errors.append(f"Line {line}: Malformed number '{number}'")

            continue

        # 6. String literal kontrolü
        if char == '"':
            string_value = ""
            i += 1

            while i < len(source_code) and source_code[i] != '"':
                if source_code[i] == "\n":
                    errors.append(f"Line {line}: Unterminated string literal")
                    line += 1
                    break

                string_value += source_code[i]
                i += 1

            if i < len(source_code) and source_code[i] == '"':
                i += 1
                add_token(tokens, "STRING_LITERAL", string_value, line)

            continue

        # 7. İki karakterli operatör kontrolü
        if i + 1 < len(source_code):
            two_char = source_code[i:i + 2]

            if two_char in operators:
                add_token(tokens, "OPERATOR", two_char, line)
                i += 2
                continue

        # 8. Tek karakterli operatör kontrolü
        if char in operators:
            add_token(tokens, "OPERATOR", char, line)
            i += 1
            continue

        # 9. Delimiter kontrolü
        if char in delimiters:
            add_token(tokens, "DELIMITER", char, line)
            i += 1
            continue

        # 10. Tanınmayan karakter hatası
        errors.append(f"Line {line}: Invalid character '{char}'")
        i += 1

    return tokens, errors
