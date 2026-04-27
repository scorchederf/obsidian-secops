---
sigma_id: "7021255e-5db3-4946-a8b9-0ba7a4644a69"
title: "Potential Provisioning Registry Key Abuse For Binary Proxy Execution - REG"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_provisioning_command_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_provisioning_command_abuse.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "7021255e-5db3-4946-a8b9-0ba7a4644a69"
  - "Potential Provisioning Registry Key Abuse For Binary Proxy Execution - REG"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential abuse of the provisioning registry key for indirect command execution through "Provlaunch.exe".

## Logsource

- category: registry_set
- definition: Requirements: The registry key "\SOFTWARE\Microsoft\Provisioning\Commands\" and its subkey must be monitored
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Provisioning\Commands\
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Provlaunch/
- https://twitter.com/0gtweet/status/1674399582162153472

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_provisioning_command_abuse.yml)
