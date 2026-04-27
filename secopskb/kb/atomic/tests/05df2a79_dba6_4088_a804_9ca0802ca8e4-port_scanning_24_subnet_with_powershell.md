---
atomic_guid: "05df2a79-dba6-4088-a804-9ca0802ca8e4"
title: "Port-Scanning /24 Subnet with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "05df2a79-dba6-4088-a804-9ca0802ca8e4"
  - "Port-Scanning /24 Subnet with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Port-Scanning /24 Subnet with PowerShell

Scanning common ports in a /24 subnet. If no IP address for the target subnet is specified the test tries to determine the attacking machine's "primary" IPv4 address first and then scans that address with a /24 netmask.
The connection attempts to use a timeout parameter in milliseconds to speed up the scan. Please note the atomic might not print any output until the scans are completed.

## Metadata

- Atomic GUID: 05df2a79-dba6-4088-a804-9ca0802ca8e4
- Technique: T1046: Network Service Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1046/T1046.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Input Arguments

### ip_address

- description: IP-Address within the target subnet. Default is empty and script tries to determine local IP address of attacking machine. A comma separated list of targe IPs is also accepted (useful to simulate a wider scan while only scanning key host e.g., honeypots)
- type: string

### port_list

- description: Comma separated list of ports to scan
- type: string
- default: 445, 3389

### timeout_ms

- description: Connection timeout in milliseconds
- type: string
- default: 200

## Executor

- name: powershell

### Command

```powershell
$ipAddr = "#{ip_address}"
if ($ipAddr -like "*,*") {
    $ip_list = $ipAddr -split ","
    $ip_list = $ip_list.ForEach({ $_.Trim() })
    Write-Host "[i] IP Address List: $ip_list"

    $ports = #{port_list}

    foreach ($ip in $ip_list) {
        foreach ($port in $ports) {
            Write-Host "[i] Establishing connection to: $ip : $port"
            try {
                $tcp = New-Object Net.Sockets.TcpClient
                $tcp.ConnectAsync($ip, $port).Wait(#{timeout_ms}) | Out-Null
            } catch {}
            if ($tcp.Connected) {
                $tcp.Close()
                Write-Host "Port $port is open on $ip"
            }
        }
    }
} elseif ($ipAddr -notlike "*,*") {
    if ($ipAddr -eq "") {
        # Assumes the "primary" interface is shown at the top
        $interface = Get-NetIPInterface -AddressFamily IPv4 -ConnectionState Connected | Select-Object -ExpandProperty InterfaceAlias -First 1
        Write-Host "[i] Using Interface $interface"
        $ipAddr = Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias $interface | Select-Object -ExpandProperty IPAddress
    }
    Write-Host "[i] Base IP-Address for Subnet: $ipAddr"
    $subnetSubstring = $ipAddr.Substring(0, $ipAddr.LastIndexOf('.') + 1)
    # Always assumes /24 subnet
    Write-Host "[i] Assuming /24 subnet. scanning $subnetSubstring'1' to $subnetSubstring'254'"

    $ports = #{port_list}
    $subnetIPs = 1..254 | ForEach-Object { "$subnetSubstring$_" }

    foreach ($ip in $subnetIPs) {
        foreach ($port in $ports) {
            try {
                $tcp = New-Object Net.Sockets.TcpClient
                $tcp.ConnectAsync($ip, $port).Wait(#{timeout_ms}) | Out-Null
            } catch {}
            if ($tcp.Connected) {
                $tcp.Close()
                Write-Host "Port $port is open on $ip"
            }
        }
    }
} else {
    Write-Host "[Error] Invalid Inputs"
    exit 1
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
