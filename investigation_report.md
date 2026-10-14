# Phishing Investigation Report — Training Case PHISH-001

## Executive summary
A synthetic email impersonates an IT helpdesk and uses urgency to encourage the recipient to submit credentials through a link. The sender and link use the reserved `.invalid` domain, so the sample is non-operational and intended only for training.

## Evidence observed
- Subject: `Urgent: Password expires today`
- Display name: `IT Helpdesk`
- Sender: `helpdesk@example.invalid`
- Candidate URL (defanged): `hxxp://login-example.invalid/verify?user=employee`
- Social engineering: threat of mailbox disablement and request for a password

## Assessment
**Disposition: Suspicious training sample; no real-world maliciousness is asserted.**
The urgency and credential request are common phishing indicators. The `.invalid` domain is reserved and is not evidence of a real attacker infrastructure.

## IOCs extracted
- Email address: `helpdesk@example.invalid`
- Domain: `example.invalid`, `login-example.invalid`
- URL: `hxxp://login-example.invalid/verify?user=employee`
- IP addresses: none
- File hashes: none

## Missing evidence
- Full original headers and authentication results
- Actual recipient/click telemetry
- Proxy/DNS/EDR events
- Attachment metadata or hashes, if any
- Threat-intelligence results from an approved source

## Recommended response
1. Do not click the link or enter credentials.
2. If this were a real message, report it through the approved security channel.
3. Determine whether recipients clicked or submitted credentials using approved logs.
4. If credentials were entered, follow the incident-response playbook for account protection and session revocation.
5. Preserve the original message and relevant logs.

## Analyst caveat
This is a tabletop exercise. No actual mailbox, user, domain, or system was investigated.
