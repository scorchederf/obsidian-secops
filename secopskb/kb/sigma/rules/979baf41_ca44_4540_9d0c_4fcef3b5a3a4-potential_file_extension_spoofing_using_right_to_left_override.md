---
sigma_id: "979baf41-ca44-4540-9d0c-4fcef3b5a3a4"
title: "Potential File Extension Spoofing Using Right-to-Left Override"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_right_to_left_override_extension_spoofing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_right_to_left_override_extension_spoofing.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "979baf41-ca44-4540-9d0c-4fcef3b5a3a4"
  - "Potential File Extension Spoofing Using Right-to-Left Override"
attack_technique_ids:
  - "T1036.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential File Extension Spoofing Using Right-to-Left Override

Detects suspicious filenames that contain a right-to-left override character and a potentially spoofed file extensions.

## Metadata

- Rule ID: 979baf41-ca44-4540-9d0c-4fcef3b5a3a4
- Status: test
- Level: high
- Author: Jonathan Peters (Nextron Systems), Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2024-11-17
- Modified: 2026-03-20
- Source Path: rules/windows/file/file_event/file_event_win_susp_right_to_left_override_extension_spoofing.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.002]]

## Detection

```yaml
selection_rtlo_unicode:
  TargetFilename|contains:
  - \u202e
  - '[U+202E]'
  - ‮
selection_extensions:
  TargetFilename|contains:
  - 3pm.
  - 4pm.
  - cod.
  - fdp.
  - ftr.
  - gepj.
  - gnp.
  - gpj.
  - ism.
  - lmth.
  - nls.
  - piz.
  - slx.
  - tdo.
  - vsc.
  - vwm.
  - xcod.
  - xslx.
  - xtpp.
condition: all of selection_*
```

## False Positives

- Filenames that contains scriptures such as arabic or hebrew might make use of this character

## References

- https://redcanary.com/blog/right-to-left-override/
- https://www.malwarebytes.com/blog/news/2014/01/the-rtlo-method
- https://tria.ge/241015-l98snsyeje/behavioral2
- https://www.unicode.org/versions/Unicode5.2.0/ch02.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_right_to_left_override_extension_spoofing.yml)
