---
sigma_id: "023394c4-29d5-46ab-92b8-6a534c6f447b"
title: "Suspicious HWP Sub Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hwp_exploits.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hwp_exploits.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "023394c4-29d5-46ab-92b8-6a534c6f447b"
  - "Suspicious HWP Sub Processes"
attack_technique_ids:
  - "T1566.001"
  - "T1203"
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious HWP Sub Processes

Detects suspicious Hangul Word Processor (Hanword) sub processes that could indicate an exploitation

## Metadata

- Rule ID: 023394c4-29d5-46ab-92b8-6a534c6f447b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-10-24
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_hwp_exploits.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection:
  ParentImage|endswith: \Hwp.exe
  Image|endswith: \gbb.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.securitynewspaper.com/2016/11/23/technical-teardown-exploit-malware-hwp-files/
- https://www.hybrid-analysis.com/search?query=context:74940dcc5b38f9f9b1a0fea760d344735d7d91b610e6d5bd34533dd0153402c5&from_sample=5db135000388385a7644131f&block_redirect=1
- https://twitter.com/cyberwar_15/status/1187287262054076416
- https://blog.alyac.co.kr/1901
- https://en.wikipedia.org/wiki/Hangul_(word_processor)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hwp_exploits.yml)
