---
mitre_id: "T1672"
mitre_name: "Email Spoofing"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e1c2db92-7ae3-4e6a-90b4-157c1c1565cb"
mitre_created: "2025-03-24T16:52:14.061Z"
mitre_modified: "2025-09-24T21:03:46.869Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1672/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Office Suite"
  - "Windows"
  - "macOS"
  - "Linux"
mitre_tactic_ids:
  - "TA0005"
---

# T1672: Email Spoofing

Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order to establish contact with victims under false pretenses.(Citation: Proofpoint TA427 April 2024) In addition to actual email content, email headers (such as the FROM header, which contains the email address of the sender) may also be modified. Email clients display these headers when emails appear in a victim's inbox, which may cause modified emails to appear as if they were from the spoofed entity. 

This behavior may succeed when the spoofed entity either does not enable or enforce identity authentication tools such as Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and/or Domain-based Message Authentication, Reporting and Conformance (DMARC).(Citation: Cloudflare DMARC, DKIM, and SPF)(Citation: DMARC-overview)(Citation: Proofpoint-DMARC) Even if SPF and DKIM are configured properly, spoofing may still succeed when a domain sets a weak DMARC policy such as `v=DMARC1; p=none; fo=1;`. This means that while DMARC is technically present, email servers are not instructed to take any filtering action when emails fail authentication checks.(Citation: Proofpoint TA427 April 2024)(Citation: ic3-dprk)

Adversaries may abuse Microsoft 365’s Direct Send functionality to spoof internal users by using internal devices like printers to send emails without authentication.(Citation: Barnea DirectSend) Adversaries may also abuse absent or weakly configured SPF, SKIM, and/or DMARC policies to conceal social engineering attempts(Citation: ic3-dprk) such as [[T1566-phishing|T1566: Phishing]]. They may also leverage email spoofing for [[T1656-impersonation|T1656: Impersonation]] of legitimate external individuals and organizations, such as journalists and academics.(Citation: ic3-dprk)

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Mitigations

- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Office Suite
- Windows
- macOS
- Linux

