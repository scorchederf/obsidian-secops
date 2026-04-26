---
sigma_id: "a7c3d773-caef-227e-a7e7-c2f13c622329"
title: "Bad Opsec Defaults Sacrificial Processes With Improper Arguments"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_bad_opsec_sacrificial_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_bad_opsec_sacrificial_processes.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a7c3d773-caef-227e-a7e7-c2f13c622329"
  - "Bad Opsec Defaults Sacrificial Processes With Improper Arguments"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bad Opsec Defaults Sacrificial Processes With Improper Arguments

Detects attackers using tooling with bad opsec defaults.
E.g. spawning a sacrificial process to inject a capability into the process without taking into account how the process is normally run.
One trivial example of this is using rundll32.exe without arguments as a sacrificial process (default in CS, now highlighted by c2lint), running WerFault without arguments (Kraken - credit am0nsec), and other examples.

## Metadata

- Rule ID: a7c3d773-caef-227e-a7e7-c2f13c622329
- Status: test
- Level: high
- Author: Oleg Kolesnikov @securonix invrep_de, oscd.community, Florian Roth (Nextron Systems), Christian Burkard (Nextron Systems)
- Date: 2020-10-23
- Modified: 2024-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_susp_bad_opsec_sacrificial_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_werfault:
  Image|endswith: \WerFault.exe
  CommandLine|endswith: WerFault.exe
selection_rundll32:
  Image|endswith: \rundll32.exe
  CommandLine|endswith: rundll32.exe
selection_regsvcs:
  Image|endswith: \regsvcs.exe
  CommandLine|endswith: regsvcs.exe
selection_regasm:
  Image|endswith: \regasm.exe
  CommandLine|endswith: regasm.exe
selection_regsvr32:
  Image|endswith: \regsvr32.exe
  CommandLine|endswith: regsvr32.exe
filter_optional_edge_update:
  ParentImage|contains: \AppData\Local\Microsoft\EdgeUpdate\Install\{
  Image|endswith: \rundll32.exe
  CommandLine|endswith: rundll32.exe
filter_optional_chromium_installer:
  ParentImage|contains:
  - \AppData\Local\BraveSoftware\Brave-Browser\Application\
  - \AppData\Local\Google\Chrome\Application\
  ParentImage|endswith: \Installer\setup.exe
  ParentCommandLine|contains: '--uninstall '
  Image|endswith: \rundll32.exe
  CommandLine|endswith: rundll32.exe
condition: 1 of selection_* and not 1 of filter_optional_*
```

## False Positives

- Unlikely

## References

- https://blog.malwarebytes.com/malwarebytes-news/2020/10/kraken-attack-abuses-wer-service/
- https://www.cobaltstrike.com/help-opsec
- https://twitter.com/CyberRaiju/status/1251492025678983169
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/regsvr32
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32
- https://learn.microsoft.com/en-us/dotnet/framework/tools/regasm-exe-assembly-registration-tool
- https://learn.microsoft.com/en-us/dotnet/framework/tools/regsvcs-exe-net-services-installation-tool

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_bad_opsec_sacrificial_processes.yml)
