---
sigma_id: "cc9cbe82-7bc0-4ef5-bc23-bbfb83947be7"
title: "File Decoded From Base64/Hex Via Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certutil_decode.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_decode.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cc9cbe82-7bc0-4ef5-bc23-bbfb83947be7"
  - "File Decoded From Base64/Hex Via Certutil.EXE"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File Decoded From Base64/Hex Via Certutil.EXE

Detects the execution of certutil with either the "decode" or "decodehex" flags to decode base64 or hex encoded files. This can be abused by attackers to decode an encoded payload before execution

## Metadata

- Rule ID: cc9cbe82-7bc0-4ef5-bc23-bbfb83947be7
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
- Date: 2023-02-15
- Modified: 2025-06-04
- Source Path: rules/windows/process_creation/proc_creation_win_certutil_decode.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection_img:
- Image|endswith: \certutil.exe
- OriginalFileName: CertUtil.exe
selection_cli:
  CommandLine|contains|windash:
  - '-decode '
  - '-decodehex '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil
- https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/
- https://news.sophos.com/en-us/2021/04/13/compromised-exchange-server-hosting-cryptojacker-targeting-other-exchange-servers/
- https://twitter.com/JohnLaTwC/status/835149808817991680
- https://learn.microsoft.com/en-us/archive/blogs/pki/basic-crl-checking-with-certutil
- https://lolbas-project.github.io/lolbas/Binaries/Certutil/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_decode.yml)
