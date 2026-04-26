---
sigma_id: "438025f9-5856-4663-83f7-52f878a70a50"
title: "Suspicious Microsoft Office Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_susp_child_processes.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "438025f9-5856-4663-83f7-52f878a70a50"
  - "Suspicious Microsoft Office Child Process"
attack_technique_ids:
  - "T1047"
  - "T1204.002"
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Microsoft Office Child Process

Detects a suspicious process spawning from one of the Microsoft Office suite products (Word, Excel, PowerPoint, Publisher, Visio, etc.)

## Metadata

- Rule ID: 438025f9-5856-4663-83f7-52f878a70a50
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Markus Neis, FPT.EagleEye Team, Vadim Khrykov, Cyb3rEng, Michael Haag, Christopher Peacock @securepeacock, @scythe_io
- Date: 2018-04-06
- Modified: 2023-04-24
- Source Path: rules/windows/process_creation/proc_creation_win_office_susp_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \EQNEDT32.EXE
  - \EXCEL.EXE
  - \MSACCESS.EXE
  - \MSPUB.exe
  - \ONENOTE.EXE
  - \POWERPNT.exe
  - \VISIO.exe
  - \WINWORD.EXE
  - \wordpad.exe
  - \wordview.exe
selection_child_processes:
- OriginalFileName:
  - bitsadmin.exe
  - CertOC.exe
  - CertUtil.exe
  - Cmd.Exe
  - CMSTP.EXE
  - cscript.exe
  - curl.exe
  - HH.exe
  - IEExec.exe
  - InstallUtil.exe
  - javaw.exe
  - Microsoft.Workflow.Compiler.exe
  - msdt.exe
  - MSHTA.EXE
  - msiexec.exe
  - Msxsl.exe
  - odbcconf.exe
  - pcalua.exe
  - PowerShell.EXE
  - RegAsm.exe
  - RegSvcs.exe
  - REGSVR32.exe
  - RUNDLL32.exe
  - schtasks.exe
  - ScriptRunner.exe
  - wmic.exe
  - WorkFolders.exe
  - wscript.exe
- Image|endswith:
  - \AppVLP.exe
  - \bash.exe
  - \bitsadmin.exe
  - \certoc.exe
  - \certutil.exe
  - \cmd.exe
  - \cmstp.exe
  - \control.exe
  - \cscript.exe
  - \curl.exe
  - \forfiles.exe
  - \hh.exe
  - \ieexec.exe
  - \installutil.exe
  - \javaw.exe
  - \mftrace.exe
  - \Microsoft.Workflow.Compiler.exe
  - \msbuild.exe
  - \msdt.exe
  - \mshta.exe
  - \msidb.exe
  - \msiexec.exe
  - \msxsl.exe
  - \odbcconf.exe
  - \pcalua.exe
  - \powershell.exe
  - \pwsh.exe
  - \regasm.exe
  - \regsvcs.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \schtasks.exe
  - \scrcons.exe
  - \scriptrunner.exe
  - \sh.exe
  - \svchost.exe
  - \verclsid.exe
  - \wmic.exe
  - \workfolders.exe
  - \wscript.exe
selection_child_susp_paths:
  Image|contains:
  - \AppData\
  - \Users\Public\
  - \ProgramData\
  - \Windows\Tasks\
  - \Windows\Temp\
  - \Windows\System32\Tasks\
condition: selection_parent and 1 of selection_child_*
```

## False Positives

- Unknown

## References

- https://www.hybrid-analysis.com/sample/465aabe132ccb949e75b8ab9c5bda36d80cf2fd503d52b8bad54e295f28bbc21?environmentId=100
- https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html
- https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/
- https://doublepulsar.com/follina-a-microsoft-office-code-execution-vulnerability-1a47fce5629e
- https://github.com/vadim-hunter/Detection-Ideas-Rules/blob/02bcbfc2bfb8b4da601bb30de0344ae453aa1afe/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sodinokibi_(aka_REvil)_Ransomware.yaml
- https://github.com/splunk/security_content/blob/300af51b88ad5d5b27ce4f5f54e4d6e6a3a2c06d/detections/endpoint/office_spawning_control.yml
- https://twitter.com/andythevariable/status/1576953781581144064?s=20&t=QiJILvK4ZiBdR8RJe24u-A
- https://www.elastic.co/security-labs/exploring-the-ref2731-intrusion-set
- https://github.com/elastic/detection-rules/blob/c76a39796972ecde44cb1da6df47f1b6562c9770/rules/windows/defense_evasion_execution_msbuild_started_by_office_app.toml
- https://www.vmray.com/analyses/2d2fa29185ad/report/overview.html
- https://app.any.run/tasks/c903e9c8-0350-440c-8688-3881b556b8e0/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_susp_child_processes.yml)
