---
mitre_id: "M1060"
mitre_name: "Out-of-Band Communications Channel"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--80a0e940-f683-4fbd-ac00-e9f935f2f808"
mitre_created: "2024-08-30T13:08:10.349Z"
mitre_modified: "2024-10-12T15:34:54.912Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1060/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Establish secure out-of-band communication channels to ensure the continuity of critical communications during security incidents, data integrity attacks, or in-network communication failures. Out-of-band communication refers to using an alternative, separate communication path that is not dependent on the potentially compromised primary network infrastructure. This method can include secure messaging apps, encrypted phone lines, satellite communications, or dedicated emergency communication systems. Leveraging these alternative channels reduces the risk of adversaries intercepting, disrupting, or tampering with sensitive communications and helps coordinate an effective incident response.(Citation: TrustedSec OOB Communications)(Citation: NIST Special Publication 800-53 Revision 5)

## Workspace

- [[workspaces/attack/mitigations/M1060-out-of-band_communications_channel-note|Open workspace note]]

![[workspaces/attack/mitigations/M1060-out-of-band_communications_channel-note]]

## Mitigates Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection|T1114: Email Collection]]
    - [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
    - [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]
    - [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
    - [[T1213-data_from_information_repositories#^t1213005-messaging-applications|T1213.005: Messaging Applications]]
- [[T1489-service_stop|T1489: Service Stop]]

