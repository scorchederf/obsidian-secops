---
sigma_id: "ac9159cc-c364-4304-8f0a-d63fc1a0aabb"
title: "ClickOnce Trust Prompt Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_clickonce_trust_prompt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_clickonce_trust_prompt.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "ac9159cc-c364-4304-8f0a-d63fc1a0aabb"
  - "ClickOnce Trust Prompt Tampering"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ClickOnce Trust Prompt Tampering

Detects changes to the ClickOnce trust prompt registry key in order to enable an installation from different locations such as the Internet.

## Metadata

- Rule ID: ac9159cc-c364-4304-8f0a-d63fc1a0aabb
- Status: test
- Level: medium
- Author: @SerkinValery, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-12
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_clickonce_trust_prompt.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\MICROSOFT\.NETFramework\Security\TrustManager\PromptingLevel\
  TargetObject|endswith:
  - \Internet
  - \LocalIntranet
  - \MyComputer
  - \TrustedSites
  - \UntrustedSites
  Details: Enabled
condition: selection
```

## False Positives

- Legitimate internal requirements.

## References

- https://posts.specterops.io/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5
- https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_clickonce_trust_prompt.yml)
