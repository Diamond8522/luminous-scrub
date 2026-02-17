import sys
from core.scanner import LuminousScanner

def main():
    print("🌌 [LUMINOUS-SCRUB]: Searching for glitches in the matrix...")
    scanner = LuminousScanner()
    
    # Example logic: checking a local string
    test_data = "api_key = 'CLEAN_AND_LUMINOUS_DATA'"
    report = scanner.scan(test_data)
    
    print(f"Analysis Complete: {report}")
    if report['leaks_found'] > 0:
        print("⚠️  Warning: Secrets detected. Keep it in the dark.")
        sys.exit(1)

if __name__ == "__main__":
    main()
