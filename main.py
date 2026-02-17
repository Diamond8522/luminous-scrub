import sys
import os
from core.scanner import LuminousScanner

def scan_file(scanner, filepath):
    """The surgical strike: audit a single file's content."""
    try:
        # errors='ignore' ensures we don't crash on weird binary characters
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            data = f.read()
            report = scanner.scan(data)
            
            if report['status'] == "BRUISED":
                print(f"⚠️  BRUISED: {filepath} | Entropy: {report['entropy']} | Leaks: {report['leaks_found']}")
                return True
            return False
    except Exception:
        # If a file is unreadable, it's a ghost we can't hunt
        return False

def main():
    scanner = LuminousScanner()
    leaks_found = False
    
    # 🛡️ THE EXCLUSION LIST: Prevents the scanner from flagging its own code
    ignored_files = {
        'Cargo.lock', 'package-lock.json', 'go.sum', '.gitignore', 
        'main.py', 'requirements.txt'
    }
    
    # Pruning these folders ensures build artifacts and the scanner's own logic are skipped
    ignored_dirs = {
        '.git', '.venv', '__pycache__', 'node_modules', 
        'target', 'build', 'dist', 'core' 
    }
    
    ignored_exts = {
        '.png', '.jpg', '.jpeg', '.gguf', '.exe', '.bin', 
        '.pyc', '.so', '.rlib', '.d', '.rmeta'
    }

    if len(sys.argv) > 1:
        target_path = sys.argv[1]
        
        if os.path.isdir(target_path):
            print(f"🌌 [LUMINOUS-SCRUB]: Hunting ghosts in directory: {target_path}")
            for root, dirs, files in os.walk(target_path):
                # CRITICAL: Prune the search tree so we NEVER enter ignored folders
                dirs[:] = [d for d in dirs if d not in ignored_dirs]
                
                for file in files:
                    if file in ignored_files or any(file.endswith(ext) for ext in ignored_exts):
                        continue
                        
                    filepath = os.path.join(root, file)
                    if scan_file(scanner, filepath):
                        leaks_found = True
                        
        elif os.path.exists(target_path):
            print(f"🌌 [LUMINOUS-SCRUB]: Auditing file: {target_path}...")
            leaks_found = scan_file(scanner, target_path)
    else:
        # Internal spark test for self-diagnostics
        print("🌌 [LUMINOUS-SCRUB]: Searching for glitches in the matrix...")
        test_data = "The phoenix rises, violet-lit and free."
        report = scanner.scan(test_data)
        if report['status'] == "BRUISED":
            print(f"⚠️  Warning: Internal test failed. Status: {report}")
            leaks_found = True

    # Final Exit Logic: Returns 0 for success (green), 1 for failure (red)
    if leaks_found:
        print("\n❌ The shadows are compromised. Clean the matrix.")
        sys.exit(1)
    else:
        print("\n✅ The matrix is clear. Proceed, storyteller.")

if __name__ == "__main__":
    main()
