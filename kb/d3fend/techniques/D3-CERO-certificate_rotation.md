---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CERO"
d3fend_name: "Certificate Rotation"
d3fend_ontology_id: "d3f:CertificateRotation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ACertificateRotation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1649"
---

# D3-CERO: Certificate Rotation

Certificate rotation involves replacing digital certificates and their private keys to maintain cryptographic integrity and trust, mitigating key compromise risks and ensuring continuous secure communications.

## Parent Technique

- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]

## Related ATT&CK Techniques

- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]

## Knowledge Base Article

## How it works

Certificate rotation should be performed when:
- Any certificate expires.
- A new CA authority is substituted for the old, thus requiring a replacement root certificate.
- New or modified constraints need to be imposed on one or more certificates.
- A security breach has occurred.

Considerations:
- Managing certificate rotation across an enterprise can be complex. Automated solutions, sold by multiple vendors, should be considered to manage this complexity.

## See Also

- https://docs.couchbase.com/server/7.0/manage/manage-security/rotate-server-certificates.html

## Ontology Relationships

- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-cero-notes|Open workspace note]]

