---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CS"
d3fend_name: "Credential Scrubbing"
d3fend_ontology_id: "d3f:CredentialScrubbing"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ACredentialScrubbing/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1505"
  - "T1505.001"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

The systematic removal of hard-coded credentials from source code to prevent accidental exposure and unauthorized access.

## Workspace

- [[workspaces/defend/techniques/D3-CS-credential_scrubbing-note|Open workspace note]]

![[workspaces/defend/techniques/D3-CS-credential_scrubbing-note]]

## Parent Technique

- [[D3-SCH-source_code_hardening|D3-SCH: Source Code Hardening]]

## Related ATT&CK Techniques

- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]

## Knowledge Base Article

## How it Works
Credential Scrubbing involves identifying and eliminating hard-coded credentials such as usernames, passwords, API keys, and tokens from source code repositories. These credentials should be managed securely using environment variables, secret management tools, or secure vaults where they can be safely accessed when needed.

## Considerations
* Developers should conduct regular audits of source code to ensure credentials are not hard-coded.
* Exposed credentials found in version control history must be disabled and replaced promptly.
* Adopt role-based access controls and credential rotation policies to minimize security risks.

## See Also

- d3f:CWE-798
- https://capec.mitre.org/data/definitions/191.html

## Ontology Relationships

- [[D3-SCH-source_code_hardening|D3-SCH: Source Code Hardening]]

