---
sigma_id: "f0025a69-e1b7-4dda-a53c-db21fa2d4071"
title: "Script Interpreter Spawning Credential Scanner - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_script_interpretor_spawn_credential_scanner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_script_interpretor_spawn_credential_scanner.yml"
build_date: "2026-04-26 14:14:35"
status: "experimental"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "f0025a69-e1b7-4dda-a53c-db21fa2d4071"
  - "Script Interpreter Spawning Credential Scanner - Linux"
attack_technique_ids:
  - "T1552"
  - "T1005"
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Script Interpreter Spawning Credential Scanner - Linux

Detects a script interpreter process (like node.js or bun) spawning a known credential scanning tool (e.g., trufflehog, gitleaks).
This behavior is indicative of an attempt to find and steal secrets, as seen in the "Shai-Hulud: The Second Coming" campaign.

## Metadata

- Rule ID: f0025a69-e1b7-4dda-a53c-db21fa2d4071
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-25
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_script_interpretor_spawn_credential_scanner.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]
- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - /node
  - /bun
selection_child:
- Image|endswith:
  - /trufflehog
  - /gitleaks
- CommandLine|contains:
  - trufflehog
  - gitleaks
condition: all of selection_*
```

## False Positives

- Legitimate pre-commit hooks or CI/CD pipeline jobs that use a script to run a credential scanner as part of a security check.

## References

- https://github.com/asyncapi/cli/blob/2efa4dff59bc3d3cecdf897ccf178f99b115d63d/bun_environment.js
- https://www.stepsecurity.io/blog/sha1-hulud-the-second-coming-zapier-ens-domains-and-other-prominent-npm-packages-compromised
- https://www.endorlabs.com/learn/shai-hulud-2-malware-campaign-targets-github-and-cloud-credentials-using-bun-runtime
- https://semgrep.dev/blog/2025/digging-for-secrets-sha1-hulud-the-second-coming-of-the-npm-worm/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_script_interpretor_spawn_credential_scanner.yml)
