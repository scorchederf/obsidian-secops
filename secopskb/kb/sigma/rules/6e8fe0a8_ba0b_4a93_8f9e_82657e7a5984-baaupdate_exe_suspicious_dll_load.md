---
sigma_id: "6e8fe0a8-ba0b-4a93-8f9e-82657e7a5984"
title: "BaaUpdate.exe Suspicious DLL Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_susp_baaupdate_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_baaupdate_dll_load.yml"
build_date: "2026-04-27 19:13:50"
status: "experimental"
level: "high"
logsource: "windows / image_load"
aliases:
  - "6e8fe0a8-ba0b-4a93-8f9e-82657e7a5984"
  - "BaaUpdate.exe Suspicious DLL Load"
attack_technique_ids:
  - "T1218"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects BitLocker Access Agent Update Utility (baaupdate.exe) loading DLLs from suspicious locations that are publicly writable which could indicate an attempt to lateral movement via BitLocker DCOM & COM Hijacking.
This technique abuses COM Classes configured as INTERACTIVE USER to spawn processes in the context of the logged-on user's session. Specifically, it targets the BDEUILauncher Class (CLSID ab93b6f1-be76-4185-a488-a9001b105b94)
which can launch BaaUpdate.exe, which is vulnerable to COM Hijacking when started with input parameters. This allows attackers to execute code in the user's context without needing to steal credentials or use additional techniques to compromise the account.

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[kb/attack/techniques/T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]

## Detection

```yaml
selection:
  Image|endswith: \BaaUpdate.exe
  ImageLoaded|endswith: .dll
  ImageLoaded|contains:
  - :\Perflogs\
  - :\Users\Default\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
  - \AppData\Roaming\
  - \Contacts\
  - \Favorites\
  - \Favourites\
  - \Links\
  - \Music\
  - \Pictures\
  - \ProgramData\
  - \Temporary Internet
  - \Videos\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/rtecCyberSec/BitlockMove

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_baaupdate_dll_load.yml)
