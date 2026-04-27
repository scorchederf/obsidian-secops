---
car_id: "CAR-2020-05-003"
title: "Rare LolBAS Command Lines"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-05-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-05-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-05-003"
  - "Rare LolBAS Command Lines"
attack_technique_ids:
  - "T1012"
  - "T1112"
  - "T1547"
  - "T1547.001"
  - "T1574"
  - "T1574.011"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2020-05-003: Rare LolBAS Command Lines

## Metadata

- CAR ID: CAR-2020-05-003
- Submission Date: 2020/05/04
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Cyber National Mission Force (CNMF)

## Description

[LoLBAS](https://lolbas-project.github.io/) are binaries and scripts that are built in to Windows, frequently are signed by Microsoft, and may be used by an attacker. Some LoLBAS are used very rarely and it might be possible to alert every time they're used (this would depend on your environment), but many others are very common and can't be simply alerted on.

This analytic takes all instances of LoLBAS execution and then looks for instances of command lines that are not normal in the environment. This can detect attackers (which will tend to need the binaries for something different than normal usage) but will also tend to have false positives.

The analytic needs to be tuned. The `1.5` in the query is the number of standard deviations away to look. It can be tuned up to filter out more noise and tuned down to get more results. This means it is probably best as a hunting analytic when you have analysts looking at the screen and able to tune the analytic up and down, because the threshold may not be stable for very long.

Note - this analytic is related to [CAR-2013-04-002](/analytics/CAR-2013-04-002), but differs by looking for a different set of binaries and also looking at standard deviation across command lines of these binaries instead of their execution within a short time window.

## ATT&CK Coverage

- [[kb/attack/techniques/T1012-query_registry|T1012]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1112-modify_registry|T1112]] (coverage: Low; tactics: TA0005)
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]] (coverage: Low; tactics: TA0003)
  - [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]] (coverage: Low; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Implementations

### Pseudocode

Pseudocode version of the below Splunk query.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
lolbas_processes = filter processes where (exe = "At.exe" OR exe = "Atbroker.exe" OR exe = "Bash.exe" OR exe = "Bitsadmin.exe" OR exe = "Certutil.exe" OR exe = "Cmd.exe" OR exe = "Cmdkey.exe" OR exe = "Cmstp.exe" OR exe = "Control.exe" OR exe = "Csc.exe" OR exe = "Cscript.exe" OR exe = "Dfsvc.exe" OR exe = "Diskshadow.exe" OR exe = "Dnscmd.exe" OR exe = "Esentutl.exe" OR exe = "Eventvwr.exe" OR exe = "Expand.exe" OR exe = "Extexport.exe" OR exe = "Extrac32.exe" OR exe = "Findstr.exe" OR exe = "Forfiles.exe" OR exe = "Ftp.exe" OR exe = "Gpscript.exe" OR exe = "Hh.exe" OR exe = "Ie4uinit.exe" OR exe = "Ieexec.exe" OR exe = "Infdefaultinstall.exe" OR exe = "Installutil.exe" OR exe = "Jsc.exe" OR exe = "Makecab.exe" OR exe = "Mavinject.exe" OR exe = "Microsoft.Workflow.r.exe" OR exe = "Mmc.exe" OR exe = "Msbuild.exe" OR exe = "Msconfig.exe" OR exe = "Msdt.exe" OR exe = "Mshta.exe" OR exe = "Msiexec.exe" OR exe = "Odbcconf.exe" OR exe = "Pcalua.exe" OR exe = "Pcwrun.exe" OR exe = "Presentationhost.exe" OR exe = "Print.exe" OR exe = "Reg.exe" OR exe = "Regasm.exe" OR exe = "Regedit.exe" OR exe = "Register-cimprovider.exe" OR exe = "Regsvcs.exe" OR exe = "Regsvr32.exe" OR exe = "Replace.exe" OR exe = "Rpcping.exe" OR exe = "Rundll32.exe" OR exe = "Runonce.exe" OR exe = "Runscripthelper.exe" OR exe = "Sc.exe" OR exe = "Schtasks.exe" OR exe = "Scriptrunner.exe" OR exe = "SyncAppvPublishingServer.exe" OR exe = "Tttracer.exe" OR exe = "Verclsid.exe" OR exe = "Wab.exe" OR exe = "Wmic.exe" OR exe = "Wscript.exe" OR exe = "Wsreset.exe" OR exe = "Xwizard.exe" OR exe = "Advpack.dll OR exe = "Comsvcs.dll OR exe = "Ieadvpack.dll OR exe = "Ieaframe.dll OR exe = "Mshtml.dll OR exe = "Pcwutl.dll OR exe = "Setupapi.dll OR exe = "Shdocvw.dll OR exe = "Shell32.dll OR exe = "Syssetup.dll OR exe = "Url.dll OR exe = "Zipfldr.dll OR exe = "Appvlp.exe" OR exe = "Bginfo.exe" OR exe = "Cdb.exe" OR exe = "csi.exe" OR exe = "Devtoolslauncher.exe" OR exe = "dnx.exe" OR exe = "Dxcap.exe" OR exe = "Excel.exe" OR exe = "Mftrace.exe" OR exe = "Msdeploy.exe" OR exe = "msxsl.exe" OR exe = "Powerpnt.exe" OR exe = "rcsi.exe" OR exe = "Sqler.exe" OR exe = "Sqlps.exe" OR exe = "SQLToolsPS.exe" OR exe = "Squirrel.exe" OR exe = "te.exe" OR exe = "Tracker.exe" OR exe = "Update.exe" OR exe = "vsjitdebugger.exe" OR exe = "Winword.exe" OR exe = "Wsl.exe" OR exe = "CL_Mutexverifiers.ps1 OR exe = "CL_Invocation.ps1 OR exe = "Manage-bde.wsf OR exe = "Pubprn.vbs OR exe = "Slmgr.vbs OR exe = "Syncappvpublishingserver.vbs OR exe = "winrm.vbs OR exe = "Pester.bat)
process_count = count(lolbas_processes) by process
process_count_avg = average(process_count)
process_count_stdev = standard_deviation(process_count)
lower_bound = process_count_avg - stdev * 1.5
outliers = filter lolbas_processes where (process_count < lower_bound)
return outliers
```

### Splunk

This Splunk query looks for instances of LoLBAS commands being executed, then stacks by rare command lines using a stddev.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 (OriginalFileName = At.exe OR OriginalFileName = Atbroker.exe OR OriginalFileName = Bash.exe OR OriginalFileName = Bitsadmin.exe OR OriginalFileName = Certutil.exe OR OriginalFileName = Cmd.exe OR OriginalFileName = Cmdkey.exe OR OriginalFileName = Cmstp.exe OR OriginalFileName = Control.exe OR OriginalFileName = Csc.exe OR OriginalFileName = Cscript.exe OR OriginalFileName = Dfsvc.exe OR OriginalFileName = Diskshadow.exe OR OriginalFileName = Dnscmd.exe OR OriginalFileName = Esentutl.exe OR OriginalFileName = Eventvwr.exe OR OriginalFileName = Expand.exe OR OriginalFileName = Extexport.exe OR OriginalFileName = Extrac32.exe OR OriginalFileName = Findstr.exe OR OriginalFileName = Forfiles.exe OR OriginalFileName = Ftp.exe OR OriginalFileName = Gpscript.exe OR OriginalFileName = Hh.exe OR OriginalFileName = Ie4uinit.exe OR OriginalFileName = Ieexec.exe OR OriginalFileName = Infdefaultinstall.exe OR OriginalFileName = Installutil.exe OR OriginalFileName = Jsc.exe OR OriginalFileName = Makecab.exe OR OriginalFileName = Mavinject.exe OR OriginalFileName = Microsoft.Workflow.r.exe OR OriginalFileName = Mmc.exe OR OriginalFileName = Msbuild.exe OR OriginalFileName = Msconfig.exe OR OriginalFileName = Msdt.exe OR OriginalFileName = Mshta.exe OR OriginalFileName = Msiexec.exe OR OriginalFileName = Odbcconf.exe OR OriginalFileName = Pcalua.exe OR OriginalFileName = Pcwrun.exe OR OriginalFileName = Presentationhost.exe OR OriginalFileName = Print.exe OR OriginalFileName = Reg.exe OR OriginalFileName = Regasm.exe OR OriginalFileName = Regedit.exe OR OriginalFileName = Register-cimprovider.exe OR OriginalFileName = Regsvcs.exe OR OriginalFileName = Regsvr32.exe OR OriginalFileName = Replace.exe OR OriginalFileName = Rpcping.exe OR OriginalFileName = Rundll32.exe OR OriginalFileName = Runonce.exe OR OriginalFileName = Runscripthelper.exe OR OriginalFileName = Sc.exe OR OriginalFileName = Schtasks.exe OR OriginalFileName = Scriptrunner.exe OR OriginalFileName = SyncAppvPublishingServer.exe OR OriginalFileName = Tttracer.exe OR OriginalFileName = Verclsid.exe OR OriginalFileName = Wab.exe OR OriginalFileName = Wmic.exe OR OriginalFileName = Wscript.exe OR OriginalFileName = Wsreset.exe OR OriginalFileName = Xwizard.exe OR OriginalFileName = Advpack.dll OR OriginalFileName = Comsvcs.dll OR OriginalFileName = Ieadvpack.dll OR OriginalFileName = Ieaframe.dll OR OriginalFileName = Mshtml.dll OR OriginalFileName = Pcwutl.dll OR OriginalFileName = Setupapi.dll OR OriginalFileName = Shdocvw.dll OR OriginalFileName = Shell32.dll OR OriginalFileName = Syssetup.dll OR OriginalFileName = Url.dll OR OriginalFileName = Zipfldr.dll OR OriginalFileName = Appvlp.exe OR OriginalFileName = Bginfo.exe OR OriginalFileName = Cdb.exe OR OriginalFileName = csi.exe OR OriginalFileName = Devtoolslauncher.exe OR OriginalFileName = dnx.exe OR OriginalFileName = Dxcap.exe OR OriginalFileName = Excel.exe OR OriginalFileName = Mftrace.exe OR OriginalFileName = Msdeploy.exe OR OriginalFileName = msxsl.exe OR OriginalFileName = Powerpnt.exe OR OriginalFileName = rcsi.exe OR OriginalFileName = Sqler.exe OR OriginalFileName = Sqlps.exe OR OriginalFileName = SQLToolsPS.exe OR OriginalFileName = Squirrel.exe OR OriginalFileName = te.exe OR OriginalFileName = Tracker.exe OR OriginalFileName = Update.exe OR OriginalFileName = vsjitdebugger.exe OR OriginalFileName = Winword.exe OR OriginalFileName = Wsl.exe OR OriginalFileName = CL_Mutexverifiers.ps1 OR OriginalFileName = CL_Invocation.ps1 OR OriginalFileName = Manage-bde.wsf OR OriginalFileName = Pubprn.vbs OR OriginalFileName = Slmgr.vbs OR OriginalFileName = Syncappvpublishingserver.vbs OR OriginalFileName = winrm.vbs OR OriginalFileName = Pester.bat)|eval CommandLine=lower(CommandLine)|eventstats count(process) as procCount by process|eventstats avg(procCount) as avg stdev(procCount) as stdev|eval lowerBound=(avg-stdev*1.5)|eval isOutlier=if((procCount < lowerBound),1,0)|where isOutlier=1|table host, Image, ParentImage, CommandLine, ParentCommandLine, procCount
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-05-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-05-003.yaml)
