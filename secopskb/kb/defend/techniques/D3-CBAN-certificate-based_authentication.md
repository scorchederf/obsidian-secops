---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CBAN"
d3fend_name: "Certificate-based Authentication"
d3fend_ontology_id: "d3f:Certificate-basedAuthentication"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ACertificate-basedAuthentication/"
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

Requiring a digital certificate in order to authenticate a user.

## Workspace

- [[workspaces/defend/techniques/D3-CBAN-certificate-based_authentication-note|Open workspace note]]

![[workspaces/defend/techniques/D3-CBAN-certificate-based_authentication-note]]

## Parent Technique

- [[D3-AA-agent_authentication|D3-AA: Agent Authentication]]

## Related ATT&CK Techniques

- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]

## Knowledge Base Article

## How it works

Certificate-based authentication is a security mechanism that uses digital certificates to verify the identity of a user, device, or server before granting access to a network or system. This method relies on a pair of cryptographic keys: a public key and a private key.

## Considerations

* Private Key Protection: Ensure that private keys are securely stored and protected against unauthorized access.
* Certificate Revocation: Implement a robust process for revoking certificates if they are compromised or no longer needed.
* Man-in-the Middle Attacks: Use mutual authentication to mitigate the risk of these attacks.

## Ontology Relationships

- [[D3-AA-agent_authentication|D3-AA: Agent Authentication]]

