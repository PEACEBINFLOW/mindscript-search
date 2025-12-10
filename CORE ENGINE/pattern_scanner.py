import re

class PatternScanner:
    def find_stages(self, text):
        return re.findall(r"<STAGE_(.*?)>", text)

    def detect_prompt_dna(self, text):
        return hash(text.strip())
