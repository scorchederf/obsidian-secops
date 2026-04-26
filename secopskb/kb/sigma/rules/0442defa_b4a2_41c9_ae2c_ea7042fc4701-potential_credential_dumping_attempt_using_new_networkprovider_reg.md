---
sigma_id: "0442defa-b4a2-41c9-ae2c-ea7042fc4701"
title: "Potential Credential Dumping Attempt Using New NetworkProvider - REG"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_new_network_provider.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_new_network_provider.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "0442defa-b4a2-41c9-ae2c-ea7042fc4701"
  - "Potential Credential Dumping Attempt Using New NetworkProvider - REG"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Credential Dumping Attempt Using New NetworkProvider - REG

Detects when an attacker tries to add a new network provider in order to dump clear text credentials, similar to how the NPPSpy tool does it

## Metadata

- Rule ID: 0442defa-b4a2-41c9-ae2c-ea7042fc4701
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-23
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_new_network_provider.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \System\CurrentControlSet\Services\
  - \NetworkProvider
filter:
  TargetObject|contains:
  - \System\CurrentControlSet\Services\WebClient\NetworkProvider
  - \System\CurrentControlSet\Services\LanmanWorkstation\NetworkProvider
  - \System\CurrentControlSet\Services\RDPNP\NetworkProvider
filter_valid_procs:
  Image: C:\Windows\System32\poqexec.exe
condition: selection and not 1 of filter*
```

## False Positives

- Other legitimate network providers used and not filtred in this rule

## References

- https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/network-provider-settings-removed-in-place-upgrade
- https://github.com/gtworek/PSBits/tree/master/PasswordStealing/NPPSpy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_new_network_provider.yml)
