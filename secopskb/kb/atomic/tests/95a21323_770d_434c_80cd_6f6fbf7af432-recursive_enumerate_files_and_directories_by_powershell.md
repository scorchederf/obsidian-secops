---
atomic_guid: "95a21323-770d-434c-80cd-6f6fbf7af432"
title: "Recursive Enumerate Files And Directories By Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "95a21323-770d-434c-80cd-6f6fbf7af432"
  - "Recursive Enumerate Files And Directories By Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Recursive Enumerate Files And Directories By Powershell

Adversary attempting to discover and collect sensitive documents and archives
from a user’s system. The test recursively enumerates common user folders
(Documents, Downloads, Desktop, OneDrive) for file types of interest such as .pdf, .doc,
.docx, .xls, .xlsx, .txt, .zip, .rar, and .7z.
This behavior is similar to malware like LOSTKEYS used by COLDRIVER in January 2025,
where attackers perform targeted file discovery to support strategic intelligence collection https://www.zscaler.com/blogs/security-research/coldriver-updates-arsenal-baitswitch-and-simplefix.

## Metadata

- Atomic GUID: 95a21323-770d-434c-80cd-6f6fbf7af432
- Technique: T1083: File and Directory Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Input Arguments

### output_file

- description: File to output results.
- type: string
- default: $env:TEMP\T1083-Enumerate-net.txt

## Executor

- name: powershell

### Command

```powershell
$out = "#{output_file}"
$dirsFilter = @('Documents','Downloads','Desktop','OneDrive')
$exts = @('.pdf','.doc','.docx','.xls','.xlsx','.txt','.zip','.rar','.7z')
$userProfile = [Environment]::GetFolderPath('UserProfile')
$tr = [System.Collections.Generic.List[string]]::new()

function MatchesExtension($path) {
  try {
    $e = [System.IO.Path]::GetExtension($path).ToLower()
    return $exts -contains $e
  } catch { return $false }
}

function Scan-Dir($root) {
  try {
    $match = $false
    foreach ($f in $dirsFilter) { if ($root -like "*$f*") { $match = $true; break } }
    if (-not $match) { return }

    [System.IO.Directory]::EnumerateFiles($root) | ForEach-Object {
      if (MatchesExtension $_) {
        $fi = [System.IO.FileInfo]::new($_)
        $tr.Add("[File] $_ Size:$($fi.Length) LastWrite:$($fi.LastWriteTime)")
      }
    }

    [System.IO.Directory]::EnumerateDirectories($root) | ForEach-Object {
      Scan-Dir $_
    }
  } catch [System.UnauthorizedAccessException] {
    $tr.Add("[AccessDenied] $root")
  } catch {
    $tr.Add("[Error] $root => $($_.Exception.Message)")
  }
}

[System.IO.Directory]::EnumerateDirectories($userProfile) | ForEach-Object { Scan-Dir $_ }

# Ensure output dir exists
$outDir = [System.IO.Path]::GetDirectoryName($out)
if (-not [string]::IsNullOrEmpty($outDir) -and -not (Test-Path $outDir)) {
  New-Item -Path $outDir -ItemType Directory -Force | Out-Null
}

# Write results
$tr | Out-File -FilePath $out -Encoding UTF8
Write-Output "Enumeration complete. Results written to: $out"
```

### Cleanup

```powershell
Remove-Item -Path "#{output_file}" -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
