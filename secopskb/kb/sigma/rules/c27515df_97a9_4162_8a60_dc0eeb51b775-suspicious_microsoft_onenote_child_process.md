---
sigma_id: "c27515df-97a9-4162-8a60-dc0eeb51b775"
title: "Suspicious Microsoft OneNote Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_onenote_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_onenote_susp_child_processes.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c27515df-97a9-4162-8a60-dc0eeb51b775"
  - "Suspicious Microsoft OneNote Child Process"
attack_technique_ids:
  - "T1566"
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious child processes of the Microsoft OneNote application. This may indicate an attempt to execute malicious embedded objects from a .one file.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566: Phishing]]
- [[kb/attack/techniques/T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \onenote.exe
selection_opt_img:
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
selection_opt_explorer:
  Image|endswith: \explorer.exe
  CommandLine|contains:
  - .hta
  - .vb
  - .wsh
  - .js
  - .ps
  - .scr
  - .pif
  - .bat
  - .cmd
selection_opt_paths:
  Image|contains:
  - \AppData\
  - \Users\Public\
  - \ProgramData\
  - \Windows\Tasks\
  - \Windows\Temp\
  - \Windows\System32\Tasks\
filter_teams:
  Image|endswith: \AppData\Local\Microsoft\Teams\current\Teams.exe
  CommandLine|endswith: -Embedding
filter_onedrive:
  Image|contains: \AppData\Local\Microsoft\OneDrive\
  Image|endswith: \FileCoAuth.exe
  CommandLine|endswith: -Embedding
condition: selection_parent and 1 of selection_opt_* and not 1 of filter_*
```

## False Positives

- File located in the AppData folder with trusted signature

## References

- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-e34e43eb5666427602ddf488b2bf3b545bd9aae81af3e6f6c7949f9652abdf18
- https://micahbabinski.medium.com/detecting-onenote-one-malware-delivery-407e9321ecf0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_onenote_susp_child_processes.yml)
