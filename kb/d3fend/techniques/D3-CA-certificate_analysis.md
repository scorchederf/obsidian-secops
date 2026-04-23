---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CA"
d3fend_name: "Certificate Analysis"
d3fend_ontology_id: "d3f:CertificateAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ACertificateAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1041"
  - "T1048"
  - "T1048.002"
  - "T1071"
  - "T1071.001"
  - "T1071.002"
  - "T1071.003"
  - "T1071.004"
  - "T1071.005"
  - "T1573"
  - "T1573.002"
  - "T1649"
---

# D3-CA: Certificate Analysis

Analyzing Public Key Infrastructure certificates to detect if they have been misconfigured or spoofed using both network traffic, certificate fields and third-party logs.

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Child Techniques

- [[D3-ACA-active_certificate_analysis|D3-ACA: Active Certificate Analysis]]
- [[D3-PCA-passive_certificate_analysis|D3-PCA: Passive Certificate Analysis]]

## Related ATT&CK Techniques

- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1048-exfiltration_over_alternative_protocol#^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol|T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1071-application_layer_protocol#^t1071002-file-transfer-protocols|T1071.002: File Transfer Protocols]]
- [[T1071-application_layer_protocol#^t1071003-mail-protocols|T1071.003: Mail Protocols]]
- [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1071-application_layer_protocol#^t1071005-publish-subscribe-protocols|T1071.005: Publish/Subscribe Protocols]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
- [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]

## Knowledge Base Article

## How it works
Certificate Analysis ensures that the data elements of the certificate are current and anchored in a known trust model. Certificate authorities, revocation lists, and third-party secure logs are used in the analysis. Analysis includes detection of server impersonation, phishing domains, and forged certificates.

TLS certificates are designed to expire to ensure that the cryptographic keys are forced to be changed on a regular basis. The certificates in the trust path also expire and can cause a break in the trust chain. This means that even if a server certificate is updated correctly, intermediate certificates can expire and the trust chain is not maintained. This can cause services to become unavailable.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-ca-notes|Open workspace note]]

