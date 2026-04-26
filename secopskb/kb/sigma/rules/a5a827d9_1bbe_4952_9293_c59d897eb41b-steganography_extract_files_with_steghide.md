---
sigma_id: "a5a827d9-1bbe-4952-9293-c59d897eb41b"
title: "Steganography Extract Files with Steghide"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_steghide_extract_steganography.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_steghide_extract_steganography.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "a5a827d9-1bbe-4952-9293-c59d897eb41b"
  - "Steganography Extract Files with Steghide"
attack_technique_ids:
  - "T1027.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Steganography Extract Files with Steghide

Detects extraction of files with usage of steghide binary, the adversaries may use this technique to prevent the detection of hidden information.

## Metadata

- Rule ID: a5a827d9-1bbe-4952-9293-c59d897eb41b
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-09-11
- Modified: 2022-10-09
- Source Path: rules/linux/auditd/execve/lnx_auditd_steghide_extract_steganography.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.003]]

## Detection

```yaml
selection:
  type: EXECVE
  a0: steghide
  a1: extract
  a2: -sf
  a3|endswith:
  - .jpg
  - .png
condition: selection
```

## False Positives

- Unknown

## References

- https://vitux.com/how-to-hide-confidential-files-in-images-on-debian-using-steganography/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_steghide_extract_steganography.yml)
