---
sigma_id: "3215aa19-f060-4332-86d5-5602511f3ca8"
title: "Suspicious LNK Double Extension File Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_lnk_double_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_lnk_double_extension.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "3215aa19-f060-4332-86d5-5602511f3ca8"
  - "Suspicious LNK Double Extension File Created"
attack_technique_ids:
  - "T1036.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious LNK Double Extension File Created

Detects the creation of files with an "LNK" as a second extension. This is sometimes used by malware as a method to abuse the fact that Windows hides the "LNK" extension by default.

## Metadata

- Rule ID: 3215aa19-f060-4332-86d5-5602511f3ca8
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2022-11-07
- Modified: 2023-10-18
- Source Path: rules/windows/file/file_event/file_event_win_susp_lnk_double_extension.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.007]]

## Detection

```yaml
selection:
  TargetFilename|endswith: .lnk
  TargetFilename|contains:
  - .doc.
  - .docx.
  - .jpg.
  - .pdf.
  - .ppt.
  - .pptx.
  - .xls.
  - .xlsx.
filter_main_recent:
  TargetFilename|contains: \AppData\Roaming\Microsoft\Windows\Recent\
filter_optional_office_recent:
  Image|endswith:
  - \excel.exe
  - \powerpnt.exe
  - \winword.exe
  TargetFilename|contains: \AppData\Roaming\Microsoft\Office\Recent\
filter_optional_office_excel:
  Image|endswith: \excel.exe
  TargetFilename|contains: \AppData\Roaming\Microsoft\Excel
filter_optional_office_powerpoint:
  Image|endswith: \powerpnt.exe
  TargetFilename|contains: \AppData\Roaming\Microsoft\PowerPoint
filter_optional_office_word:
  Image|endswith: \winword.exe
  TargetFilename|contains: \AppData\Roaming\Microsoft\Word
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Some tuning is required for other general purpose directories of third party apps

## References

- https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/
- https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations
- https://www.cybereason.com/blog/research/a-bazar-of-tricks-following-team9s-development-cycles
- https://twitter.com/malwrhunterteam/status/1235135745611960321
- https://twitter.com/luc4m/status/1073181154126254080

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_lnk_double_extension.yml)
