---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SPP"
d3fend_name: "Strong Password Policy"
d3fend_ontology_id: "d3f:StrongPasswordPolicy"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AStrongPasswordPolicy/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1110"
  - "T1110.001"
  - "T1110.002"
  - "T1110.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Modifying system configuration to increase password strength.

## Workspace

- [[workspaces/defend/techniques/D3-SPP-strong_password_policy-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SPP-strong_password_policy-note]]

## Parent Technique

- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]

## Child Techniques

- [[D3-CDP-change_default_password|D3-CDP: Change Default Password]]

## Related ATT&CK Techniques

- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
- [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]

## Knowledge Base Article

## How it works
Password strength guidelines include increasing password length, permitting passwords that contain ASCII or Unicode characters, and requiring systems to screen new passwords against lists of commonly used or compromised passwords.
## Considerations
Extremely complex password requirements may lead users to saving passwords in text files or picking obvious passwords that meet the policy.

## Ontology Relationships

- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]

