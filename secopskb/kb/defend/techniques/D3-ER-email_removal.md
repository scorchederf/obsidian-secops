---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ER"
d3fend_name: "Email Removal"
d3fend_ontology_id: "d3f:EmailRemoval"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AEmailRemoval/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1114"
  - "T1114.001"
  - "T1114.002"
  - "T1505"
  - "T1505.002"
  - "T1534"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The email removal technique deletes email files from system storage.

## Workspace

- [[workspaces/defend/techniques/D3-ER-email_removal-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ER-email_removal-note]]

## Parent Technique

- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
- [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
- [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]

## Knowledge Base Article

## How it works

Email removal is a technique that can be used to prevent a user from executing malware or responding to phishing attempts. Security software or users themselves may detect malicious or suspicious email in a local or remote mail folder email and then employ this technique.

## Considerations

For email that needs to be removed, an infosec organization may choose to take additional follow-up actions (such as blocking the sources or notifying providers), rather than only relying on email deletion.

For the case where users detect likely suspicious email files, the organization should consider implementing a means for reporting these emails to their infosec organization.

Email files may propagate through many storage systems across the an organization's systems over time, so early detection and blocking helps avoid residual, latent stores of malicous email content in the enterprise.

## Ontology Relationships

- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]

