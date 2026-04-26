---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PR"
d3fend_name: "Password Rotation"
d3fend_ontology_id: "d3f:PasswordRotation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3APasswordRotation/"
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

Password rotation is a security policy that mandates the periodic change of user account passwords to mitigate the risk of unauthorized access due to compromised credentials.

## Workspace

- [[workspaces/defend/techniques/D3-PR-password_rotation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-PR-password_rotation-note]]

## Parent Technique

- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]

## Child Techniques

- [[D3-OTP-one-time_password|D3-OTP: One-time Password]]

## Related ATT&CK Techniques

- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
- [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]

## Knowledge Base Article

## How it works

Users may be requested to change their passwords on a regular schedule. Management servers with enterprise policies for account management provide the ability to change or reset passwords for accounts.

## Considerations

Requiring users to change their passwords frequently can result in insecure password practices by the user. The latest update of NIST SP 800-63B, Digital Identity Guidelines, recommends requiring password reset only when a known compromise has occurred, or every 365 days, rather than every 60 or 90 days.

## See Also

- https://pages.nist.gov/800-63-3/sp800-63-3.html
- https://www.auditboard.com/blog/nist-password-guidelines/

## Ontology Relationships

- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]

