---
atomic_guid: "17e7637a-ddaf-4a82-8622-377e20de8fdb"
title: "Create ADS command prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.004"
attack_technique_name: "Hide Artifacts: NTFS File Attributes"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "17e7637a-ddaf-4a82-8622-377e20de8fdb"
  - "Create ADS command prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Create an Alternate Data Stream with the command prompt. Write access is required. Upon execution, run "dir /a-d /s /r | find ":$DATA"" in the %temp%
folder to view that the alternate data stream exists. To view the data in the alternate data stream, run "notepad T1564.004_has_ads.txt:adstest.txt"

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

## Input Arguments

### ads_filename

- description: Name of ADS.
- type: string
- default: adstest.txt

### file_name

- description: File name of file to create ADS on.
- type: string
- default: %temp%\T1564.004_has_ads_cmd.txt

## Executor

- name: command_prompt

### Command

```cmd
echo cmd /c echo "Shell code execution."> #{file_name}:#{ads_filename}
for /f "usebackq delims=?" %i in (#{file_name}:#{ads_filename}) do %i
```

### Cleanup

```cmd
del #{file_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.004/T1564.004.yaml)
