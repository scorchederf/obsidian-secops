---
sigma_id: "d0d2f720-d14f-448d-8242-51ff396a334e"
title: "HackTool - Generic Process Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_hktl_generic_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_generic_access.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "d0d2f720-d14f-448d-8242-51ff396a334e"
  - "HackTool - Generic Process Access"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - Generic Process Access

Detects process access requests from hacktool processes based on their default image name

## Metadata

- Rule ID: d0d2f720-d14f-448d-8242-51ff396a334e
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel
- Date: 2023-11-27
- Source Path: rules/windows/process_access/proc_access_win_hktl_generic_access.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### Software Tags

- S0002

## Detection

```yaml
selection:
- SourceImage|endswith:
  - \Akagi.exe
  - \Akagi64.exe
  - \atexec_windows.exe
  - \Certify.exe
  - \Certipy.exe
  - \CoercedPotato.exe
  - \crackmapexec.exe
  - \CreateMiniDump.exe
  - \dcomexec_windows.exe
  - \dpapi_windows.exe
  - \findDelegation_windows.exe
  - \GetADUsers_windows.exe
  - \GetNPUsers_windows.exe
  - \getPac_windows.exe
  - \getST_windows.exe
  - \getTGT_windows.exe
  - \GetUserSPNs_windows.exe
  - \gmer.exe
  - \hashcat.exe
  - \htran.exe
  - \ifmap_windows.exe
  - \impersonate.exe
  - \Inveigh.exe
  - \LocalPotato.exe
  - \mimikatz_windows.exe
  - \mimikatz.exe
  - \netview_windows.exe
  - \nmapAnswerMachine_windows.exe
  - \opdump_windows.exe
  - \PasswordDump.exe
  - \Potato.exe
  - \PowerTool.exe
  - \PowerTool64.exe
  - \psexec_windows.exe
  - \PurpleSharp.exe
  - \pypykatz.exe
  - \QuarksPwDump.exe
  - \rdp_check_windows.exe
  - \Rubeus.exe
  - \SafetyKatz.exe
  - \sambaPipe_windows.exe
  - \SelectMyParent.exe
  - \SharpChisel.exe
  - \SharPersist.exe
  - \SharpEvtMute.exe
  - \SharpImpersonation.exe
  - \SharpLDAPmonitor.exe
  - \SharpLdapWhoami.exe
  - \SharpUp.exe
  - \SharpView.exe
  - \smbclient_windows.exe
  - \smbserver_windows.exe
  - \sniff_windows.exe
  - \sniffer_windows.exe
  - \split_windows.exe
  - \SpoolSample.exe
  - \Stracciatella.exe
  - \SysmonEOP.exe
  - \temp\rot.exe
  - \ticketer_windows.exe
  - \TruffleSnout.exe
  - \winPEASany_ofs.exe
  - \winPEASany.exe
  - \winPEASx64_ofs.exe
  - \winPEASx64.exe
  - \winPEASx86_ofs.exe
  - \winPEASx86.exe
  - \xordump.exe
- SourceImage|contains:
  - \goldenPac
  - \just_dce_
  - \karmaSMB
  - \kintercept
  - \LocalPotato
  - \ntlmrelayx
  - \rpcdump
  - \samrdump
  - \secretsdump
  - \smbexec
  - \smbrelayx
  - \wmiexec
  - \wmipersist
  - HotPotato
  - Juicy Potato
  - JuicyPotato
  - PetitPotam
  - RottenPotato
condition: selection
```

## False Positives

- Unlikely

## References

- https://jsecurity101.medium.com/bypassing-access-mask-auditing-strategies-480fb641c158
- https://www.splunk.com/en_us/blog/security/you-bet-your-lsass-hunting-lsass-access.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_generic_access.yml)
