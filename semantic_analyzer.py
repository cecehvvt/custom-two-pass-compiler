class SemanticAnalyzer:
    NUMBER_TYPES = ["NAT", "COMMA", "TWINAT", "TWINCO"]
    INTEGER_TYPES = ["NAT", "TWINAT"]
    DECIMAL_TYPES = ["COMMA", "TWINCO"]

    def __init__(self, tokens, symbol_table):
        self.tokens = self.tokens_until_stop(tokens)
        self.symbol_table = symbol_table
        self.errors = []

    def tokens_until_stop(self, tokens):
        effective_tokens = []
        include_stop_semicolon = False
        for token in tokens:
            effective_tokens.append(token)
            if include_stop_semicolon:
                break
            if token["type"] == "KEYWORD" and token["value"] == "STOP":
                include_stop_semicolon = True
        return effective_tokens

    def analyze(self):
        self.check_undeclared_variables()
        self.check_assignment_types()
        return self.errors

    def is_declared(self, variable_name):
        return self.symbol_table.lookup(variable_name) is not None

    def get_variable_type(self, variable_name):
        symbol = self.symbol_table.lookup(variable_name)
        if symbol:
            return symbol["type"]
        return None

    def check_undeclared_variables(self):
        previous_token = None

        for token in self.tokens:
            if token["type"] == "IDENTIFIER":
                name = token["value"]

                if (
                    previous_token
                    and previous_token["type"] == "KEYWORD"
                    and previous_token["value"] in self.NUMBER_TYPES
                ):
                    previous_token = token
                    continue

                if not self.is_declared(name):
                    self.errors.append(
                        f"Line {token['line']}: Variable '{name}' used before declaration"
                    )

            previous_token = token

    def check_assignment_types(self):
        i = 0

        while i < len(self.tokens):
            token = self.tokens[i]

            if token["type"] == "IDENTIFIER":
                variable_name = token["value"]

                if i + 1 >= len(self.tokens):
                    i += 1
                    continue

                next_token = self.tokens[i + 1]
                is_by_assignment = next_token["type"] == "OPERATOR" and next_token["value"] == "BY"
                is_bracket_assignment = next_token["type"] == "DELIMITER" and next_token["value"] == "["

                if not is_by_assignment and not is_bracket_assignment:
                    i += 1
                    continue

                variable_type = self.get_variable_type(variable_name)

                if variable_type is None:
                    i += 1
                    continue

                j = i + 2

                while j < len(self.tokens):
                    right_token = self.tokens[j]

                    if right_token["type"] == "DELIMITER" and right_token["value"] in ["NEWLINE", ";", ")", "]"]:
                        break

                    if (
                        right_token["type"] == "STRING_LITERAL"
                        and variable_type in self.NUMBER_TYPES
                    ):
                        self.errors.append(
                            f"Line {right_token['line']}: Type mismatch. Cannot assign string to {variable_type} variable '{variable_name}'"
                        )

                    if right_token["type"] == "FLOAT_LITERAL" and variable_type in self.INTEGER_TYPES:
                        self.errors.append(
                            f"Line {right_token['line']}: Type mismatch. Cannot assign decimal value to {variable_type} variable '{variable_name}'"
                        )

                    if right_token["type"] == "IDENTIFIER":
                        right_type = self.get_variable_type(right_token["value"])

                        if variable_type in self.INTEGER_TYPES and right_type in self.DECIMAL_TYPES:
                            self.errors.append(
                                f"Line {right_token['line']}: Type mismatch. Cannot assign {right_type} value to {variable_type} variable '{variable_name}'"
                            )

                        if variable_type == "COMMA" and right_type == "TWINCO":
                            self.errors.append(
                                f"Line {right_token['line']}: Type mismatch. Cannot assign TWINCO value to COMMA variable '{variable_name}'"
                            )

                    j += 1

            i += 1
