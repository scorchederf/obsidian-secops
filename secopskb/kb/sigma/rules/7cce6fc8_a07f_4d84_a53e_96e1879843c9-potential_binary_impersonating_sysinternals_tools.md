---
sigma_id: "7cce6fc8-a07f-4d84-a53e-96e1879843c9"
title: "Potential Binary Impersonating Sysinternals Tools"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_tools_masquerading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_tools_masquerading.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7cce6fc8-a07f-4d84-a53e-96e1879843c9"
  - "Potential Binary Impersonating Sysinternals Tools"
attack_technique_ids:
  - "T1218"
  - "T1202"
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Binary Impersonating Sysinternals Tools

Detects binaries that use the same name as legitimate sysinternals tools to evade detection.
This rule looks for the execution of binaries that are named similarly to Sysinternals tools.
Adversary may rename their malicious tools as legitimate Sysinternals tools to evade detection.

## Metadata

- Rule ID: 7cce6fc8-a07f-4d84-a53e-96e1879843c9
- Status: test
- Level: medium
- Author: frack113, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2021-12-20
- Modified: 2025-04-12
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_tools_masquerading.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]
- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection_exe:
  Image|endswith:
  - \accesschk.exe
  - \accesschk64.exe
  - \AccessEnum.exe
  - \ADExplorer.exe
  - \ADExplorer64.exe
  - \ADInsight.exe
  - \ADInsight64.exe
  - \adrestore.exe
  - \adrestore64.exe
  - \Autologon.exe
  - \Autologon64.exe
  - \Autoruns.exe
  - \Autoruns64.exe
  - \autorunsc.exe
  - \autorunsc64.exe
  - \Bginfo.exe
  - \Bginfo64.exe
  - \Cacheset.exe
  - \Cacheset64.exe
  - \Clockres.exe
  - \Clockres64.exe
  - \Contig.exe
  - \Contig64.exe
  - \Coreinfo.exe
  - \Coreinfo64.exe
  - \CPUSTRES.EXE
  - \CPUSTRES64.EXE
  - \ctrl2cap.exe
  - \Dbgview.exe
  - \dbgview64.exe
  - \Desktops.exe
  - \Desktops64.exe
  - \disk2vhd.exe
  - \disk2vhd64.exe
  - \diskext.exe
  - \diskext64.exe
  - \Diskmon.exe
  - \Diskmon64.exe
  - \DiskView.exe
  - \DiskView64.exe
  - \du.exe
  - \du64.exe
  - \efsdump.exe
  - \FindLinks.exe
  - \FindLinks64.exe
  - \handle.exe
  - \handle64.exe
  - \hex2dec.exe
  - \hex2dec64.exe
  - \junction.exe
  - \junction64.exe
  - \ldmdump.exe
  - \listdlls.exe
  - \listdlls64.exe
  - \livekd.exe
  - \livekd64.exe
  - \loadOrd.exe
  - \loadOrd64.exe
  - \loadOrdC.exe
  - \loadOrdC64.exe
  - \logonsessions.exe
  - \logonsessions64.exe
  - \movefile.exe
  - \movefile64.exe
  - \notmyfault.exe
  - \notmyfault64.exe
  - \notmyfaultc.exe
  - \notmyfaultc64.exe
  - \ntfsinfo.exe
  - \ntfsinfo64.exe
  - \pendmoves.exe
  - \pendmoves64.exe
  - \pipelist.exe
  - \pipelist64.exe
  - \portmon.exe
  - \procdump.exe
  - \procdump64.exe
  - \procexp.exe
  - \procexp64.exe
  - \Procmon.exe
  - \Procmon64.exe
  - \psExec.exe
  - \psExec64.exe
  - \psfile.exe
  - \psfile64.exe
  - \psGetsid.exe
  - \psGetsid64.exe
  - \psInfo.exe
  - \psInfo64.exe
  - \pskill.exe
  - \pskill64.exe
  - \pslist.exe
  - \pslist64.exe
  - \psLoggedon.exe
  - \psLoggedon64.exe
  - \psloglist.exe
  - \psloglist64.exe
  - \pspasswd.exe
  - \pspasswd64.exe
  - \psping.exe
  - \psping64.exe
  - \psService.exe
  - \psService64.exe
  - \psshutdown.exe
  - \psshutdown64.exe
  - \pssuspend.exe
  - \pssuspend64.exe
  - \RAMMap.exe
  - \RAMMap64.exe
  - \RDCMan.exe
  - \RegDelNull.exe
  - \RegDelNull64.exe
  - \regjump.exe
  - \ru.exe
  - \ru64.exe
  - \sdelete.exe
  - \sdelete64.exe
  - \ShareEnum.exe
  - \ShareEnum64.exe
  - \shellRunas.exe
  - \sigcheck.exe
  - \sigcheck64.exe
  - \streams.exe
  - \streams64.exe
  - \strings.exe
  - \strings64.exe
  - \sync.exe
  - \sync64.exe
  - \Sysmon.exe
  - \Sysmon64.exe
  - \tcpvcon.exe
  - \tcpvcon64.exe
  - \tcpview.exe
  - \tcpview64.exe
  - \Testlimit.exe
  - \Testlimit64.exe
  - \vmmap.exe
  - \vmmap64.exe
  - \Volumeid.exe
  - \Volumeid64.exe
  - \whois.exe
  - \whois64.exe
  - \Winobj.exe
  - \Winobj64.exe
  - \ZoomIt.exe
  - \ZoomIt64.exe
selection_arm64:
  Image|endswith:
  - \accesschk64a.exe
  - \ADExplorer64a.exe
  - \ADInsight64a.exe
  - \adrestore64a.exe
  - \Autologon64a.exe
  - \Autoruns64a.exe
  - \autorunsc64a.exe
  - \Clockres64a.exe
  - \Contig64a.exe
  - \Coreinfo64a.exe
  - \Dbgview64a.exe
  - \disk2vhd64a.exe
  - \diskext64a.exe
  - \DiskView64a.exe
  - \du64a.exe
  - \FindLinks64a.exe
  - \handle64a.exe
  - \hex2dec64a.exe
  - \junction64a.exe
  - \LoadOrd64a.exe
  - \LoadOrdC64a.exe
  - \logonsessions64a.exe
  - \movefile64a.exe
  - \notmyfault64a.exe
  - \notmyfaultc64a.exe
  - \pendmoves64a.exe
  - \pipelist64a.exe
  - \procdump64a.exe
  - \procexp64a.exe
  - \Procmon64a.exe
  - \PsExec64a.exe
  - \psfile64a.exe
  - \PsGetsid64a.exe
  - \PsInfo64a.exe
  - \pskill64a.exe
  - \psloglist64a.exe
  - \pspasswd64a.exe
  - \psping64a.exe
  - \PsService64a.exe
  - \pssuspend64a.exe
  - \RAMMap64a.exe
  - \RegDelNull64a.exe
  - \ru64a.exe
  - \sdelete64a.exe
  - \sigcheck64a.exe
  - \streams64a.exe
  - \strings64a.exe
  - \sync64a.exe
  - \Sysmon64a.exe
  - \tcpvcon64a.exe
  - \tcpview64a.exe
  - \vmmap64a.exe
  - \whois64a.exe
  - \Winobj64a.exe
  - \ZoomIt64a.exe
filter_valid:
- Company:
  - Sysinternals - www.sysinternals.com
  - Sysinternals
- Product|startswith: Sysinternals
filter_empty:
- Company: null
- Product: null
condition: 1 of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_tools_masquerading.yml)
