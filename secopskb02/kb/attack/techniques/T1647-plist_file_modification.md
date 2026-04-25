---
mitre_id: "T1647"
mitre_name: "Plist File Modification"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7d20fff9-8751-404e-badd-ccd71bda0236"
mitre_created: "2022-04-09T15:06:32.458Z"
mitre_modified: "2025-10-24T17:49:00.573Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1647/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "macOS"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially evading and bypassing system defenses. macOS applications use plist files, such as the `info.plist` file, to store properties and configuration settings that inform the operating system how to handle the application at runtime. Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files can be saved in text or binary format.(Citation: fileinfo plist file description) 

Adversaries can modify key-value pairs in plist files to influence system behaviors, such as hiding the execution of an application (i.e. [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]) or running additional commands for persistence (ex: [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]/[[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]] or [[T1547-boot_or_logon_autostart_execution#^t1547007-re-opened-applications|T1547.007: Re-opened Applications]]).

For example, adversaries can add a malicious application path to the `~/Library/Preferences/com.apple.dock.plist` file, which controls apps that appear in the Dock. Adversaries can also modify the `LSUIElement` key in an application’s `info.plist` file  to run the app in the background. Adversaries can also insert key-value pairs to insert environment variables, such as `LSEnvironment`, to enable persistence via [[T1574-hijack_execution_flow#^t1574006-dynamic-linker-hijacking|T1574.006: Dynamic Linker Hijacking]].(Citation: wardle chp2 persistence)(Citation: eset_osx_flashback)

## Workspace

- [[workspaces/attack/techniques/T1647-plist_file_modification-note|Open workspace note]]

![[workspaces/attack/techniques/T1647-plist_file_modification-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Mitigations

- [[M1013-application_developer_guidance|M1013: Application Developer Guidance]]

## Platforms

- macOS

