from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []
    def valid_extension(self, extension):
        self.extension = extension
        extension in Parser.extensions
