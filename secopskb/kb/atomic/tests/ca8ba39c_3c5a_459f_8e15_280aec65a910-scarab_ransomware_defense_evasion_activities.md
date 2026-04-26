---
atomic_guid: "ca8ba39c-3c5a-459f-8e15-280aec65a910"
title: "Scarab Ransomware Defense Evasion Activities"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "ca8ba39c-3c5a-459f-8e15-280aec65a910"
  - "Scarab Ransomware Defense Evasion Activities"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Scarab Ransomware Defense Evasion Activities

Scarab Ransomware defense evasion activities that can abuse the registry values to modify the settings of the Credential Security Support Provider to overcome potential RDP connection issues.
[Scarab Ransomware Article](https://www.welivesecurity.com/en/eset-research/scarabs-colon-izing-vulnerable-servers/)

## Metadata

- Atomic GUID: ca8ba39c-3c5a-459f-8e15-280aec65a910
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters" /v AllowEncryptionOracle /t REG_DWORD /d 2 /f
```

### Cleanup

```cmd
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters" /v AllowEncryptionOracle /t REG_DWORD /d 0 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
