---
sigma_id: "c09dad97-1c78-4f71-b127-7edb2b8e491a"
title: "Execution of Suspicious File Type Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_non_exe_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_non_exe_image.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c09dad97-1c78-4f71-b127-7edb2b8e491a"
  - "Execution of Suspicious File Type Extension"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execution of Suspicious File Type Extension

Detects whether the image specified in a process creation event doesn't refer to an ".exe" (or other known executable extension) file. This can be caused by process ghosting or other unorthodox methods to start a process.
This rule might require some initial baselining to align with some third party tooling in the user environment.

## Metadata

- Rule ID: c09dad97-1c78-4f71-b127-7edb2b8e491a
- Status: test
- Level: medium
- Author: Max Altgelt (Nextron Systems)
- Date: 2021-12-09
- Modified: 2023-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_susp_non_exe_image.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
known_image_extension:
  Image|endswith:
  - .bin
  - .cgi
  - .com
  - .exe
  - .scr
  - .tmp
filter_main_image:
  Image:
  - System
  - Registry
  - MemCompression
  - vmmem
filter_main_msi_installers:
  Image|contains: :\Windows\Installer\MSI
filter_main_driver_store:
  Image|contains: :\Windows\System32\DriverStore\FileRepository\
filter_main_msi_rollbackfiles:
  Image|contains: :\Config.Msi\
  Image|endswith:
  - .rbf
  - .rbs
filter_main_windows_temp:
- ParentImage|contains: :\Windows\Temp\
- Image|contains: :\Windows\Temp\
filter_main_deleted:
  Image|contains: :\$Extend\$Deleted\
filter_main_empty:
  Image:
  - '-'
  - ''
filter_main_null:
  Image: null
filter_optional_avira:
  ParentImage|contains: :\ProgramData\Avira\
filter_optional_nvidia:
  Image|contains: NVIDIA\NvBackend\
  Image|endswith: .dat
filter_optional_winpakpro:
  Image|contains:
  - :\Program Files (x86)\WINPAKPRO\
  - :\Program Files\WINPAKPRO\
  Image|endswith: .ngn
filter_optional_myq_server:
  Image|endswith:
  - :\Program Files (x86)\MyQ\Server\pcltool.dll
  - :\Program Files\MyQ\Server\pcltool.dll
filter_optional_wsl:
  Image|contains|all:
  - \AppData\Local\Packages\
  - \LocalState\rootfs\
filter_optional_lzma_exe:
  Image|endswith: \LZMA_EXE
filter_optional_firefox:
  Image|contains: :\Program Files\Mozilla Firefox\
filter_optional_docker:
  ParentImage: C:\Windows\System32\services.exe
  Image|endswith: com.docker.service
condition: not known_image_extension and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://pentestlaboratories.com/2021/12/08/process-ghosting/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_non_exe_image.yml)
