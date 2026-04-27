---
sigma_id: "02ee49e2-e294-4d0f-9278-f5b3212fc588"
title: "New RUN Key Pointing to Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_run_key_img_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_run_key_img_folder.yml"
build_date: "2026-04-27 19:13:53"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "02ee49e2-e294-4d0f-9278-f5b3212fc588"
  - "New RUN Key Pointing to Suspicious Folder"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious new RUN key element pointing to an executable in a suspicious folder

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Detection

```yaml
selection_target:
  TargetObject|contains:
  - \Software\Microsoft\Windows\CurrentVersion\Run
  - \Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
  - \Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
selection_suspicious_paths_1:
  Details|contains:
  - :\Perflogs
  - :\ProgramData'
  - :\Windows\Temp
  - :\Temp
  - \AppData\Local\Temp
  - \AppData\Roaming
  - :\$Recycle.bin
  - :\Users\Default
  - :\Users\public
  - '%temp%'
  - '%tmp%'
  - '%Public%'
  - '%AppData%'
selection_suspicious_paths_user_1:
  Details|contains: :\Users\
selection_suspicious_paths_user_2:
  Details|contains:
  - \Favorites
  - \Favourites
  - \Contacts
  - \Music
  - \Pictures
  - \Documents
  - \Photos
filter_main_windows_update:
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\RunOnce\
  Image|startswith: C:\Windows\SoftwareDistribution\Download\
  Details|contains|all:
  - 'rundll32.exe '
  - C:\WINDOWS\system32\advpack.dll,DelNodeRunDLL32
  Details|contains:
  - \AppData\Local\Temp\
  - C:\Windows\Temp\
filter_optional_spotify:
  Image|endswith:
  - C:\Program Files\Spotify\Spotify.exe
  - C:\Program Files (x86)\Spotify\Spotify.exe
  - \AppData\Roaming\Spotify\Spotify.exe
  TargetObject|endswith: SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Spotify
  Details|endswith: Spotify.exe --autostart --minimized
condition: selection_target and (selection_suspicious_paths_1 or (all of selection_suspicious_paths_user_*
  )) and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Software using weird folders for updates

## References

- https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_run_key_img_folder.yml)
