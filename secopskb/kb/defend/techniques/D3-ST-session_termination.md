---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ST"
d3fend_name: "Session Termination"
d3fend_ontology_id: "d3f:SessionTermination"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASessionTermination/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1021"
  - "T1021.001"
  - "T1021.004"
  - "T1133"
  - "T1134"
  - "T1134.003"
  - "T1199"
  - "T1563"
  - "T1563.001"
  - "T1563.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Forcefully end all active sessions associated with compromised accounts or devices.

## Workspace

- [[workspaces/defend/techniques/D3-ST-session_termination-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ST-session_termination-note]]

## Parent Technique

- [[D3-PE-process_eviction|D3-PE: Process Eviction]]

## Related ATT&CK Techniques

- [[T1021-remote_services|T1021: Remote Services]]
- [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
- [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]]
- [[T1133-external_remote_services|T1133: External Remote Services]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]]
- [[T1199-trusted_relationship|T1199: Trusted Relationship]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
- [[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]]
- [[T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]

## Knowledge Base Article

Defined in NIST 800-53 as AC-12.

## Ontology Relationships

- [[D3-PE-process_eviction|D3-PE: Process Eviction]]

