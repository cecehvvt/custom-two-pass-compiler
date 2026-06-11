from ast_nodes import ASTNode


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.errors = []
        self.ast = ASTNode("Program")
        self.stopped = False

    def get_current_token(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def advance(self):
        self.current += 1

    def consume_statement_end(self):
        token = self.get_current_token()
        if token is not None and token["type"] == "DELIMITER" and token["value"] == "NEWLINE":
            self.advance()

    def match(self, expected_type, expected_value=None):
        token = self.get_current_token()

        if token is None:
            self.errors.append("Unexpected end of input")
            return False

        if token["type"] != expected_type:
            self.errors.append(
                f"Line {token['line']}: Expected {expected_type}, found {token['type']} '{token['value']}'"
            )
            return False

        if expected_value is not None and token["value"] != expected_value:
            self.errors.append(
                f"Line {token['line']}: Expected '{expected_value}', found '{token['value']}'"
            )
            return False

        self.advance()
        return True

    def parse(self):
        while self.get_current_token() is not None and not self.stopped:
            self.parse_statement()

        return self.ast, self.errors

    def parse_statement(self):
        token = self.get_current_token()

        if token is None:
            return

        if token["type"] == "DELIMITER" and token["value"] == "NEWLINE":
            self.advance()

        elif token["type"] == "KEYWORD" and token["value"] in ["NAT", "COMMA", "TWINAT", "TWINCO"]:
            self.parse_declaration()

        elif token["type"] == "IDENTIFIER":
            self.parse_assignment()

        elif token["type"] == "KEYWORD" and token["value"] == "GIVE":
            self.parse_print()

        elif token["type"] == "KEYWORD" and token["value"] == "TAKE":
            self.parse_scanf()

        elif token["type"] == "KEYWORD" and token["value"] == "THIS":
            self.parse_if()

        elif token["type"] == "KEYWORD" and token["value"] == "WHEN":
            self.parse_while()

        elif token["type"] == "KEYWORD" and token["value"] == "CYC":
            self.parse_for()

        elif token["type"] == "KEYWORD" and token["value"] == "RUN":
            self.parse_run()

        elif token["type"] == "KEYWORD" and token["value"] == "STOP":
            self.parse_stop()

        elif token["type"] == "OPERATOR" and token["value"] in ["NEXT", "EX"]:
            self.parse_update()

        elif token["type"] == "DELIMITER" and token["value"] == "}":
            self.advance()

        else:
            self.errors.append(
                f"Line {token['line']}: Unexpected token '{token['value']}'"
            )
            self.advance()

    def parse_declaration(self):
        data_type = self.get_current_token()["value"]
        line = self.get_current_token()["line"]

        self.advance()

        if self.match("IDENTIFIER"):
            variable_name = self.tokens[self.current - 1]["value"]

            node = ASTNode("Declaration", variable_name)
            node.add_child(ASTNode("Type", data_type))
            self.ast.add_child(node)

            self.consume_statement_end()
        else:
            self.errors.append(f"Line {line}: Invalid declaration")

    def parse_run(self):
        node = ASTNode("Run")

        self.match("KEYWORD", "RUN")
        token = self.get_current_token()

        if token is not None and token["type"] == "INTEGER_LITERAL":
            node.add_child(ASTNode("StartAddress", token["value"]))
            self.advance()
        else:
            if token:
                self.errors.append(f"Line {token['line']}: RUN expects an integer start address")
            else:
                self.errors.append("Unexpected end of input after RUN")

        self.match("DELIMITER", ";")

        self.ast.add_child(node)

    def parse_stop(self):
        node = ASTNode("Stop")

        self.match("KEYWORD", "STOP")

        self.match("DELIMITER", ";")

        self.ast.add_child(node)
        self.stopped = True

    # -----------------------------
    # Expression Parser
    # Precedence:
    # 1. factor: numbers, identifiers, strings, parentheses
    # 2. term: BUMP CUT
    # 3. expression: PLUS MINUS
    # -----------------------------
    def parse_expression(self):
        left = self.parse_term()

        while self.get_current_token() is not None:
            token = self.get_current_token()

            if token["type"] == "OPERATOR" and token["value"] in ["PLUS", "MINUS"]:
                operator = token["value"]
                self.advance()

                right = self.parse_term()

                node = ASTNode("Expression", operator)
                node.add_child(left)
                node.add_child(right)

                left = node
            else:
                break

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.get_current_token() is not None:
            token = self.get_current_token()

            if token["type"] == "OPERATOR" and token["value"] in ["BUMP", "CUT"]:
                operator = token["value"]
                self.advance()

                right = self.parse_factor()

                node = ASTNode("Expression", operator)
                node.add_child(left)
                node.add_child(right)

                left = node
            else:
                break

        return left

    def parse_factor(self):
        token = self.get_current_token()

        if token is None:
            self.errors.append("Unexpected end of expression")
            return ASTNode("Error", "Unexpected end")

        if token["type"] in ["INTEGER_LITERAL", "FLOAT_LITERAL", "IDENTIFIER", "STRING_LITERAL"]:
            self.advance()
            return ASTNode(token["type"], token["value"])

        if token["type"] == "OPERATOR" and token["value"] in ["NEXT", "EX"]:
            operator = token["value"]
            self.advance()
            node = ASTNode("Expression", operator)
            node.add_child(self.parse_factor())
            return node

        if token["type"] == "DELIMITER" and token["value"] == "(":
            self.advance()
            node = self.parse_expression()
            self.match("DELIMITER", ")")
            return node

        self.errors.append(
            f"Line {token['line']}: Invalid expression token '{token['value']}'"
        )
        self.advance()
        return ASTNode("Error", token["value"])

    def parse_assignment(self):
        variable_name = self.get_current_token()["value"]

        node = ASTNode("Assignment", variable_name)

        self.advance()
        token = self.get_current_token()

        if token is not None and token["type"] == "DELIMITER" and token["value"] == "[":
            self.advance()
            expression_node = self.parse_expression()
            node.add_child(expression_node)
            self.match("DELIMITER", "]")
            self.consume_statement_end()

            self.ast.add_child(node)
            return

        self.match("OPERATOR", "BY")

        expression_node = self.parse_expression()
        node.add_child(expression_node)
        self.consume_statement_end()
        self.ast.add_child(node)

    def parse_update(self):
        operator = self.get_current_token()["value"]
        node = ASTNode("Update", operator)

        self.advance()
        token = self.get_current_token()

        if token is not None and token["type"] == "IDENTIFIER":
            node.add_child(ASTNode("IDENTIFIER", token["value"]))
            self.advance()
        else:
            if token:
                self.errors.append(f"Line {token['line']}: {operator} expects an identifier")
            else:
                self.errors.append(f"Unexpected end of input after {operator}")

        self.consume_statement_end()

        self.ast.add_child(node)

    def parse_print(self):
        node = ASTNode("Give")

        self.match("KEYWORD", "GIVE")
        self.match("OPERATOR", "->")

        expression_node = self.parse_expression()
        node.add_child(expression_node)

        self.consume_statement_end()

        self.ast.add_child(node)

    def parse_scanf(self):
        node = ASTNode("Take")

        self.match("KEYWORD", "TAKE")
        self.match("OPERATOR", "<-")

        token = self.get_current_token()

        if token is not None and token["type"] in ["STRING_LITERAL", "IDENTIFIER"]:
            node.add_child(ASTNode("InputPrompt", token["value"]))
            self.advance()
        else:
            if token:
                self.errors.append(f"Line {token['line']}: TAKE expects a text or identifier")

        self.consume_statement_end()

        self.ast.add_child(node)

    def parse_condition(self):
        node = ASTNode("Condition")

        left = self.parse_expression()
        node.add_child(left)

        token = self.get_current_token()

        if token is not None and token["type"] == "OPERATOR" and token["value"] in [
            "==", "!=", "<", ">", "<=", ">=", "&&", "||"
        ]:
            operator = token["value"]
            self.advance()

            condition_node = ASTNode("ConditionOperator", operator)
            condition_node.add_child(left)

            right = self.parse_expression()
            condition_node.add_child(right)

            return condition_node

        return node

    def parse_if(self):
        node = ASTNode("IfStatement")

        self.match("KEYWORD", "THIS")
        self.match("DELIMITER", "(")

        condition_node = self.parse_condition()
        node.add_child(condition_node)

        self.match("DELIMITER", ")")
        self.match("DELIMITER", "{")

        body_node = ASTNode("IfBlock")

        while self.get_current_token() is not None:
            token = self.get_current_token()

            if token["type"] == "DELIMITER" and token["value"] == "}":
                break

            before_count = len(self.ast.children)
            self.parse_statement()

            if len(self.ast.children) > before_count:
                body_node.add_child(self.ast.children.pop())

        self.match("DELIMITER", "}")
        node.add_child(body_node)

        token = self.get_current_token()

        if token is not None and token["type"] == "KEYWORD" and token["value"] == "OR":
            self.match("KEYWORD", "OR")
            self.match("DELIMITER", "{")

            else_node = ASTNode("ElseBlock")

            while self.get_current_token() is not None:
                token = self.get_current_token()

                if token["type"] == "DELIMITER" and token["value"] == "}":
                    break

                before_count = len(self.ast.children)
                self.parse_statement()

                if len(self.ast.children) > before_count:
                    else_node.add_child(self.ast.children.pop())

            self.match("DELIMITER", "}")
            node.add_child(else_node)

        self.ast.add_child(node)

    def parse_while(self):
        node = ASTNode("WhileLoop")

        self.match("KEYWORD", "WHEN")
        self.match("DELIMITER", "(")

        condition_node = self.parse_condition()
        node.add_child(condition_node)

        self.match("DELIMITER", ")")
        self.match("DELIMITER", "{")

        body_node = ASTNode("WhileBlock")

        while self.get_current_token() is not None:
            token = self.get_current_token()

            if token["type"] == "DELIMITER" and token["value"] == "}":
                break

            before_count = len(self.ast.children)
            self.parse_statement()

            if len(self.ast.children) > before_count:
                body_node.add_child(self.ast.children.pop())

        self.match("DELIMITER", "}")
        node.add_child(body_node)

        self.ast.add_child(node)

    def parse_for(self):
        node = ASTNode("ForLoop")

        self.match("KEYWORD", "CYC")
        self.match("DELIMITER", "(")

        header_node = ASTNode("ForHeader")

        while self.get_current_token() is not None:
            token = self.get_current_token()

            if token["type"] == "DELIMITER" and token["value"] == ")":
                break

            header_node.add_child(ASTNode(token["type"], token["value"]))
            self.advance()

        self.match("DELIMITER", ")")
        node.add_child(header_node)

        self.match("DELIMITER", "{")

        body_node = ASTNode("ForBlock")

        while self.get_current_token() is not None:
            token = self.get_current_token()

            if token["type"] == "DELIMITER" and token["value"] == "}":
                break

            before_count = len(self.ast.children)
            self.parse_statement()

            if len(self.ast.children) > before_count:
                body_node.add_child(self.ast.children.pop())

        self.match("DELIMITER", "}")
        node.add_child(body_node)

        self.ast.add_child(node)
