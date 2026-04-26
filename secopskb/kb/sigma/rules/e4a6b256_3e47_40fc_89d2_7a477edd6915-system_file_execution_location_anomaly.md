---
sigma_id: "e4a6b256-3e47-40fc-89d2-7a477edd6915"
title: "System File Execution Location Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_system_exe_anomaly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_system_exe_anomaly.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e4a6b256-3e47-40fc-89d2-7a477edd6915"
  - "System File Execution Location Anomaly"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System File Execution Location Anomaly

Detects the execution of a Windows system binary that is usually located in the system folder from an uncommon location.

## Metadata

- Rule ID: e4a6b256-3e47-40fc-89d2-7a477edd6915
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Patrick Bareiss, Anton Kutepov, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2017-11-27
- Modified: 2026-02-12
- Source Path: rules/windows/process_creation/proc_creation_win_susp_system_exe_anomaly.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  Image|endswith:
  - \atbroker.exe
  - \audiodg.exe
  - \bcdedit.exe
  - \bitsadmin.exe
  - \certreq.exe
  - \certutil.exe
  - \cmstp.exe
  - \conhost.exe
  - \consent.exe
  - \cscript.exe
  - \csrss.exe
  - \dashost.exe
  - \defrag.exe
  - \dfrgui.exe
  - \dism.exe
  - \dllhost.exe
  - \dllhst3g.exe
  - \dwm.exe
  - \eventvwr.exe
  - \fsquirt.exe
  - \finger.exe
  - \logonui.exe
  - \LsaIso.exe
  - \lsass.exe
  - \lsm.exe
  - \msiexec.exe
  - \ntoskrnl.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \runonce.exe
  - \RuntimeBroker.exe
  - \schtasks.exe
  - \services.exe
  - \sihost.exe
  - \smartscreen.exe
  - \smss.exe
  - \spoolsv.exe
  - \svchost.exe
  - \taskhost.exe
  - \taskhostw.exe
  - \Taskmgr.exe
  - \userinit.exe
  - \werfault.exe
  - \werfaultsecure.exe
  - \wininit.exe
  - \winlogon.exe
  - \winver.exe
  - \wlanext.exe
  - \wscript.exe
  - \wsl.exe
  - \wsmprovhost.exe
filter_main_generic:
  Image|startswith:
  - C:\$WINDOWS.~BT\
  - C:\$WinREAgent\
  - C:\Windows\SoftwareDistribution\
  - C:\Windows\System32\
  - C:\Windows\SystemTemp\
  - C:\Windows\SysWOW64\
  - C:\Windows\uus\
  - C:\Windows\WinSxS\
filter_optional_system32:
  Image|contains: \SystemRoot\System32\
filter_main_powershell:
  Image|contains:
  - C:\Program Files\PowerShell\7\
  - C:\Program Files\PowerShell\7-preview\
  - C:\Program Files\WindowsApps\Microsoft.PowerShellPreview
  - \AppData\Local\Microsoft\WindowsApps\Microsoft.PowerShellPreview
  Image|endswith: \pwsh.exe
filter_main_wsl_programfiles:
  Image|startswith:
  - C:\Program Files\WindowsApps\MicrosoftCorporationII.WindowsSubsystemForLinux
  - C:\Program Files\WSL\
  Image|endswith: \wsl.exe
filter_main_wsl_appdata:
  Image|startswith: C:\Users\'
  Image|contains: \AppData\Local\Microsoft\WindowsApps\
  Image|endswith: \wsl.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://twitter.com/GelosSnake/status/934900723426439170
- https://asec.ahnlab.com/en/39828/
- https://www.splunk.com/en_us/blog/security/inno-setup-malware-redline-stealer-campaign.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_system_exe_anomaly.yml)
