# AST = Abstract Syntax Tree
class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        indent = "  " * level
        result = f"{indent}{self.node_type}"

        if self.value is not None:
            result += f": {self.value}"

        result += "\n"

        for child in self.children:
            result += child.display(level + 1)

        return result