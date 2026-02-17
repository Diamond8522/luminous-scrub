import math
import re

class LuminousScanner:
    """A tuned sentinel that distinguishes between creative chaos and actual leaks."""
    
    def __init__(self):
        # Sharpened patterns to catch specific 'Mercenary' secrets
        self.patterns = [
            r"(?i)(api_key|secret|token|password|auth|credential)\s*[:=]\s*['\"].+['\"]",
            r"(sk|ak|as)-[a-zA-Z0-9]{32,}",
            r"(?i)key-[a-zA-Z0-9]{32,}"
        ]

    def calculate_entropy(self, data):
        """Calculates Shannon Entropy. 0 is static; 8 is pure noise."""
        if not data:
            return 0
        entropy = 0
        for x in range(256):
            p_x = float(data.count(chr(x))) / len(data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        return round(entropy, 2)

    def scan(self, content):
        entropy = self.calculate_entropy(content)
        
        # Check for any regex matches (The 'Smoking Gun')
        found_leaks = []
        for pattern in self.patterns:
            matches = re.findall(pattern, content)
            if matches:
                found_leaks.extend(matches)
        
        # 🦾 THE INTELLIGENT GATE:
        # We mark as BRUISED if:
        # 1. We found a regex match (High confidence leak)
        # 2. OR Entropy is > 5.5 (Prevents emojis/code syntax from false alarms)
        is_bruised = len(found_leaks) > 0 or entropy > 5.5
        
        return {
            "entropy": entropy, 
            "leaks_found": len(found_leaks), 
            "status": "BRUISED" if is_bruised else "LUMINOUS"
        }
