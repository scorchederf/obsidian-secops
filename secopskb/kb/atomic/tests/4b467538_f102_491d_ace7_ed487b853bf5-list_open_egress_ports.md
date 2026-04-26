---
atomic_guid: "4b467538-f102-491d-ace7-ed487b853bf5"
title: "List Open Egress Ports"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4b467538-f102-491d-ace7-ed487b853bf5"
  - "List Open Egress Ports"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# List Open Egress Ports

This is to test for what ports are open outbound.  The technique used was taken from the following blog:
https://www.blackhillsinfosec.com/poking-holes-in-the-firewall-egress-testing-with-allports-exposed/

Upon successful execution, powershell will read top-128.txt (ports) and contact each port to confirm if open or not. Output will be to Desktop\open-ports.txt.

## Metadata

- Atomic GUID: 4b467538-f102-491d-ace7-ed487b853bf5
- Technique: T1016: System Network Configuration Discovery
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1016/T1016.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Input Arguments

### output_file

- description: Path of file to write port scan results
- type: path
- default: $env:USERPROFILE\Desktop\open-ports.txt

### port_file

- description: The path to a text file containing ports to be scanned, one port per line. The default list uses the top 128 ports as defined by Nmap.
- type: path
- default: PathToAtomicsFolder\T1016\src\top-128.txt

### portfile_url

- description: URL to top-128.txt
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1016/src/top-128.txt

## Dependencies

Test requires #{port_file} to exist

### Prerequisite Check

```powershell
if (Test-Path "#{port_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{port_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "#{portfile_url}" -OutFile "#{port_file}"
```

## Executor

- name: powershell

### Command

```powershell
$ports = Get-content "#{port_file}"
$file = "#{output_file}"
$totalopen = 0
$totalports = 0
New-Item $file -Force
foreach ($port in $ports) {
    $test = new-object system.Net.Sockets.TcpClient
    $wait = $test.beginConnect("allports.exposed", $port, $null, $null)
    $wait.asyncwaithandle.waitone(250, $false) | Out-Null
    $totalports++ | Out-Null
    if ($test.Connected) {
        $result = "$port open" 
        Write-Host -ForegroundColor Green $result
        $result | Out-File -Encoding ASCII -append $file
        $totalopen++ | Out-Null
    }
    else {
        $result = "$port closed" 
        Write-Host -ForegroundColor Red $result
        $totalclosed++ | Out-Null
        $result | Out-File -Encoding ASCII -append $file
    }
}
$results = "There were a total of $totalopen open ports out of $totalports ports tested."
$results | Out-File -Encoding ASCII -append $file
Write-Host $results
```

### Cleanup

```powershell
Remove-Item -ErrorAction ignore "#{output_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
