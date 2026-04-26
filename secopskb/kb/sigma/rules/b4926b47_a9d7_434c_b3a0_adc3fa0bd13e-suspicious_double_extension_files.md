---
sigma_id: "b4926b47-a9d7-434c-b3a0-adc3fa0bd13e"
title: "Suspicious Double Extension Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_double_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_double_extension.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "b4926b47-a9d7-434c-b3a0-adc3fa0bd13e"
  - "Suspicious Double Extension Files"
attack_technique_ids:
  - "T1036.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Double Extension Files

Detects dropped files with double extensions, which is often used by malware as a method to abuse the fact that Windows hide default extensions by default.

## Metadata

- Rule ID: b4926b47-a9d7-434c-b3a0-adc3fa0bd13e
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2022-06-19
- Modified: 2026-03-31
- Source Path: rules/windows/file/file_event/file_event_win_susp_double_extension.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.007]]

## Detection

```yaml
selection_gen:
  TargetFilename|endswith:
  - .exe
  - .iso
  - .rar
  - .svg
  - .zip
  TargetFilename|contains:
  - .doc.
  - .docx.
  - .gif.
  - .jpeg.
  - .jpg.
  - .mp3.
  - .mp4.
  - .pdf.
  - .png.
  - .ppt.
  - .pptx.
  - .rtf.
  - .svg.
  - .txt.
  - .xls.
  - .xlsx.
selection_exe:
  TargetFilename|endswith:
  - .rar.exe
  - .zip.exe
filter_icons_linux:
  TargetFilename|startswith: /usr/share/icons/
condition: 1 of selection_* and not 1 of filter_*
```

## False Positives

- Unlikely

## References

- https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/
- https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations
- https://www.cybereason.com/blog/research/a-bazar-of-tricks-following-team9s-development-cycles
- https://twitter.com/malwrhunterteam/status/1235135745611960321
- https://twitter.com/luc4m/status/1073181154126254080
- https://cloud.google.com/blog/topics/threat-intelligence/cybercriminals-weaponize-fake-ai-websites
- https://vipre.com/blog/svg-phishing-attacks-the-new-trick-in-the-cybercriminals-playbook/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_double_extension.yml)
