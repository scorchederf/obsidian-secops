---
sigma_id: "fabb0e80-030c-4e3e-a104-d09676991ac3"
title: "Suspicious File Created in Outlook Temporary Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_outlook_susp_file_creation_in_temp_dir.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_susp_file_creation_in_temp_dir.yml"
build_date: "2026-04-26 17:03:22"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "fabb0e80-030c-4e3e-a104-d09676991ac3"
  - "Suspicious File Created in Outlook Temporary Directory"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious File Created in Outlook Temporary Directory

Detects the creation of files with suspicious file extensions in the temporary directory that Outlook uses when opening attachments.
This can be used to detect spear-phishing campaigns that use suspicious files as attachments, which may contain malicious code.

## Metadata

- Rule ID: fabb0e80-030c-4e3e-a104-d09676991ac3
- Status: experimental
- Level: high
- Author: Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-07-22
- Source Path: rules/windows/file/file_event/file_event_win_office_outlook_susp_file_creation_in_temp_dir.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection_extension:
  TargetFilename|endswith:
  - .cpl
  - .hta
  - .iso
  - .rdp
  - .svg
  - .vba
  - .vbe
  - .vbs
selection_location:
- TargetFilename|contains:
  - \AppData\Local\Packages\Microsoft.Outlook_
  - \AppData\Local\Microsoft\Olk\Attachments\
- TargetFilename|contains|all:
  - \AppData\Local\Microsoft\Windows\
  - \Content.Outlook\
condition: all of selection_*
```

## False Positives

- Opening of headers or footers in email signatures that include SVG images or legitimate SVG attachments

## References

- https://vipre.com/blog/svg-phishing-attacks-the-new-trick-in-the-cybercriminals-playbook/
- https://thecyberexpress.com/rogue-rdp-files-used-in-ukraine-cyberattacks/
- https://www.microsoft.com/en-us/security/blog/2024/10/29/midnight-blizzard-conducts-large-scale-spear-phishing-campaign-using-rdp-files/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_outlook_susp_file_creation_in_temp_dir.yml)
