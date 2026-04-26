---
mitre_id: "T1560"
mitre_name: "Archive Collected Data"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--53ac20cd-aca3-406e-9aa0-9fc7fdc60a5a"
mitre_created: "2020-02-20T20:53:45.725Z"
mitre_modified: "2025-10-24T17:48:48.023Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1560/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0009"
d3fend_ids:
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RF"
  - "D3-RFAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Workspace

- [[workspaces/attack/techniques/T1560-archive_collected_data-note|Open workspace note]]

![[workspaces/attack/techniques/T1560-archive_collected_data-note]]

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]

## Subtechniques

### T1560.001: Archive via Utility

^t1560001-archive-via-utility

Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport.

Adversaries may abuse various utilities to compress or encrypt data before exfiltration. Some third party utilities may be preinstalled, such as `tar` on Linux and macOS or `zip` on Windows systems. 

On Windows, `diantz` or `makecab` may be used to package collected files into a cabinet (.cab) file. `diantz` may also be used to download and compress files from remote locations (i.e. [[T1074-data_staged#^t1074002-remote-data-staging|T1074.002: Remote Data Staging]]).(Citation: diantz.exe_lolbas) `xcopy` on Windows can copy files and directories with a variety of options. Additionally, adversaries may use [[certutil|certutil (S0160)]] to Base64 encode collected data before exfiltration. 

Adversaries may use also third party utilities, such as 7-Zip, WinRAR, and WinZip, to perform similar activities.(Citation: 7zip Homepage)(Citation: WinRAR Homepage)(Citation: WinZip Homepage)

### T1560.002: Archive via Library

^t1560002-archive-via-library

An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party libraries. Many libraries exist that can archive data, including [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]] rarfile (Citation: PyPI RAR), libzip (Citation: libzip), and zlib (Citation: Zlib Github). Most libraries include functionality to encrypt and/or compress data.

Some archival libraries are preinstalled on systems, such as bzip2 on macOS and Linux, and zip on Windows. Note that the libraries are different from the utilities. The libraries can be linked against when compiling, while the utilities require spawning a subshell, or a similar execution mechanism.

### T1560.003: Archive via Custom Method

^t1560003-archive-via-custom-method

An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method. Adversaries may choose to use custom archival methods, such as encryption with XOR or stream ciphers implemented with no external library or utility references. Custom implementations of well-known compression algorithms have also been used.(Citation: ESET Sednit Part 2)

## Mitigations

- [[M1047-audit|M1047: Audit]]

## Tools
- [[bloodhound|BloodHound (S0521)]]
- [[empire|Empire (S0363)]]
- [[shimratreporter|ShimRatReporter (S0445)]]


## Platforms

- Linux
- macOS
- Windows

