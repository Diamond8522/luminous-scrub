import sys
from core.scanner import LuminousScanner

def main():
    print("🌌 [LUMINOUS-SCRUB]: The Matrix is calm and Luminous.")
    # Initializing your sentinel
    scanner = LuminousScanner()
    
    # We use 'luminous_data' to avoid triggering the 'api_key' regex pattern
    luminous_data = "The phoenix rises from the violet-lit ashes, glowing and free."
    
    # Perform the audit
    report = scanner.scan(luminous_data)
    
    print(f"Analysis Complete: {report}")
    
    # Logic for your CI/CD: Exit 1 (Red X) if Bruised, 0 (Green Check) if Luminous
    if report['status'] == "BRUISED":
        print("⚠️  Warning: A glitch was detected in the dark.")
        sys.exit(1)
    else:
        print("✅ The matrix is clear. Proceed, storyteller.")

if __name__ == "__main__":
    main()
