---
mitre_id: "T1080"
mitre_name: "Taint Shared Content"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--246fd3c7-f5e3-466d-8787-4c13d9e3b61c"
mitre_created: "2017-05-31T21:31:01.759Z"
mitre_modified: "2025-10-24T17:48:32.156Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1080/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "SaaS"
  - "Linux"
  - "macOS"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0008"
d3fend_ids:
  - "D3-DNR"
  - "D3-NRAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---


Adversaries may deliver payloads to remote systems by adding content to shared storage locations, such as network drives or internal code repositories. Content stored on network drives or in other shared locations may be tainted by adding malicious programs, scripts, or exploit code to otherwise valid files. Once a user opens the shared tainted content, the malicious portion can be executed to run the adversary's code on a remote system. Adversaries may use tainted shared content to move laterally.

A directory share pivot is a variation on this technique that uses several other techniques to propagate malware when users access a shared network directory. It uses [[T1547-boot_or_logon_autostart_execution#^t1547009-shortcut-modification|T1547.009: Shortcut Modification]] of directory .LNK files that use [[T1036-masquerading|T1036: Masquerading]] to look like the real directories, which are hidden through [[T1564-hide_artifacts#^t1564001-hidden-files-and-directories|T1564.001: Hidden Files and Directories]]. The malicious .LNK-based directories have an embedded command that executes the hidden malware file in the directory and then opens the real intended directory so that the user's expected action still occurs. When used with frequently used network directories, the technique may result in frequent reinfections and broad access to systems and potentially to new and higher privileged accounts. (Citation: Retwin Directory Share Pivot)

Adversaries may also compromise shared network directories through binary infections by appending or prepending its code to the healthy binary on the shared network directory. The malware may modify the original entry point (OEP) of the healthy binary to ensure that it is executed before the legitimate code. The infection could continue to spread via the newly infected file when it is executed by a remote system. These infections may target both binary and non-binary formats that end with extensions including, but not limited to, .EXE, .DLL, .SCR, .BAT, and/or .VBS.

## Workspace

- [[notes/attack/techniques/T1080-taint_shared_content-note|Open workspace note]]

![[notes/attack/techniques/T1080-taint_shared_content-note]]

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

## D3FEND

- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]

## Mitigations

- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1049-antivirus_antimalware|M1049: Antivirus/Antimalware]]
- [[M1050-exploit_protection|M1050: Exploit Protection]]

## Platforms

- Windows
- SaaS
- Linux
- macOS
- Office Suite

