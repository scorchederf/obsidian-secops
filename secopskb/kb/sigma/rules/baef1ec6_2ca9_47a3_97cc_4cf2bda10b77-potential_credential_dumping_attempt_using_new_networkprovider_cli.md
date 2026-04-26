---
sigma_id: "baef1ec6-2ca9-47a3-97cc-4cf2bda10b77"
title: "Potential Credential Dumping Attempt Using New NetworkProvider - CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_new_network_provider.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_new_network_provider.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "baef1ec6-2ca9-47a3-97cc-4cf2bda10b77"
  - "Potential Credential Dumping Attempt Using New NetworkProvider - CLI"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Credential Dumping Attempt Using New NetworkProvider - CLI

Detects when an attacker tries to add a new network provider in order to dump clear text credentials, similar to how the NPPSpy tool does it

## Metadata

- Rule ID: baef1ec6-2ca9-47a3-97cc-4cf2bda10b77
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-23
- Modified: 2023-02-02
- Source Path: rules/windows/process_creation/proc_creation_win_registry_new_network_provider.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \System\CurrentControlSet\Services\
  - \NetworkProvider
condition: selection
```

## False Positives

- Other legitimate network providers used and not filtred in this rule

## References

- https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/network-provider-settings-removed-in-place-upgrade
- https://github.com/gtworek/PSBits/tree/master/PasswordStealing/NPPSpy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_new_network_provider.yml)
