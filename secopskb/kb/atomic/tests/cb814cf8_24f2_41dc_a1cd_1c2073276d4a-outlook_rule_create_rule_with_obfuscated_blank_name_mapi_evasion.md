---
atomic_guid: "cb814cf8-24f2-41dc-a1cd-1c2073276d4a"
title: "Outlook Rule - Create Rule with Obfuscated Blank Name (MAPI Evasion)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.005"
attack_technique_name: "Office Application Startup: Outlook Rules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "cb814cf8-24f2-41dc-a1cd-1c2073276d4a"
  - "Outlook Rule - Create Rule with Obfuscated Blank Name (MAPI Evasion)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Outlook Rule - Create Rule with Obfuscated Blank Name (MAPI Evasion)

Creates an Outlook rule with a zero-width space as its display name,
making it appear blank and invisible in the standard Outlook Rules UI.
Simulates the hidden inbox rule technique documented by Damian Pfammatter
(2018) and referenced in MITRE ATT&CK T1137.005 - adversaries use MAPI
editors or Ruler to blank PR_RULE_MSG_NAME so the rule does not appear
during casual rule auditing. Tests whether monitoring catches rules that
are invisible in the Outlook GUI but detectable via MFCMapi or
Get-InboxRule on Exchange. Uses PlaySound action as RunApplication
cannot be created programmatically per Microsoft's Rules object model.
NOTE: This test MUST be run from a non-elevated (standard user) PowerShell
session. Outlook COM fails with 0x80080005 when invoked as Administrator.
NOTE: Script is written to a temp file before execution to prevent the
ART executor's quote-wrapping from mangling the zero-width space bytes.

## Metadata

- Atomic GUID: cb814cf8-24f2-41dc-a1cd-1c2073276d4a
- Technique: T1137.005: Office Application Startup: Outlook Rules
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1137.005/T1137.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup|T1137.005]]

## Input Arguments

### sound_file_path

- description: Path to .wav file used as the rule action payload indicator
- type: string
- default: C:\Windows\Media\notify.wav

### trigger_subject

- description: Subject keyword to trigger the hidden rule
- type: string
- default: atomic-rt-hidden

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

Sound file must exist for PlaySound action

### Prerequisite Check

```text
if (Test-Path "#{sound_file_path}") { exit 0 } else { exit 1 }
```

### Get Prerequisite

```text
Write-Host "[-] Sound file not found at #{sound_file_path}"
Write-Host "    Specify a valid .wav file path in the sound_file_path input argument."
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
$tmpScript = "$env:TEMP\T1137005_hidden_rule_create.ps1"
$lines = @(
    '$hiddenName = [System.Text.Encoding]::Unicode.GetString([byte[]](0x0B, 0x20))',
    '$outlook   = New-Object -ComObject Outlook.Application',
    '$namespace = $outlook.GetNamespace("MAPI")',
    '$rules     = $namespace.DefaultStore.GetRules()',
    '$rule      = $rules.Create($hiddenName, 0)',
    '$cond = $rule.Conditions.Subject',
    '$cond.Enabled = $true',
    '$cond.Text    = @("#{trigger_subject}")',
    '$action          = $rule.Actions.PlaySound',
    '$action.Enabled  = $true',
    '$action.FilePath = "#{sound_file_path}"',
    '$rule.Enabled = $true',
    '$rules.Save()',
    'Write-Host "[+] Hidden rule created with zero-width space name."',
    'Write-Host "[*] Open Outlook via File -> Manage Rules and Alerts - rule name will appear blank."',
    'Write-Host "[*] Verify rule exists via PowerShell COM enumeration (Test 4) or Get-InboxRule in Exchange."'
)
$lines -join "`n" | Set-Content -Path $tmpScript -Encoding UTF8
powershell.exe -NoProfile -ExecutionPolicy Bypass -File $tmpScript
Remove-Item $tmpScript -ErrorAction SilentlyContinue
```

### Cleanup

```powershell
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")
if ($isAdmin) {
    Write-Host "[-] Cleanup must be run from a non-elevated PowerShell session. Skipping."
    exit 1
}
$tmpScript = "$env:TEMP\T1137005_hidden_rule_cleanup.ps1"
$lines = @(
    '$hiddenName = [System.Text.Encoding]::Unicode.GetString([byte[]](0x0B, 0x20))',
    '$outlook    = New-Object -ComObject Outlook.Application',
    '$namespace  = $outlook.GetNamespace("MAPI")',
    '$rules      = $namespace.DefaultStore.GetRules()',
    '$removed    = $false',
    'for ($i = $rules.Count; $i -ge 1; $i--) {',
    '    if ($rules.Item($i).Name -eq $hiddenName) {',
    '        $rules.Remove($rules.Item($i).Name)',
    '        $removed = $true',
    '    }',
    '}',
    'if ($removed) {',
    '    $rules.Save()',
    '    Write-Host "[+] Hidden rule(s) removed."',
    '} else {',
    '    Write-Host "[-] Hidden rule not found - may have already been removed."',
    '}'
)
$lines -join "`n" | Set-Content -Path $tmpScript -Encoding UTF8
powershell.exe -NoProfile -ExecutionPolicy Bypass -File $tmpScript
Remove-Item $tmpScript -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.005/T1137.005.yaml)
