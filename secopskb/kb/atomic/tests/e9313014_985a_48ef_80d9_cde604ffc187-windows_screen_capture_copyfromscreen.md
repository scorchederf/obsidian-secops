---
atomic_guid: "e9313014-985a-48ef-80d9-cde604ffc187"
title: "Windows Screen Capture (CopyFromScreen)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "e9313014-985a-48ef-80d9-cde604ffc187"
  - "Windows Screen Capture (CopyFromScreen)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Screen Capture (CopyFromScreen)

Take a screen capture of the desktop through a call to the [Graphics.CopyFromScreen] .NET API.
[Graphics.CopyFromScreen]: https://docs.microsoft.com/en-us/dotnet/api/system.drawing.graphics.copyfromscreen

## Metadata

- Atomic GUID: e9313014-985a-48ef-80d9-cde604ffc187
- Technique: T1113: Screen Capture
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1113/T1113.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Input Arguments

### output_file

- description: Path where captured results will be placed
- type: path
- default: $env:TEMP\T1113.png

## Executor

- name: powershell

### Command

```powershell
Add-Type -AssemblyName System.Windows.Forms
$screen = [Windows.Forms.SystemInformation]::VirtualScreen
$bitmap = New-Object Drawing.Bitmap $screen.Width, $screen.Height
$graphic = [Drawing.Graphics]::FromImage($bitmap)
$graphic.CopyFromScreen($screen.Left, $screen.Top, 0, 0, $bitmap.Size)
$bitmap.Save("#{output_file}")
```

### Cleanup

```powershell
Remove-Item #{output_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
