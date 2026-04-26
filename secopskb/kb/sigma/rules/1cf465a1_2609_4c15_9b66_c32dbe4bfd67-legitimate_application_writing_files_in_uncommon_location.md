---
sigma_id: "1cf465a1-2609-4c15-9b66-c32dbe4bfd67"
title: "Legitimate Application Writing Files In Uncommon Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_in_uncommon_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_in_uncommon_location.yml"
build_date: "2026-04-26 17:03:19"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "1cf465a1-2609-4c15-9b66-c32dbe4bfd67"
  - "Legitimate Application Writing Files In Uncommon Location"
attack_technique_ids:
  - "T1218"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Legitimate Application Writing Files In Uncommon Location

Detects legitimate applications writing any type of file to uncommon or suspicious locations that are not typical for application data storage or execution.
Adversaries may leverage legitimate applications (Living off the Land Binaries - LOLBins) to drop or download malicious files to uncommon locations on the system to evade detection by security solutions.

## Metadata

- Rule ID: 1cf465a1-2609-4c15-9b66-c32dbe4bfd67
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-12-10
- Source Path: rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_in_uncommon_location.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - \eqnedt32.exe
  - \wordpad.exe
  - \wordview.exe
  - \cmdl32.exe
  - \certutil.exe
  - \certoc.exe
  - \CertReq.exe
  - \bitsadmin.exe
  - \Desktopimgdownldr.exe
  - \esentutl.exe
  - \expand.exe
  - \extrac32.exe
  - \replace.exe
  - \mshta.exe
  - \ftp.exe
  - \Ldifde.exe
  - \RdrCEF.exe
  - \hh.exe
  - \finger.exe
  - \findstr.exe
selection_locations:
  TargetFilename|contains:
  - :\Perflogs
  - :\ProgramData\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\
  - \$Recycle.Bin\
  - \AppData\Local\
  - \AppData\Roaming\
  - \Contacts\
  - \Desktop\
  - \Favorites\
  - \Favourites\
  - \inetpub\wwwroot\
  - \Music\
  - \Pictures\
  - \Start Menu\Programs\Startup\
  - \Users\Default\
  - \Videos\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/#/download

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_in_uncommon_location.yml)
