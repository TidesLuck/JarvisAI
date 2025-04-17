import asyncio
import sys
from io import StringIO
import contextlib

class PythonInterpreter:
    async def execute_code(self, code):
        output = StringIO()
        with contextlib.redirect_stdout(output):
            try:
                exec(code)
            except Exception as e:
                return f"Ошибка: {str(e)}"
        return output.getvalue() or "Код выполнен успешно."