---
sigma_id: "0f60b28c-64dd-4e2c-9a63-5334d3e3a6e6"
title: "Script Interpreter Spawning Credential Scanner - Windows"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_script_interpretor_spawn_credential_scanner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_script_interpretor_spawn_credential_scanner.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0f60b28c-64dd-4e2c-9a63-5334d3e3a6e6"
  - "Script Interpreter Spawning Credential Scanner - Windows"
attack_technique_ids:
  - "T1552"
  - "T1005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a script interpreter process (like node.js or bun) spawning a known credential scanning tool (e.g., trufflehog, gitleaks).
This behavior is indicative of an attempt to find and steal secrets, as seen in the "Shai-Hulud: The Second Coming" campaign.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[kb/attack/techniques/T1005-data_from_local_system|T1005: Data from Local System]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \node.exe
  - \bun.exe
selection_child:
- Image|endswith:
  - trufflehog.exe
  - gitleaks.exe
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_script_interpretor_spawn_credential_scanner.yml)
