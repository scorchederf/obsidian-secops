---
sigma_id: "8d31a8ce-46b5-4dd6-bdc3-680931f1db86"
title: "Bad Opsec Powershell Code Artifacts"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_bad_opsec_artifacts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_bad_opsec_artifacts.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "critical"
logsource: "windows / ps_module"
aliases:
  - "8d31a8ce-46b5-4dd6-bdc3-680931f1db86"
  - "Bad Opsec Powershell Code Artifacts"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bad Opsec Powershell Code Artifacts

focuses on trivial artifacts observed in variants of prevalent offensive ps1 payloads, including
Cobalt Strike Beacon, PoshC2, Powerview, Letmein, Empire, Powersploit, and other attack payloads
that often undergo minimal changes by attackers due to bad opsec.

## Metadata

- Rule ID: 8d31a8ce-46b5-4dd6-bdc3-680931f1db86
- Status: test
- Level: critical
- Author: ok @securonix invrep_de, oscd.community
- Date: 2020-10-09
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_module/posh_pm_bad_opsec_artifacts.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_4103:
  Payload|contains:
  - $DoIt
  - harmj0y
  - mattifestation
  - _RastaMouse
  - tifkin_
  - '0xdeadbeef'
condition: selection_4103
```

## False Positives

- Moderate-to-low; Despite the shorter length/lower entropy for some of these, because of high specificity, fp appears to be fairly limited in many environments.

## References

- https://newtonpaul.com/analysing-fileless-malware-cobalt-strike-beacon/
- https://labs.sentinelone.com/top-tier-russian-organized-cybercrime-group-unveils-fileless-stealthy-powertrick-backdoor-for-high-value-targets/
- https://www.mdeditor.tw/pl/pgRt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_bad_opsec_artifacts.yml)
