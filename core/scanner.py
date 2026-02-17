import math
import re

class LuminousScanner:
    """A resilient hunter for secrets and chaos."""
    def __init__(self):
        # Tracking standard patterns that shouldn't be in the wild
        self.patterns = [
            r"(?i)api_key\s*[:=]\s*['\"].+['\"]",
            r"(?i)secret\s*[:=]\s*['\"].+['\"]",
            r"sk-[a-zA-Z0-9]{48}" # OpenAI Key Pattern
        ]

    def calculate_entropy(self, data):
        """Math to find high-randomness (potential keys)."""
        if not data: return 0
        entropy = 0
        for x in range(256):
            p_x = float(data.count(chr(x))) / len(data)
            if p_x > 0: entropy += - p_x * math.log(p_x, 2)
        return round(entropy, 2)

    def scan(self, content):
        entropy = self.calculate_entropy(content)
        leaks = [p for p in self.patterns if re.search(p, content)]
        return {"entropy": entropy, "leaks_found": len(leaks), "status": "LUMINOUS" if not leaks else "BRUISED"}
