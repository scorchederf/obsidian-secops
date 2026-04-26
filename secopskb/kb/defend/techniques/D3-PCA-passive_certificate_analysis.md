---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PCA"
d3fend_name: "Passive Certificate Analysis"
d3fend_ontology_id: "d3f:PassiveCertificateAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3APassiveCertificateAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Collecting host certificates from network traffic or other passive sources like a certificate transparency log and analyzing them for unauthorized activity.

## Workspace

- [[workspaces/defend/techniques/D3-PCA-passive_certificate_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-PCA-passive_certificate_analysis-note]]

## Parent Technique

- [[D3-CA-certificate_analysis|D3-CA: Certificate Analysis]]

## Knowledge Base Article

## How it works
Certificates are analyzed outside of a TLS server connection using third-party secure update logs, domain name analysis and analytics.

### Secure update certificate logs
* Certificate Logs
The key enabling feature is a secure service that maintains record logs of certificate activities. The logs allow users to only append certificates and never to delete or modify the log entries. The logs use Merkle Tree Hashes to ensure they have not been tampered with. The logging service also allows for public auditing by any user.

The logging service, upon receipt of a certificate to log, will respond with a signed certificate timestamp (SCT). The SCT guarantees the certificate will be added to the log within the time specified. The SCT must be present with the certificate during a TLS handshake.

* Certificate Monitoring
Certificate monitoring, of the logs, is typically done by the CA and they watch for suspicious certificate logging and unusual certificates or extensions or permissions. Monitors are also responsible for verifying the logs are accurate and public.

* Certificate Auditors
Log integrity is verified by log auditors. Auditors make use of log proofs are used to validate the cryptographic hashes (Merkle Trees) that the log employs are consistent. In order to ensure consistency throughout multiple monitors and auditors, sharing a common logging service, gossip protocol is employed.

### Phishing domain name analysis
* A curated corpus of known benign domains and phishing domain names is used as training text for machine learning. Through the use of feature set extraction, vectors labels are created with scoring to indicated if they are considered benign or phishing domains.

* A stream of new or updated SSL certificates with fully qualified domain names (FQDN) is analyzed against the feature vectors and a predictive model determines a score for the domains. The scoring considers distance measures such as Levenshtein distance to help in determining the final label score. Supervised learning is also employed using the curated domains of benign and phishing domains.

* Subdomain phishing analysis, prepending a trusted domain to a phishing domain, and regular expression comparisons  are also used in the label scoring model. A tunable measure is used to determine the threshold for alerting. This measure helps to balance between precision and recall measures.

## Considerations
* Some entity will need to run the logging service and a trusted entity is preferred.
* Certificate Authorities will likely need to monitor the logging service for consistency.
* Certificate revocation is unchanged and remains outside of Certificate Transparency, but certificates needing to be revoked are visible.
* Technique dependent of reliable feed of new and updated certificates
* Some certificate authorities allow for certificates to be registered with wildcards in the FQDN and thus will fail some of the subdomain scoring
* Phishing HTTP domains will not be discovered

## Ontology Relationships

- [[D3-CA-certificate_analysis|D3-CA: Certificate Analysis]]

