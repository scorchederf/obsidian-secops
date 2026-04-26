---
sigma_id: "cea2b7ea-792b-405f-95a1-b903ea06458f"
title: "Suspicious Child Process Of Manage Engine ServiceDesk"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_java_manageengine_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_manageengine_susp_child_process.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cea2b7ea-792b-405f-95a1-b903ea06458f"
  - "Suspicious Child Process Of Manage Engine ServiceDesk"
attack_technique_ids:
  - "T1102"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Child Process Of Manage Engine ServiceDesk

Detects suspicious child processes of the "Manage Engine ServiceDesk Plus" Java web service

## Metadata

- Rule ID: cea2b7ea-792b-405f-95a1-b903ea06458f
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2023-01-18
- Modified: 2023-08-29
- Source Path: rules/windows/process_creation/proc_creation_win_java_manageengine_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1102-web_service|T1102]]

## Detection

```yaml
selection:
  ParentImage|contains|all:
  - \ManageEngine\ServiceDesk\
  - \java.exe
  Image|endswith:
  - \AppVLP.exe
  - \bash.exe
  - \bitsadmin.exe
  - \calc.exe
  - \certutil.exe
  - \cscript.exe
  - \curl.exe
  - \forfiles.exe
  - \mftrace.exe
  - \mshta.exe
  - \net.exe
  - \net1.exe
  - \notepad.exe
  - \powershell.exe
  - \pwsh.exe
  - \query.exe
  - \reg.exe
  - \schtasks.exe
  - \scrcons.exe
  - \sh.exe
  - \systeminfo.exe
  - \whoami.exe
  - \wmic.exe
  - \wscript.exe
filter_main_net:
  Image|endswith:
  - \net.exe
  - \net1.exe
  CommandLine|contains: ' stop'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate sub processes started by Manage Engine ServiceDesk Pro

## References

- https://www.horizon3.ai/manageengine-cve-2022-47966-technical-deep-dive/
- https://github.com/horizon3ai/CVE-2022-47966/blob/3a51c6b72ebbd87392babd955a8fbeaee2090b35/CVE-2022-47966.py
- https://blog.viettelcybersecurity.com/saml-show-stopper/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_manageengine_susp_child_process.yml)
