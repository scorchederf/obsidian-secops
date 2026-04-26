---
sigma_id: "02d1d718-dd13-41af-989d-ea85c7fab93f"
title: "Rare Remote Thread Creation By Uncommon Source Image"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_susp_relevant_source_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_susp_relevant_source_image.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "02d1d718-dd13-41af-989d-ea85c7fab93f"
  - "Rare Remote Thread Creation By Uncommon Source Image"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Rare Remote Thread Creation By Uncommon Source Image

Detects uncommon processes creating remote threads.

## Metadata

- Rule ID: 02d1d718-dd13-41af-989d-ea85c7fab93f
- Status: test
- Level: high
- Author: Perez Diego (@darkquassar), oscd.community
- Date: 2019-10-27
- Modified: 2025-12-08
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_susp_relevant_source_image.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  SourceImage|endswith:
  - \bash.exe
  - \cscript.exe
  - \cvtres.exe
  - \defrag.exe
  - \dialer.exe
  - \dnx.exe
  - \esentutl.exe
  - \excel.exe
  - \expand.exe
  - \find.exe
  - \findstr.exe
  - \forfiles.exe
  - \gpupdate.exe
  - \hh.exe
  - \installutil.exe
  - \lync.exe
  - \makecab.exe
  - \mDNSResponder.exe
  - \monitoringhost.exe
  - \msbuild.exe
  - \mshta.exe
  - \mspaint.exe
  - \outlook.exe
  - \ping.exe
  - \provtool.exe
  - \python.exe
  - \regsvr32.exe
  - \robocopy.exe
  - \runonce.exe
  - \sapcimc.exe
  - \smartscreen.exe
  - \spoolsv.exe
  - \tstheme.exe
  - \userinit.exe
  - \vssadmin.exe
  - \vssvc.exe
  - \w3wp.exe
  - \winscp.exe
  - \winword.exe
  - \wmic.exe
  - \wscript.exe
filter_main_conhost:
  SourceImage:
  - C:\Windows\System32\Defrag.exe
  - C:\Windows\System32\makecab.exe
  TargetImage: C:\Windows\System32\conhost.exe
filter_main_provtol_svchost:
  SourceImage: C:\Windows\System32\provtool.exe
  TargetImage: C:\Windows\System32\svchost.exe
filter_main_provtool_system:
  SourceImage: C:\Windows\System32\provtool.exe
  TargetImage: System
filter_main_userinit:
  SourceImage: C:\Windows\System32\userinit.exe
  TargetImage: C:\Windows\explorer.exe
filter_main_winword:
  SourceImage|endswith: \WINWORD.EXE
  TargetImage|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
filter_main_ms_office:
  SourceImage|startswith:
  - C:\Program Files\Microsoft Office\
  - C:\Program Files (x86)\Microsoft Office\
  TargetImage: System
filter_optional_explorer_vmtools:
  SourceImage|endswith: \SysWOW64\explorer.exe
  TargetImage:
  - C:\Program Files (x86)\VMware\VMware Tools\vmtoolsd.exe
  - C:\Program Files\VMware\VMware Tools\vmtoolsd.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- This rule is best put in testing first in order to create a baseline that reflects the data in your environment.

## References

- Personal research, statistical analysis
- https://lolbas-project.github.io

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_susp_relevant_source_image.yml)
