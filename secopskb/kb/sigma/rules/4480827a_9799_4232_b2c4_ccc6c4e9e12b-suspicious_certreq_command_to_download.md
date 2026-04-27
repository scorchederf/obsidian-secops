---
sigma_id: "4480827a-9799-4232-b2c4-ccc6c4e9e12b"
title: "Suspicious CertReq Command to Download"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certreq_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certreq_download.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4480827a-9799-4232-b2c4-ccc6c4e9e12b"
  - "Suspicious CertReq Command to Download"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious CertReq execution downloading a file.
This behavior is often used by attackers to download additional payloads or configuration files.
Certreq is a built-in Windows utility used to request and retrieve certificates from a certification authority (CA). However, it can be abused by threat actors for malicious purposes.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection_img:
- Image|endswith: \certreq.exe
- OriginalFileName: CertReq.exe
selection_cli_flag_post:
  CommandLine|contains|windash: -Post
selection_cli_flag_config:
  CommandLine|contains|windash: -config
selection_cli_http:
  CommandLine|contains: http
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://lolbas-project.github.io/lolbas/Binaries/Certreq/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certreq_download.yml)
