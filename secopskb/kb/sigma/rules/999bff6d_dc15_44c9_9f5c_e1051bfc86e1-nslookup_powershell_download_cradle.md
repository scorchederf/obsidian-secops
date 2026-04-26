---
sigma_id: "999bff6d-dc15-44c9-9f5c-e1051bfc86e1"
title: "Nslookup PowerShell Download Cradle"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_abuse_nslookup_with_dns_records.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_abuse_nslookup_with_dns_records.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / ps_classic_start"
aliases:
  - "999bff6d-dc15-44c9-9f5c-e1051bfc86e1"
  - "Nslookup PowerShell Download Cradle"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Nslookup PowerShell Download Cradle

Detects a powershell download cradle using nslookup. This cradle uses nslookup to extract payloads from DNS records.

## Metadata

- Rule ID: 999bff6d-dc15-44c9-9f5c-e1051bfc86e1
- Status: test
- Level: medium
- Author: Sai Prashanth Pulisetti @pulisettis, Aishwarya Singam
- Date: 2022-12-10
- Modified: 2025-02-25
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_abuse_nslookup_with_dns_records.yml

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  Data|contains|all:
  - powershell
  - nslookup
  - '[1]'
  Data|contains:
  - -q=txt http
  - -querytype=txt http
  - -type=txt http
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/Alh4zr3d/status/1566489367232651264

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_abuse_nslookup_with_dns_records.yml)
