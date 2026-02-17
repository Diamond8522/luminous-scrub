import sys
import os
from core.scanner import LuminousScanner

def scan_file(scanner, filepath):
    """Audits a single file without crashing on binary or noise."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            data = f.read()
            report = scanner.scan(data)
            
            if report['status'] == "BRUISED":
                print(f"⚠️  BRUISED: {filepath} | Entropy: {report['entropy']} | Leaks: {report['leaks_found']}")
                return True
            return False
    except Exception:
        return False

def main():
    scanner = LuminousScanner()
    leaks_found = False
    
    # 🛡️ THE MIRROR SHIELD: Ignore the scanner's own files
    ignored_files = {'main.py', 'requirements.txt', 'Cargo.lock', '.gitignore'}
    ignored_dirs = {'.git', '.venv', 'target', 'core', '__pycache__'} # 'core' is critical
    ignored_exts = {'.png', '.jpg', '.gguf', '.exe', '.bin', '.so', '.rlib'}

    if len(sys.argv) > 1:
        target_path = sys.argv[1]
        if os.path.isdir(target_path):
            print(f"🌌 [LUMINOUS-SCRUB]: Auditing directory: {target_path}")
            for root, dirs, files in os.walk(target_path):
                # Prune ignored folders so we don't even enter them
                dirs[:] = [d for d in dirs if d not in ignored_dirs]
                
                for file in files:
                    if file in ignored_files or any(file.endswith(ext) for ext in ignored_exts):
                        continue
                    filepath = os.path.join(root, file)
                    if scan_file(scanner, filepath):
                        leaks_found = True
        elif os.path.exists(target_path):
            leaks_found = scan_file(scanner, target_path)
    else:
        # Internal self-check (Non-leaking string)
        print("🌌 [LUMINOUS-SCRUB]: Testing internal pulse...")
        report = scanner.scan("The phoenix rises in the violet light.")
        if report['status'] == "BRUISED":
            leaks_found = True

    if leaks_found:
        print("\n❌ The shadows are compromised.")
        sys.exit(1)
    else:
        print("\n✅ The matrix is clear.")

if __name__ == "__main__":
    main()
