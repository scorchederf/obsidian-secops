---
sigma_id: "d59d7842-9a21-4bc6-ba98-64bfe0091355"
title: "Powershell DNSExfiltration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_dnsexfiltration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_dnsexfiltration.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "d59d7842-9a21-4bc6-ba98-64bfe0091355"
  - "Powershell DNSExfiltration"
attack_technique_ids:
  - "T1048"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Powershell DNSExfiltration

DNSExfiltrator allows for transferring (exfiltrate) a file over a DNS request covert channel

## Metadata

- Rule ID: d59d7842-9a21-4bc6-ba98-64bfe0091355
- Status: test
- Level: high
- Author: frack113
- Date: 2022-01-07
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_dnsexfiltration.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detection

```yaml
selection_cmdlet:
- ScriptBlockText|contains: Invoke-DNSExfiltrator
- ScriptBlockText|contains|all:
  - ' -i '
  - ' -d '
  - ' -p '
  - ' -doh '
  - ' -t '
condition: selection_cmdlet
```

## False Positives

- Legitimate script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1048/T1048.md#atomic-test-3---dnsexfiltration-doh
- https://github.com/Arno0x/DNSExfiltrator

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_dnsexfiltration.yml)
