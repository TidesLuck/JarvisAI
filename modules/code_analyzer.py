import ast
import asyncio

class CodeAnalyzer:
    async def analyze_code(self, code_path):
        with open(code_path, "r") as f:
            code = f.read()
        try:
            ast.parse(code)
            return f"Код в {code_path} валиден."
        except SyntaxError as e:
            return f"Ошибка в коде: {str(e)}."