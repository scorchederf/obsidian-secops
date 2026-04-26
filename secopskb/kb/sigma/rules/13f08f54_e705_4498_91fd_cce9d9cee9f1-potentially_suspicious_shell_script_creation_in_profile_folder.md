---
sigma_id: "13f08f54-e705-4498-91fd-cce9d9cee9f1"
title: "Potentially Suspicious Shell Script Creation in Profile Folder"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_susp_shell_script_under_profile_directory.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_susp_shell_script_under_profile_directory.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "linux / file_event"
aliases:
  - "13f08f54-e705-4498-91fd-cce9d9cee9f1"
  - "Potentially Suspicious Shell Script Creation in Profile Folder"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Shell Script Creation in Profile Folder

Detects the creation of shell scripts under the "profile.d" path.

## Metadata

- Rule ID: 13f08f54-e705-4498-91fd-cce9d9cee9f1
- Status: test
- Level: low
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Source Path: rules/linux/file_event/file_event_lnx_susp_shell_script_under_profile_directory.yml

## Logsource

- category: file_event
- product: linux

## Detection

```yaml
selection:
  TargetFilename|contains: /etc/profile.d/
  TargetFilename|endswith:
  - .csh
  - .sh
condition: selection
```

## False Positives

- Legitimate shell scripts in the "profile.d" directory could be common in your environment. Apply additional filter accordingly via "image", by adding specific filenames you "trust" or by correlating it with other events.
- Regular file creation during system update or software installation by the package manager

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_susp_shell_script_under_profile_directory.yml)
