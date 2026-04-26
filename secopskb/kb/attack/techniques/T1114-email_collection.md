---
mitre_id: "T1114"
mitre_name: "Email Collection"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1608f3e1-598a-42f4-a01a-2e252e81728f"
mitre_created: "2017-05-31T21:31:25.454Z"
mitre_modified: "2025-10-24T17:48:26.463Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1114/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "macOS"
  - "Linux"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0009"
d3fend_ids:
  - "D3-ACH"
  - "D3-CF"
  - "D3-CI"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-DI"
  - "D3-DRA"
  - "D3-EF"
  - "D3-EFA"
  - "D3-EHB"
  - "D3-ER"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HD"
  - "D3-LFP"
  - "D3-LLM"
  - "D3-NNI"
  - "D3-PLM"
  - "D3-RC"
  - "D3-RE"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RNA"
  - "D3-SMRA"
  - "D3-SRA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may target user email to collect sensitive information. Emails may contain sensitive data, including trade secrets or personal information, that can prove valuable to adversaries. Emails may also contain details of ongoing incident response operations, which may allow adversaries to adjust their techniques in order to maintain persistence or evade defenses.(Citation: TrustedSec OOB Communications)(Citation: CISA AA20-352A 2021) Adversaries can collect or forward email from mail servers or clients. 

## Workspace

- [[workspaces/attack/techniques/T1114-email_collection-note|Open workspace note]]

![[workspaces/attack/techniques/T1114-email_collection-note]]

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-ACH-application_configuration_hardening|D3-ACH: Application Configuration Hardening]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-DRA-disable_remote_access|D3-DRA: Disable Remote Access]]
- [[D3-EF-email_filtering|D3-EF: Email Filtering]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-EHB-endpoint_health_beacon|D3-EHB: Endpoint Health Beacon]]
- [[D3-ER-email_removal|D3-ER: Email Removal]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HD-homoglyph_detection|D3-HD: Homoglyph Detection]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-LLM-logical_link_mapping|D3-LLM: Logical Link Mapping]]
- [[D3-NNI-network_node_inventory|D3-NNI: Network Node Inventory]]
- [[D3-PLM-physical_link_mapping|D3-PLM: Physical Link Mapping]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RE-restore_email|D3-RE: Restore Email]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RNA-restore_network_access|D3-RNA: Restore Network Access]]
- [[D3-SMRA-sender_mta_reputation_analysis|D3-SMRA: Sender MTA Reputation Analysis]]
- [[D3-SRA-sender_reputation_analysis|D3-SRA: Sender Reputation Analysis]]

## Subtechniques

### T1114.001: Local Email Collection

^t1114001-local-email-collection

Adversaries may target user email on local systems to collect sensitive information. Files containing email data can be acquired from a user’s local system, such as Outlook storage or cache files.

Outlook stores data locally in offline data files with an extension of .ost. Outlook 2010 and later supports .ost file sizes up to 50GB, while earlier versions of Outlook support up to 20GB.(Citation: Outlook File Sizes) IMAP accounts in Outlook 2013 (and earlier) and POP accounts use Outlook Data Files (.pst) as opposed to .ost, whereas IMAP accounts in Outlook 2016 (and later) use .ost files. Both types of Outlook data files are typically stored in `C:\Users\<username>\Documents\Outlook Files` or `C:\Users\<username>\AppData\Local\Microsoft\Outlook`.(Citation: Microsoft Outlook Files)

### T1114.002: Remote Email Collection

^t1114002-remote-email-collection

Adversaries may target an Exchange server, Office 365, or Google Workspace to collect sensitive information. Adversaries may leverage a user's credentials and interact directly with the Exchange server to acquire information from within a network. Adversaries may also access externally facing Exchange services, Office 365, or Google Workspace to access email using credentials or access tokens. Tools such as [[mailsniper|MailSniper (S0413)]] can be used to automate searches for specific keywords.

### T1114.003: Email Forwarding Rule

^t1114003-email-forwarding-rule

Adversaries may setup email forwarding rules to collect sensitive information. Adversaries may abuse email forwarding rules to monitor the activities of a victim, steal information, and further gain intelligence on the victim or the victim’s organization to use as part of further exploits or operations.(Citation: US-CERT TA18-068A 2018) Furthermore, email forwarding rules can allow adversaries to maintain persistent access to victim's emails even after compromised credentials are reset by administrators.(Citation: Pfammatter - Hidden Inbox Rules) Most email clients allow users to create inbox rules for various email functions, including forwarding to a different recipient. These rules may be created through a local email application, a web interface, or by command-line interface. Messages can be forwarded to internal or external recipients, and there are no restrictions limiting the extent of this rule. Administrators may also create forwarding rules for user accounts with the same considerations and outcomes.(Citation: Microsoft Tim McMichael Exchange Mail Forwarding 2)(Citation: Mac Forwarding Rules)

Any user or administrator within the organization (or adversary with valid credentials) can create rules to automatically forward all received messages to another recipient, forward emails to different locations based on the sender, and more. Adversaries may also hide the rule by making use of the Microsoft Messaging API (MAPI) to modify the rule properties, making it hidden and not visible from Outlook, OWA or most Exchange Administration tools.(Citation: Pfammatter - Hidden Inbox Rules)

In some environments, administrators may be able to enable email forwarding rules that operate organization-wide rather than on individual inboxes. For example, Microsoft Exchange supports transport rules that evaluate all mail an organization receives against user-specified conditions, then performs a user-specified action on mail that adheres to those conditions.(Citation: Microsoft Mail Flow Rules 2023) Adversaries that abuse such features may be able to enable forwarding on all or specific mail an organization receives. 

## Mitigations

- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1047-audit|M1047: Audit]]
- [[M1060-out-of-band_communications_channel|M1060: Out-of-Band Communications Channel]]

## Platforms

- Windows
- macOS
- Linux
- Office Suite

