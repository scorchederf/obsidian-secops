---
sigma_id: "03f4ca17-de95-428d-a75a-4ee78b047256"
title: "HackTool - Impacket File Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_impacket_file_indicators.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_impacket_file_indicators.yml"
build_date: "2026-04-27 19:13:51"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "03f4ca17-de95-428d-a75a-4ee78b047256"
  - "HackTool - Impacket File Indicators"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects file creation events with filename patterns used by Impacket.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection_names_re:
  TargetFilename|re: \\sessionresume_[a-zA-Z]{8}$
condition: selection_names_re
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2025/05/19/another-confluence-bites-the-dust-falling-to-elpaco-team-ransomware/
- https://github.com/fortra/impacket

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_impacket_file_indicators.yml)
