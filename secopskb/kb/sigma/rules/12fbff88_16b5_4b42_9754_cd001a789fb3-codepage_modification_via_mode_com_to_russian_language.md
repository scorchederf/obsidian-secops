---
sigma_id: "12fbff88-16b5-4b42-9754-cd001a789fb3"
title: "CodePage Modification Via MODE.COM To Russian Language"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mode_codepage_russian.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mode_codepage_russian.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "12fbff88-16b5-4b42-9754-cd001a789fb3"
  - "CodePage Modification Via MODE.COM To Russian Language"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CodePage Modification Via MODE.COM To Russian Language

Detects a CodePage modification using the "mode.com" utility to Russian language.
This behavior has been used by threat actors behind Dharma ransomware.

## Metadata

- Rule ID: 12fbff88-16b5-4b42-9754-cd001a789fb3
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2024-01-17
- Source Path: rules/windows/process_creation/proc_creation_win_mode_codepage_russian.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_img:
- Image|endswith: \mode.com
- OriginalFileName: MODE.COM
selection_cli:
  CommandLine|contains|all:
  - ' con '
  - ' cp '
  - ' select='
  CommandLine|endswith:
  - =1251
  - =866
condition: all of selection_*
```

## False Positives

- Russian speaking people changing the CodePage

## References

- https://learn.microsoft.com/en-us/windows/win32/intl/code-page-identifiers
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mode
- https://strontic.github.io/xcyclopedia/library/mode.com-59D1ED51ACB8C3D50F1306FD75F20E99.html
- https://www.virustotal.com/gui/file/5e75ef02517afd6e8ba6462b19217dc4a5a574abb33d10eb0f2bab49d8d48c22/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mode_codepage_russian.yml)
