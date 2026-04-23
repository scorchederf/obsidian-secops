---
mitre_id: "T1534"
mitre_name: "Internal Spearphishing"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--9e7452df-5144-4b6e-b04a-b66dd4016747"
mitre_created: "2019-09-04T19:26:12.441Z"
mitre_modified: "2025-10-24T17:49:09.394Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1534/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "macOS"
  - "Linux"
  - "SaaS"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0008"
d3fend_ids:
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-DI"
  - "D3-EF"
  - "D3-EFA"
  - "D3-ER"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HD"
  - "D3-LFP"
  - "D3-RE"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SMRA"
  - "D3-SRA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

# T1534: Internal Spearphishing

After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating [[T1656-impersonation|T1656: Impersonation]].(Citation: Trend Micro - Int SP)

For example, adversaries may leverage [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]] or [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]] as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through [[T1056-input_capture|T1056: Input Capture]] on sites that mimic login interfaces.

Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials.(Citation: Int SP - chat apps)

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-EF-email_filtering|D3-EF: Email Filtering]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-ER-email_removal|D3-ER: Email Removal]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HD-homoglyph_detection|D3-HD: Homoglyph Detection]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RE-restore_email|D3-RE: Restore Email]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SMRA-sender_mta_reputation_analysis|D3-SMRA: Sender MTA Reputation Analysis]]
- [[D3-SRA-sender_reputation_analysis|D3-SRA: Sender Reputation Analysis]]

## Platforms

- Windows
- macOS
- Linux
- SaaS
- Office Suite

## Workspace

- [[kb/notes/attack/techniques/t1534-notes|Open workspace note]]

