class SymbolTable:
    def __init__(self):
        self.symbols = []
        self.memory_location = 1000

    def add_symbol(self, name, data_type, scope, line):
        for symbol in self.symbols:
            if symbol["name"] == name and symbol["scope"] == scope:
                return f"Line {line}: Duplicate declaration of variable '{name}' in scope '{scope}'"

        self.symbols.append({
            "name": name,
            "type": data_type,
            "scope": scope,
            "memory_location": self.memory_location,
            "line": line,
            "value": ""
        })

        self.memory_location += 4
        return None

    def set_value(self, name, value, scope=None):
        symbol = self.lookup(name, scope)
        if symbol:
            symbol["value"] = value
            return True
        return False

    def lookup(self, name, scope=None):
        if scope:
            for symbol in reversed(self.symbols):
                if symbol["name"] == name and symbol["scope"] == scope:
                    return symbol

        for symbol in reversed(self.symbols):
            if symbol["name"] == name and symbol["scope"] == "global":
                return symbol

        for symbol in reversed(self.symbols):
            if symbol["name"] == name:
                return symbol

        return None

    def display(self):
        return self.symbols
