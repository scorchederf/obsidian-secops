---
sigma_id: "e62a9f0c-ca1e-46b2-85d5-a6da77f86d1a"
title: "File Encoded To Base64 Via Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certutil_encode.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_encode.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e62a9f0c-ca1e-46b2-85d5-a6da77f86d1a"
  - "File Encoded To Base64 Via Certutil.EXE"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Encoded To Base64 Via Certutil.EXE

Detects the execution of certutil with the "encode" flag to encode a file to base64. This can be abused by threat actors and attackers for data exfiltration

## Metadata

- Rule ID: e62a9f0c-ca1e-46b2-85d5-a6da77f86d1a
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-02-24
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_certutil_encode.yml

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
  CommandLine|contains|windash: -encode
condition: all of selection_*
```

## False Positives

- As this is a general purpose rule, legitimate usage of the encode functionality will trigger some false positives. Apply additional filters accordingly

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil
- https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/
- https://lolbas-project.github.io/lolbas/Binaries/Certutil/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_encode.yml)
