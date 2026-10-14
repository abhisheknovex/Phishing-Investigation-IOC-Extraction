# Phishing Investigation & IOC Extraction

## Objective
Investigate a synthetic phishing email and extract candidate email addresses, URLs, domains, IP addresses, and file hashes using Python regular expressions.

## Files
- `data/sample_phishing_email.eml` — synthetic, non-operational training email
- `extract_iocs.py` — IOC extraction utility
- `investigation_report.md` — example analyst case report

## Run
```bash
python3 extract_iocs.py
```
Or provide a different text file:
```bash
python3 extract_iocs.py /path/to/authorized/sample.txt
```

## Investigation checklist
1. Review sender display name and actual sender address.
2. Inspect reply-to, return-path, SPF/DKIM/DMARC results if headers are available.
3. Defang links before documenting them.
4. Do not click the URL or open unexpected attachments on a normal workstation.
5. Check endpoint, proxy, DNS, browser, and identity logs to determine whether anyone clicked, submitted credentials, or downloaded a file.
6. Record evidence, timestamps, affected users, confidence, and recommended actions.
7. Follow the organization's incident-response playbook and escalate when required.

## Important limitations
- Regex extraction produces candidate IOCs, not a verdict that an email is malicious.
- The sample uses the reserved `.invalid` domain and a defanged `hxxp` URL.
- No live threat-intelligence lookup is performed.
- Never upload confidential emails, customer data, or internal indicators to public services without authorization.
