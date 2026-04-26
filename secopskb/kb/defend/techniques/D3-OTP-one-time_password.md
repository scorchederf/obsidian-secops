---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-OTP"
d3fend_name: "One-time Password"
d3fend_ontology_id: "d3f:One-timePassword"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AOne-timePassword/"
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

A one-time password is valid for only one user authentication.

## Workspace

- [[workspaces/defend/techniques/D3-OTP-one-time_password-note|Open workspace note]]

![[workspaces/defend/techniques/D3-OTP-one-time_password-note]]

## Parent Technique

- [[D3-PR-password_rotation|D3-PR: Password Rotation]]

## Related ATT&CK Techniques

- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
- [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]

## Knowledge Base Article

## How it works

When a user initiates authentication, they are asked for a one-time password, often in addition to other credentials such as a traditional password or smart card. The one-time password may be from a list provided in advance, sent via a channel such as SMS or HTTPS to an app, or a generated token.

In the case of a physical token which generates one-time passwords incrementally based on time elapsed, that token device need not be connected to the internet. In different implementations, an administrator of the system, or a user with additional verification, can adjust for clock skew between the token and the verification system as needed.

## Considerations

### Compromise of delivery channel
- SIM Swapping
- Secure token visual compromise
- Insecure delivery channel

### Compromise of delivery device
Physical loss of One-time Password device.

### Compromise of long-term backup codes
These are often provided in the form of a downloadable document with a regular name, which can be searched for in the case that the user forgets where they put them.  This digital file or printed document could be stolen.
Additionally, after the code file is printed, it could be recovered from the system printer spool unless the spooler cache is cleared.

## See Also

- dbr:One-time_password

## Ontology Relationships

- [[D3-PR-password_rotation|D3-PR: Password Rotation]]

