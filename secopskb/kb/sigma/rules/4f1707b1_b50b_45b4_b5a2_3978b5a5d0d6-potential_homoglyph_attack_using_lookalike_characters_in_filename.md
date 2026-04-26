---
sigma_id: "4f1707b1-b50b-45b4-b5a2-3978b5a5d0d6"
title: "Potential Homoglyph Attack Using Lookalike Characters in Filename"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_homoglyph_filename.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_homoglyph_filename.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "4f1707b1-b50b-45b4-b5a2-3978b5a5d0d6"
  - "Potential Homoglyph Attack Using Lookalike Characters in Filename"
attack_technique_ids:
  - "T1036"
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Homoglyph Attack Using Lookalike Characters in Filename

Detects the presence of unicode characters which are homoglyphs, or identical in appearance, to ASCII letter characters.
This is used as an obfuscation and masquerading techniques. Only "perfect" homoglyphs are included; these are characters that
are indistinguishable from ASCII characters and thus may make excellent candidates for homoglyph attack characters.

## Metadata

- Rule ID: 4f1707b1-b50b-45b4-b5a2-3978b5a5d0d6
- Status: test
- Level: medium
- Author: Micah Babinski, @micahbabinski
- Date: 2023-05-08
- Source Path: rules/windows/file/file_event/file_event_win_susp_homoglyph_filename.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection_upper:
  TargetFilename|contains:
  - А
  - В
  - Е
  - К
  - М
  - Н
  - О
  - Р
  - С
  - Т
  - Х
  - Ѕ
  - І
  - Ј
  - Ү
  - Ӏ
  - Ԍ
  - Ԛ
  - Ԝ
  - Α
  - Β
  - Ε
  - Ζ
  - Η
  - Ι
  - Κ
  - Μ
  - Ν
  - Ο
  - Ρ
  - Τ
  - Υ
  - Χ
selection_lower:
  TargetFilename|contains:
  - а
  - е
  - о
  - р
  - с
  - х
  - ѕ
  - і
  - ӏ
  - ј
  - һ
  - ԁ
  - ԛ
  - ԝ
  - ο
condition: 1 of selection_*
```

## False Positives

- File names with legitimate Cyrillic text. Will likely require tuning (or not be usable) in countries where these alphabets are in use.

## References

- https://redcanary.com/threat-detection-report/threats/socgholish/#threat-socgholish
- http://www.irongeek.com/homoglyph-attack-generator.php

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_homoglyph_filename.yml)
