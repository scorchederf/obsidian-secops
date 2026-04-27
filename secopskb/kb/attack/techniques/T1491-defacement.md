---
mitre_id: "T1491"
mitre_name: "Defacement"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--5909f20f-3c39-4795-be06-ef1ea40d350b"
mitre_created: "2019-04-08T17:51:41.390Z"
mitre_modified: "2025-10-24T17:48:49.761Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1491/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "ESXi"
mitre_tactic_ids:
  - "TA0040"
d3fend_ids:
  - "D3-DNR"
  - "D3-NRAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may modify visual content available internally or externally to an enterprise network, thus affecting the integrity of the original content. Reasons for [[T1491-defacement|T1491: Defacement]] include delivering messaging, intimidation, or claiming (possibly false) credit for an intrusion. Disturbing or offensive images may be used as a part of [[T1491-defacement|T1491: Defacement]] in order to cause user discomfort, or to pressure compliance with accompanying messages. 


## Workspace

- [[workspaces/attack/techniques/T1491-defacement-note|Open workspace note]]

![[workspaces/attack/techniques/T1491-defacement-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/8b9606c9_28be_4a38_b146_0e313cc232c1-potential_ransomware_activity_using_legalnotice_message|Potential Ransomware Activity Using LegalNotice Message (high; windows / registry_set)]]

### Atomic Tests

- [[kb/atomic/tests/0eeb68ce_e64c_4420_8d53_ad5bdc6f86d5-windows_display_a_simulated_ransom_note_via_notepad_non_destructive|Windows - Display a simulated ransom note via Notepad (non-destructive) (powershell; windows)]]
- [[kb/atomic/tests/30558d53_9d76_41c4_9267_a7bd5184bed3-replace_desktop_wallpaper|Replace Desktop Wallpaper (powershell; windows)]]
- [[kb/atomic/tests/30905f21_34f3_4504_8b4c_f7a5e314b810-esxi_change_welcome_message_on_direct_console_user_interface_dcui|ESXi - Change Welcome Message on Direct Console User Interface (DCUI) (command_prompt; windows)]]
- [[kb/atomic/tests/ffcbfaab_c9ff_470b_928c_f086b326089b-configure_legalnoticecaption_and_legalnoticetext_registry_keys_to_display_ransom_message|Configure LegalNoticeCaption and LegalNoticeText registry keys to display ransom message (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## D3FEND

- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]

## Subtechniques

### T1491.001: Internal Defacement

^t1491001-internal-defacement

An adversary may deface systems internal to an organization in an attempt to intimidate or mislead users, thus discrediting the integrity of the systems. This may take the form of modifications to internal websites or server login messages, or directly to user systems with the replacement of the desktop wallpaper.(Citation: Novetta Blockbuster)(Citation: Varonis) Disturbing or offensive images may be used as a part of [[T1491-defacement#^t1491001-internal-defacement|T1491.001: Internal Defacement]] in order to cause user discomfort, or to pressure compliance with accompanying messages. Since internally defacing systems exposes an adversary's presence, it often takes place after other intrusion goals have been accomplished.(Citation: Novetta Blockbuster Destructive Malware)

### T1491.002: External Defacement

^t1491002-external-defacement

An adversary may deface systems external to an organization in an attempt to deliver messaging, intimidate, or otherwise mislead an organization or users. [[T1491-defacement#^t1491002-external-defacement|T1491.002: External Defacement]] may ultimately cause users to distrust the systems and to question/discredit the system’s integrity. Externally-facing websites are a common victim of defacement; often targeted by adversary and hacktivist groups in order to push a political message or spread propaganda.(Citation: FireEye Cyber Threats to Media Industries)(Citation: Kevin Mandia Statement to US Senate Committee on Intelligence)(Citation: Anonymous Hackers Deface Russian Govt Site) [[T1491-defacement#^t1491002-external-defacement|T1491.002: External Defacement]] may be used as a catalyst to trigger events, or as a response to actions taken by an organization or government. Similarly, website defacement may also be used as setup, or a precursor, for future attacks such as [[T1189-drive-by_compromise|T1189: Drive-by Compromise]].(Citation: Trend Micro Deep Dive Into Defacement)

## Mitigations

- [[M1053-data_backup|M1053: Data Backup]]

## Platforms

- Windows
- IaaS
- Linux
- macOS
- ESXi

