---
atomic_guid: "114ccff9-ae6d-4547-9ead-4cd69f687306"
title: "Download Macro-Enabled Phishing Attachment"
framework: "atomic"
generated: "true"
attack_technique_id: "T1566.001"
attack_technique_name: "Phishing: Spearphishing Attachment"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1566.001/T1566.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "114ccff9-ae6d-4547-9ead-4cd69f687306"
  - "Download Macro-Enabled Phishing Attachment"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Download Macro-Enabled Phishing Attachment

This atomic test downloads a macro enabled document from the Atomic Red Team GitHub repository, simulating an end user clicking a phishing link to download the file.
The file "PhishingAttachment.xlsm" is downloaded to the %temp% directory.

## Metadata

- Atomic GUID: 114ccff9-ae6d-4547-9ead-4cd69f687306
- Technique: T1566.001: Phishing: Spearphishing Attachment
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1566.001/T1566.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Executor

- name: powershell

### Command

```powershell
$url = 'https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1566.001/bin/PhishingAttachment.xlsm'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri $url -OutFile $env:TEMP\PhishingAttachment.xlsm
```

### Cleanup

```powershell
Remove-Item $env:TEMP\PhishingAttachment.xlsm -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1566.001/T1566.001.yaml)
