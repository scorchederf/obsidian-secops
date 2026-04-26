---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ACA"
d3fend_name: "Active Certificate Analysis"
d3fend_ontology_id: "d3f:ActiveCertificateAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AActiveCertificateAnalysis/"
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

Actively collecting PKI certificates by connecting to the server and downloading its server certificates for analysis.

## Workspace

- [[workspaces/defend/techniques/D3-ACA-active_certificate_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ACA-active_certificate_analysis-note]]

## Parent Technique

- [[D3-CA-certificate_analysis|D3-CA: Certificate Analysis]]

## Knowledge Base Article

## How it works
Analysis of server certificates using active methods to detect if certificates have been misconfigured or spoofed by using elements of the certificate, certificate authorities and signatures.

### Certificate validity analysis
This can be accomplished by verifying the digital signature on certificate.

### Certificate path analysis
The client's browser can perform path verification to ensure that the server's certificate contains a valid trust anchor.

### Certificate configuration analysis
Some browsers can be configured to implement the key-usage extensions contained certificates. This can help to prevent a certificate from being misused.

### Certificate revocation status analysis
Using either Certificate Revocation Lists (CRLs) or Online Certificate Status Protocol (OCSP) to determine the revocation status. OCSP Stapling, binding the status with the certificate, helps to mitigate potential delay in status verifications.

## Considerations
* Management of the PKI across the enterprise typically requires automation to maintain scalability and flexibility
* If the certificate authority, issuing the certificate, is compromised then all of the certificates issued by the CA are suspect
* There may be delays associated with updates to certificates
* Revoked certificates give the appearance of valid certificates until they are published to a trusted revocation service (OCSP or CRL)
* The revocation service (OCSP or CRL) may be down during our connection and a browser will need to make a decision will need to be made about trusting the connection

## Ontology Relationships

- [[D3-CA-certificate_analysis|D3-CA: Certificate Analysis]]

