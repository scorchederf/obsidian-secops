---
sigma_id: "e0b06658-7d1d-4cd3-bf15-03467507ff7c"
title: "Suspicious DotNET CLR Usage Log Artifact"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_net_cli_artefact.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "e0b06658-7d1d-4cd3-bf15-03467507ff7c"
  - "Suspicious DotNET CLR Usage Log Artifact"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious DotNET CLR Usage Log Artifact

Detects the creation of Usage Log files by the CLR (clr.dll). These files are named after the executing process once the assembly is finished executing for the first time in the (user) session context.

## Metadata

- Rule ID: e0b06658-7d1d-4cd3-bf15-03467507ff7c
- Status: test
- Level: high
- Author: frack113, omkar72, oscd.community, Wojciech Lesicki
- Date: 2022-11-18
- Modified: 2023-02-23
- Source Path: rules/windows/file/file_event/file_event_win_net_cli_artefact.yml

## Logsource

- category: file_event
- definition: Requirements: UsageLogs folder must be monitored by the sysmon configuration
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \UsageLogs\cmstp.exe.log
  - \UsageLogs\cscript.exe.log
  - \UsageLogs\mshta.exe.log
  - \UsageLogs\msxsl.exe.log
  - \UsageLogs\regsvr32.exe.log
  - \UsageLogs\rundll32.exe.log
  - \UsageLogs\svchost.exe.log
  - \UsageLogs\wscript.exe.log
  - \UsageLogs\wmic.exe.log
filter_main_rundll32:
  ParentImage|endswith: \MsiExec.exe
  ParentCommandLine|contains: ' -Embedding'
  Image|endswith: \rundll32.exe
  CommandLine|contains|all:
  - Temp
  - zzzzInvokeManagedCustomActionOutOfProc
condition: selection and not 1 of filter_main_*
```

## False Positives

- Rundll32.exe with zzzzInvokeManagedCustomActionOutOfProc in command line and msiexec.exe as parent process - https://twitter.com/SBousseaden/status/1388064061087260675

## References

- https://bohops.com/2021/03/16/investigating-net-clr-usage-log-tampering-techniques-for-edr-evasion/
- https://github.com/olafhartong/sysmon-modular/blob/fa1ae53132403d262be2bbd7f17ceea7e15e8c78/11_file_create/include_dotnet.xml
- https://web.archive.org/web/20221026202428/https://gist.github.com/code-scrap/d7f152ffcdb3e0b02f7f394f5187f008
- https://web.archive.org/web/20230329154538/https://blog.menasec.net/2019/07/interesting-difr-traces-of-net-clr.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml)
