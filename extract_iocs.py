import re
import sys
from pathlib import Path

DEFAULT_FILE = Path(__file__).parent / "data" / "sample_phishing_email.eml"

PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "url": re.compile(r"\b(?:hxxps?|https?)://[^\s<>'\"]+", re.I),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "hash_md5": re.compile(r"\b[a-f0-9]{32}\b", re.I),
    "hash_sha1": re.compile(r"\b[a-f0-9]{40}\b", re.I),
    "hash_sha256": re.compile(r"\b[a-f0-9]{64}\b", re.I),
    "domain": re.compile(r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,}|invalid)\b", re.I),
}

def unique_sorted(items):
    return sorted(set(items), key=str.lower)

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILE
    if not path.exists():
        raise SystemExit(f"Input file not found: {path}")
    text = path.read_text(encoding="utf-8", errors="replace")
    print(f"=== IOC EXTRACTION REPORT ===\nInput: {path.name}")
    for label, pattern in PATTERNS.items():
        values = unique_sorted(pattern.findall(text))
        print(f"\n{label.upper()} ({len(values)}):")
        if values:
            for value in values:
                print(f"  {value}")
        else:
            print("  None found")
    print("\nAnalyst note: extraction is pattern-based; validate context and defanged indicators manually.")
    print("Do not visit suspicious URLs or upload confidential data to public scanning services.")

if __name__ == "__main__":
    main()
