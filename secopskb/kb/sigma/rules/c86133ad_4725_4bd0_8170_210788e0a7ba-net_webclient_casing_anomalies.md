---
sigma_id: "c86133ad-4725-4bd0-8170-210788e0a7ba"
title: "Net WebClient Casing Anomalies"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_webclient_casing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_webclient_casing.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c86133ad-4725-4bd0-8170-210788e0a7ba"
  - "Net WebClient Casing Anomalies"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Net WebClient Casing Anomalies

Detects PowerShell command line contents that include a suspicious abnormal casing in the Net.Webclient (e.g. nEt.WEbCliEnT) string as used in obfuscation techniques

## Metadata

- Rule ID: c86133ad-4725-4bd0-8170-210788e0a7ba
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-05-24
- Modified: 2023-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_webclient_casing.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_encoded:
  CommandLine|contains:
  - TgBlAFQALgB3AEUAQg
  - 4AZQBUAC4AdwBFAEIA
  - OAGUAVAAuAHcARQBCA
  - bgBFAHQALgB3AGUAYg
  - 4ARQB0AC4AdwBlAGIA
  - uAEUAdAAuAHcAZQBiA
  - TgBFAHQALgB3AGUAYg
  - OAEUAdAAuAHcAZQBiA
  - bgBlAFQALgB3AGUAYg
  - 4AZQBUAC4AdwBlAGIA
  - uAGUAVAAuAHcAZQBiA
  - TgBlAFQALgB3AGUAYg
  - OAGUAVAAuAHcAZQBiA
  - bgBFAFQALgB3AGUAYg
  - 4ARQBUAC4AdwBlAGIA
  - uAEUAVAAuAHcAZQBiA
  - bgBlAHQALgBXAGUAYg
  - 4AZQB0AC4AVwBlAGIA
  - uAGUAdAAuAFcAZQBiA
  - bgBFAHQALgBXAGUAYg
  - 4ARQB0AC4AVwBlAGIA
  - uAEUAdAAuAFcAZQBiA
  - TgBFAHQALgBXAGUAYg
  - OAEUAdAAuAFcAZQBiA
  - bgBlAFQALgBXAGUAYg
  - 4AZQBUAC4AVwBlAGIA
  - uAGUAVAAuAFcAZQBiA
  - TgBlAFQALgBXAGUAYg
  - OAGUAVAAuAFcAZQBiA
  - bgBFAFQALgBXAGUAYg
  - 4ARQBUAC4AVwBlAGIA
  - uAEUAVAAuAFcAZQBiA
  - bgBlAHQALgB3AEUAYg
  - 4AZQB0AC4AdwBFAGIA
  - uAGUAdAAuAHcARQBiA
  - TgBlAHQALgB3AEUAYg
  - OAGUAdAAuAHcARQBiA
  - bgBFAHQALgB3AEUAYg
  - 4ARQB0AC4AdwBFAGIA
  - uAEUAdAAuAHcARQBiA
  - TgBFAHQALgB3AEUAYg
  - OAEUAdAAuAHcARQBiA
  - bgBlAFQALgB3AEUAYg
  - 4AZQBUAC4AdwBFAGIA
  - uAGUAVAAuAHcARQBiA
  - TgBlAFQALgB3AEUAYg
  - OAGUAVAAuAHcARQBiA
  - bgBFAFQALgB3AEUAYg
  - 4ARQBUAC4AdwBFAGIA
  - uAEUAVAAuAHcARQBiA
  - TgBFAFQALgB3AEUAYg
  - OAEUAVAAuAHcARQBiA
  - bgBlAHQALgBXAEUAYg
  - 4AZQB0AC4AVwBFAGIA
  - uAGUAdAAuAFcARQBiA
  - TgBlAHQALgBXAEUAYg
  - OAGUAdAAuAFcARQBiA
  - bgBFAHQALgBXAEUAYg
  - 4ARQB0AC4AVwBFAGIA
  - uAEUAdAAuAFcARQBiA
  - TgBFAHQALgBXAEUAYg
  - OAEUAdAAuAFcARQBiA
  - bgBlAFQALgBXAEUAYg
  - 4AZQBUAC4AVwBFAGIA
  - uAGUAVAAuAFcARQBiA
  - TgBlAFQALgBXAEUAYg
  - OAGUAVAAuAFcARQBiA
  - bgBFAFQALgBXAEUAYg
  - 4ARQBUAC4AVwBFAGIA
  - uAEUAVAAuAFcARQBiA
  - TgBFAFQALgBXAEUAYg
  - OAEUAVAAuAFcARQBiA
  - bgBlAHQALgB3AGUAQg
  - 4AZQB0AC4AdwBlAEIA
  - uAGUAdAAuAHcAZQBCA
  - TgBlAHQALgB3AGUAQg
  - OAGUAdAAuAHcAZQBCA
  - bgBFAHQALgB3AGUAQg
  - 4ARQB0AC4AdwBlAEIA
  - uAEUAdAAuAHcAZQBCA
  - TgBFAHQALgB3AGUAQg
  - OAEUAdAAuAHcAZQBCA
  - bgBlAFQALgB3AGUAQg
  - 4AZQBUAC4AdwBlAEIA
  - uAGUAVAAuAHcAZQBCA
  - TgBlAFQALgB3AGUAQg
  - OAGUAVAAuAHcAZQBCA
  - bgBFAFQALgB3AGUAQg
  - 4ARQBUAC4AdwBlAEIA
  - uAEUAVAAuAHcAZQBCA
  - TgBFAFQALgB3AGUAQg
  - OAEUAVAAuAHcAZQBCA
  - bgBlAHQALgBXAGUAQg
  - 4AZQB0AC4AVwBlAEIA
  - uAGUAdAAuAFcAZQBCA
  - TgBlAHQALgBXAGUAQg
  - OAGUAdAAuAFcAZQBCA
  - bgBFAHQALgBXAGUAQg
  - 4ARQB0AC4AVwBlAEIA
  - uAEUAdAAuAFcAZQBCA
  - TgBFAHQALgBXAGUAQg
  - OAEUAdAAuAFcAZQBCA
  - bgBlAFQALgBXAGUAQg
  - 4AZQBUAC4AVwBlAEIA
  - uAGUAVAAuAFcAZQBCA
  - TgBlAFQALgBXAGUAQg
  - OAGUAVAAuAFcAZQBCA
  - bgBFAFQALgBXAGUAQg
  - 4ARQBUAC4AVwBlAEIA
  - uAEUAVAAuAFcAZQBCA
  - TgBFAFQALgBXAGUAQg
  - OAEUAVAAuAFcAZQBCA
  - bgBlAHQALgB3AEUAQg
  - 4AZQB0AC4AdwBFAEIA
  - uAGUAdAAuAHcARQBCA
  - TgBlAHQALgB3AEUAQg
  - OAGUAdAAuAHcARQBCA
  - bgBFAHQALgB3AEUAQg
  - 4ARQB0AC4AdwBFAEIA
  - uAEUAdAAuAHcARQBCA
  - TgBFAHQALgB3AEUAQg
  - OAEUAdAAuAHcARQBCA
  - bgBlAFQALgB3AEUAQg
  - uAGUAVAAuAHcARQBCA
  - bgBFAFQALgB3AEUAQg
  - 4ARQBUAC4AdwBFAEIA
  - uAEUAVAAuAHcARQBCA
  - TgBFAFQALgB3AEUAQg
  - OAEUAVAAuAHcARQBCA
  - TgBlAHQALgBXAEUAQg
  - 4AZQB0AC4AVwBFAEIA
  - OAGUAdAAuAFcARQBCA
  - bgBFAHQALgBXAEUAQg
  - 4ARQB0AC4AVwBFAEIA
  - uAEUAdAAuAFcARQBCA
  - TgBFAHQALgBXAEUAQg
  - OAEUAdAAuAFcARQBCA
  - bgBlAFQALgBXAEUAQg
  - 4AZQBUAC4AVwBFAEIA
  - uAGUAVAAuAFcARQBCA
  - TgBlAFQALgBXAEUAQg
  - OAGUAVAAuAFcARQBCA
  - bgBFAFQALgBXAEUAQg
  - 4ARQBUAC4AVwBFAEIA
  - uAEUAVAAuAFcARQBCA
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://app.any.run/tasks/b9040c63-c140-479b-ad59-f1bb56ce7a97/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_webclient_casing.yml)
