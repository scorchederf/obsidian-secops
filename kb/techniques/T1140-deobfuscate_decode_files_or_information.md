---
mitre_id: "T1140"
mitre_name: "Deobfuscate/Decode Files or Information"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3ccef7ae-cb5e-48f6-8302-897105fbf55c"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2025-10-24T17:48:40.925Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1140/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
---

# T1140: Deobfuscate/Decode Files or Information

Adversaries may use [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]] to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present on the system.

One such example is the use of [[certutil|certutil]] to decode a remote access tool portable executable file that has been hidden inside a certificate file.(Citation: Malwarebytes Targeted Attack against Saudi Arabia) Another example is using the Windows `copy /b` or `type` command to reassemble binary fragments into a malicious payload.(Citation: Carbon Black Obfuscation Sept 2016)(Citation: Sentinel One Tainted Love 2023)

Sometimes a user's action may be required to open it for deobfuscation or decryption as part of [[T1204-user_execution|T1204: User Execution]]. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.(Citation: Volexity PowerDuke November 2016)

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Tools

- [[certutil|certutil]]
- [[expand|Expand]]
- [[imminent_monitor|Imminent Monitor]]
- [[ironnetinjector|IronNetInjector]]
- [[pcshare|PcShare]]
- [[brute_ratel_c4|Brute Ratel C4]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

