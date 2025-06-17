import re


class ZCompiler:
    def __init__(self, sourceCode):
        self.sourceCode = sourceCode
        self.pythonCode = None

    def compile(self):
        result_list = [item.strip() for item in self.sourceCode.split(".")]
        python_code_lines = []

        for line in result_list:
            if self.is_variable_assignment(line):
                formatted_line = self.format_variable_assignment(line)
                python_code_lines.append(formatted_line)
            elif self.is_arithmetic(line):
                python_code_lines.append("arth")

        print(python_code_lines)

    def is_variable_assignment(self, source):
        return re.search(r'@(\w+)\s+is\s+(\d+)', source)

    def format_variable_assignment(self, source):
        match = re.search(r'@(\w+)\s+is\s+(\d+)', source)
        variable_name = match.group(1)
        value = match.group(2)
        formatted_line = f"{variable_name} = {value}"
        return formatted_line

    def is_arithmetic(self, source):
        arithmetic_functions = ['add', 'mul', 'sub', 'div']
        for function in arithmetic_functions:
            if re.search(rf'\b{function}\(', source):
                return True
        return False

    def print(self):
        print(self.pythonCode)
