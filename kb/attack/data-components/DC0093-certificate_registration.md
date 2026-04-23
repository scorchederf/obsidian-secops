---
mitre_id: "DC0093"
mitre_name: "Certificate Registration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--1dad5aa4-4bb5-45e4-9e42-55d40003cfa6"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

# DC0093: Certificate Registration

Certificate Registration refers to the collection and analysis of information about digital certificates, including current, revoked, and expired certificates. Sources such as Certificate Transparency logs and other public resources provide visibility into certificates issued for specific domains or organizations. Monitoring certificate registrations can help identify potential misuse, such as unauthorized certificates or signs of adversary reconnaissance. Examples: 

- Certificate Transparency Logs: These logs record the issuance of SSL/TLS certificates by trusted Certificate Authorities (CAs).
- Revoked Certificates: Information about certificates that have been invalidated before their expiration date.
- Expired Certificates: Reports of expired certificates for a domain, which may indicate lax security practices or opportunities for adversaries to exploit expired credentials.
- Domain Monitoring for Certificates: Maps SSL/TLS certificates to domains and subdomains, helping to identify any rogue certificates.
- Public Certificate Directories: Services providing APIs to query issued certificates for analysis.

This data component can be collected through the following measures:

Use Certificate Transparency Monitors

- Tools like crt.sh, CertStream, or APIs provided by certificate authorities (CAs) allow you to monitor issued certificates in real-time.
- Example: Use CertStream to stream certificate issuance logs and filter for domains of interest.

Analyze Certificate Revocation Sources

- Monitor CRLs or query OCSP responders to detect revoked certificates.
- Configure tools like OpenSSL or browsers to validate certificate revocation status automatically.

Leverage Public Scanning Tools

- Use tools such as SSL Labs, Censys, or Shodan to scan for certificate details related to your domain or network.

Automate Certificate Monitoring

- Set up automated scripts or services to parse Certificate Transparency logs for anomalies.
- Example: Automate searches on crt.sh to identify certificates issued for typo-squatted domains.

Integrate with Threat Intelligence

- Enrich certificate data with threat intelligence feeds to detect connections to known adversary-controlled infrastructure.
- Tools like VirusTotal can identify malicious certificates based on associated indicators.

## Workspace

- [[kb/notes/attack/data-components/dc0093-notes|Open workspace note]]

