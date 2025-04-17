from PyPDF2 import PdfReader
import docx
import pandas as pd
import os
import asyncio
from datetime import datetime

class FileAnalyzer:
    async def read_file(self, file_path):
        if file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        elif file_path.endswith(".docx"):
            doc = docx.Document(file_path)
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            return df.to_string()
        else:
            return "Формат файла не поддерживается."

    async def modify_file(self, file_path, action):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_path = f"data/output/modified_{os.path.basename(file_path)}_{timestamp}"

        if action.lower().startswith("формат на txt"):
            content = await self.read_file(file_path)
            output_path += ".txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            return output_path
        elif action.lower().startswith("структуру"):
            content = await self.read_file(file_path)
            lines = content.split("\n")
            lines.sort()
            output_path += os.path.splitext(file_path)[1]
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            return output_path
        elif action == "auto":
            content = await self.read_file(file_path)
            output_path += ".txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            return output_path
        else:
            return f"Действие '{action}' не поддерживается."