---
sigma_id: "fcdf69e5-a3d3-452a-9724-26f2308bf2b1"
title: "Phishing Pattern ISO in Archive"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_archiver_iso_phishing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_archiver_iso_phishing.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fcdf69e5-a3d3-452a-9724-26f2308bf2b1"
  - "Phishing Pattern ISO in Archive"
attack_technique_ids:
  - "T1566"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Phishing Pattern ISO in Archive

Detects cases in which an ISO files is opend within an archiver like 7Zip or Winrar, which is a sign of phishing as threat actors put small ISO files in archives as email attachments to bypass certain filters and protective measures (mark of web)

## Metadata

- Rule ID: fcdf69e5-a3d3-452a-9724-26f2308bf2b1
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-07
- Source Path: rules/windows/process_creation/proc_creation_win_susp_archiver_iso_phishing.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \Winrar.exe
  - \7zFM.exe
  - \peazip.exe
  Image|endswith:
  - \isoburn.exe
  - \PowerISO.exe
  - \ImgBurn.exe
condition: selection
```

## False Positives

- Legitimate cases in which archives contain ISO or IMG files and the user opens the archive and the image via clicking and not extraction

## References

- https://twitter.com/1ZRR4H/status/1534259727059787783
- https://app.any.run/tasks/e1fe6a62-bce8-4323-a49a-63795d9afd5d/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_archiver_iso_phishing.yml)
