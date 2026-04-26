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
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1649"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Certificate rotation involves replacing digital certificates and their private keys to maintain cryptographic integrity and trust, mitigating key compromise risks and ensuring continuous secure communications.

## Workspace

- [[workspaces/defend/techniques/D3-CERO-certificate_rotation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-CERO-certificate_rotation-note]]

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

