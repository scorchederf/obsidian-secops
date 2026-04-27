---
atomic_guid: "5ff5249a-5807-480e-ab52-c430497a8a25"
title: "Outlook Rules - Enumerate Existing Rules via PowerShell COM Object"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.005"
attack_technique_name: "Office Application Startup: Outlook Rules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "5ff5249a-5807-480e-ab52-c430497a8a25"
  - "Outlook Rules - Enumerate Existing Rules via PowerShell COM Object"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerates all Outlook rules configured on the local profile using the
PowerShell COM object. Simulates the discovery phase where an adversary
audits existing rules before implanting their own, or where a threat actor
tool such as Ruler lists rules to understand the environment. This
enumeration should itself generate telemetry - use it to validate that
your monitoring catches PowerShell spawning Outlook COM for recon purposes.
NOTE: This test MUST be run from a non-elevated (standard user) PowerShell
session. Outlook COM fails with 0x80080005 when invoked as Administrator.

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup#^t1137005-outlook-rules|T1137.005: Outlook Rules]]

## Dependencies

Classic Outlook must be installed (required for COM automation)

### Prerequisite Check

```untitled
$clsid = (Get-ItemProperty "REGISTRY::HKEY_CLASSES_ROOT\Outlook.Application\CLSID" -ErrorAction SilentlyContinue).'(Default)'
if ($clsid) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```untitled
Write-Host "[-] Classic Outlook is not installed or COM is not registered."
Write-Host "    Install Microsoft 365 Apps with Classic Outlook before running this test."
Write-Host "    Note: The new Outlook for Windows does NOT support COM automation."
exit 1
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")
if ($isAdmin) {
    Write-Host "[-] This test must be run from a non-elevated PowerShell session."
    Write-Host "    Outlook COM fails with 0x80080005 when run as Administrator."
    exit 1
}

$outlook = New-Object -ComObject Outlook.Application
$rules   = $outlook.GetNamespace("MAPI").DefaultStore.GetRules()

Write-Host "`n[*] Enumerating Outlook rules on local profile..."
Write-Host "    Total rules found: $($rules.Count)`n"

for ($i = 1; $i -le $rules.Count; $i++) {
    $r = $rules.Item($i)
    Write-Host "  Rule $i : Name='$($r.Name)' | Enabled=$($r.Enabled)"
}

if ($rules.Count -eq 0) {
    Write-Host "  (No rules configured)"
}
```

### Cleanup

```powershell
Write-Host "[*] No cleanup required for enumeration test."
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml)
