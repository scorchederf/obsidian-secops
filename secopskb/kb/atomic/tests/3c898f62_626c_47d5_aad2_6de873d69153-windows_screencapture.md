---
atomic_guid: "3c898f62-626c-47d5-aad2-6de873d69153"
title: "Windows Screencapture"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3c898f62-626c-47d5-aad2-6de873d69153"
  - "Windows Screencapture"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Screencapture

Use Psr.exe binary to collect screenshots of user display. Test will do left mouse click to simulate user behaviour

## Metadata

- Atomic GUID: 3c898f62-626c-47d5-aad2-6de873d69153
- Technique: T1113: Screen Capture
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1113/T1113.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Input Arguments

### output_file

- description: Output file path
- type: path
- default: c:\temp\T1113_desktop.zip

### recording_time

- description: Time to take screenshots
- type: integer
- default: 5

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cmd /c start /b psr.exe /start /output #{output_file} /sc 1 /gui 0 /stopevent 12
Add-Type -MemberDefinition '[DllImport("user32.dll")] public static extern void mouse_event(int flags, int dx, int dy, int cButtons, int info);' -Name U32 -Namespace W;
[W.U32]::mouse_event(0x02 -bor 0x04 -bor 0x01, 0, 0, 0, 0);
cmd /c "timeout #{recording_time} > NULL && psr.exe /stop"
```

### Cleanup

```powershell
rm #{output_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
