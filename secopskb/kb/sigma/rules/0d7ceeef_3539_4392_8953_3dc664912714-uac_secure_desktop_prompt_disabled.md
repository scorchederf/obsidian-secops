---
sigma_id: "0d7ceeef-3539-4392-8953-3dc664912714"
title: "UAC Secure Desktop Prompt Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_uac_disable_secure_desktop_prompt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_disable_secure_desktop_prompt.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "0d7ceeef-3539-4392-8953-3dc664912714"
  - "UAC Secure Desktop Prompt Disabled"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Secure Desktop Prompt Disabled

Detects when an attacker tries to change User Account Control (UAC) elevation request destination via the "PromptOnSecureDesktop" value.
The "PromptOnSecureDesktop" setting specifically determines whether UAC prompts are displayed on the secure desktop. The secure desktop is a separate desktop environment that's isolated from other processes running on the system. It's designed to prevent malicious software from intercepting or tampering with UAC prompts.
When "PromptOnSecureDesktop" is set to 0, UAC prompts are displayed on the user's current desktop instead of the secure desktop. This reduces the level of security because it potentially exposes the prompts to manipulation by malicious software.

## Metadata

- Rule ID: 0d7ceeef-3539-4392-8953-3dc664912714
- Status: test
- Level: medium
- Author: frack113
- Date: 2024-05-10
- Source Path: rules/windows/registry/registry_set/registry_set_uac_disable_secure_desktop_prompt.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\Policies\System\PromptOnSecureDesktop
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/7e11e9b79583545f208a6dc3fa062f2ed443d999/atomics/T1548.002/T1548.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_disable_secure_desktop_prompt.yml)
