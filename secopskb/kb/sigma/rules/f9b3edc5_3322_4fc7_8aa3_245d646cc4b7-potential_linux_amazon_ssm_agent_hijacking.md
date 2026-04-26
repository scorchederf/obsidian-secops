---
sigma_id: "f9b3edc5-3322-4fc7-8aa3-245d646cc4b7"
title: "Potential Linux Amazon SSM Agent Hijacking"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_ssm_agent_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_ssm_agent_abuse.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "f9b3edc5-3322-4fc7-8aa3-245d646cc4b7"
  - "Potential Linux Amazon SSM Agent Hijacking"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Linux Amazon SSM Agent Hijacking

Detects potential Amazon SSM agent hijack attempts as outlined in the Mitiga research report.

## Metadata

- Rule ID: f9b3edc5-3322-4fc7-8aa3-245d646cc4b7
- Status: test
- Level: medium
- Author: Muhammad Faisal
- Date: 2023-08-03
- Source Path: rules/linux/process_creation/proc_creation_lnx_ssm_agent_abuse.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  Image|endswith: /amazon-ssm-agent
  CommandLine|contains|all:
  - '-register '
  - '-code '
  - '-id '
  - '-region '
condition: selection
```

## False Positives

- Legitimate activity of system administrators

## References

- https://www.mitiga.io/blog/mitiga-security-advisory-abusing-the-ssm-agent-as-a-remote-access-trojan
- https://www.bleepingcomputer.com/news/security/amazons-aws-ssm-agent-can-be-used-as-post-exploitation-rat-malware/
- https://www.helpnetsecurity.com/2023/08/02/aws-instances-attackers-access/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_ssm_agent_abuse.yml)
