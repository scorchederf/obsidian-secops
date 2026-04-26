---
sigma_id: "edd595d7-7895-4fa7-acb3-85a18a8772ca"
title: "Steganography Unzip Hidden Information From Picture File"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_unzip_hidden_zip_files_steganography.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_unzip_hidden_zip_files_steganography.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "edd595d7-7895-4fa7-acb3-85a18a8772ca"
  - "Steganography Unzip Hidden Information From Picture File"
attack_technique_ids:
  - "T1027.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Steganography Unzip Hidden Information From Picture File

Detects extracting of zip file from image file

## Metadata

- Rule ID: edd595d7-7895-4fa7-acb3-85a18a8772ca
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-09-09
- Modified: 2022-10-09
- Source Path: rules/linux/auditd/execve/lnx_auditd_unzip_hidden_zip_files_steganography.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.003]]

## Detection

```yaml
commands:
  type: EXECVE
  a0: unzip
a1:
  a1|endswith:
  - .jpg
  - .png
condition: commands and a1
```

## False Positives

- Unknown

## References

- https://zerotoroot.me/steganography-hiding-a-zip-in-a-jpeg-file/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_unzip_hidden_zip_files_steganography.yml)
