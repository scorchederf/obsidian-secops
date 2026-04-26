---
sigma_id: "e593cf51-88db-4ee1-b920-37e89012a3c9"
title: "Potentially Suspicious Rundll32 Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e593cf51-88db-4ee1-b920-37e89012a3c9"
  - "Potentially Suspicious Rundll32 Activity"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Rundll32 Activity

Detects suspicious execution of rundll32, with specific calls to some DLLs with known LOLBIN functionalities

## Metadata

- Rule ID: e593cf51-88db-4ee1-b920-37e89012a3c9
- Status: test
- Level: medium
- Author: juju4, Jonhnathan Ribeiro, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-01-16
- Modified: 2023-05-17
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
- CommandLine|contains|all:
  - 'javascript:'
  - .RegisterXLL
- CommandLine|contains|all:
  - url.dll
  - OpenURL
- CommandLine|contains|all:
  - url.dll
  - OpenURLA
- CommandLine|contains|all:
  - url.dll
  - FileProtocolHandler
- CommandLine|contains|all:
  - zipfldr.dll
  - RouteTheCall
- CommandLine|contains|all:
  - shell32.dll
  - Control_RunDLL
- CommandLine|contains|all:
  - shell32.dll
  - ShellExec_RunDLL
- CommandLine|contains|all:
  - mshtml.dll
  - PrintHTML
- CommandLine|contains|all:
  - advpack.dll
  - LaunchINFSection
- CommandLine|contains|all:
  - advpack.dll
  - RegisterOCX
- CommandLine|contains|all:
  - ieadvpack.dll
  - LaunchINFSection
- CommandLine|contains|all:
  - ieadvpack.dll
  - RegisterOCX
- CommandLine|contains|all:
  - ieframe.dll
  - OpenURL
- CommandLine|contains|all:
  - shdocvw.dll
  - OpenURL
- CommandLine|contains|all:
  - syssetup.dll
  - SetupInfObjectInstallAction
- CommandLine|contains|all:
  - setupapi.dll
  - InstallHinfSection
- CommandLine|contains|all:
  - pcwutl.dll
  - LaunchApplication
- CommandLine|contains|all:
  - dfshim.dll
  - ShOpenVerbApplication
- CommandLine|contains|all:
  - dfshim.dll
  - ShOpenVerbShortcut
- CommandLine|contains|all:
  - scrobj.dll
  - GenerateTypeLib
  - http
- CommandLine|contains|all:
  - shimgvw.dll
  - ImageView_Fullscreen
  - http
- CommandLine|contains|all:
  - comsvcs.dll
  - MiniDump
filter_main_screensaver:
  CommandLine|contains: shell32.dll,Control_RunDLL desk.cpl,screensaver,@screensaver
filter_main_parent_cpl:
  ParentImage: C:\Windows\System32\control.exe
  ParentCommandLine|contains: .cpl
  CommandLine|contains|all:
  - Shell32.dll
  - Control_RunDLL
  - .cpl
filter_main_startmenu:
  ParentImage: C:\Windows\System32\control.exe
  CommandLine|startswith: '"C:\Windows\system32\rundll32.exe" Shell32.dll,Control_RunDLL
    "C:\Windows\System32\'
  CommandLine|endswith: .cpl",
condition: selection and not 1 of filter_main_*
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- http://www.hexacorn.com/blog/2017/05/01/running-programs-via-proxy-jumping-on-a-edr-bypass-trampoline/
- https://twitter.com/Hexacorn/status/885258886428725250
- https://gist.github.com/ryhanson/227229866af52e2d963cf941af135a52
- https://twitter.com/nas_bench/status/1433344116071583746
- https://twitter.com/eral4m/status/1479106975967240209
- https://twitter.com/eral4m/status/1479080793003671557

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml)
