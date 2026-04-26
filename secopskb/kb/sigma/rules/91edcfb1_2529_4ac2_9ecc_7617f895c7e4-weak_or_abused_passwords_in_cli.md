---
sigma_id: "91edcfb1-2529-4ac2-9ecc-7617f895c7e4"
title: "Weak or Abused Passwords In CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_weak_or_abused_passwords.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_weak_or_abused_passwords.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "91edcfb1-2529-4ac2-9ecc-7617f895c7e4"
  - "Weak or Abused Passwords In CLI"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Weak or Abused Passwords In CLI

Detects weak passwords or often abused passwords (seen used by threat actors) via the CLI.
An example would be a threat actor creating a new user via the net command and providing the password inline

## Metadata

- Rule ID: 91edcfb1-2529-4ac2-9ecc-7617f895c7e4
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-14
- Modified: 2024-02-23
- Source Path: rules/windows/process_creation/proc_creation_win_susp_weak_or_abused_passwords.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains:
  - '123456789'
  - 123123qwE
  - Asd123.aaaa
  - Decryptme
  - P@ssw0rd!
  - Pass8080
  - password123
  - test@202
condition: selection
```

## False Positives

- Legitimate usage of the passwords by users via commandline (should be discouraged)
- Other currently unknown false positives

## References

- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-asia-governments
- https://thedfirreport.com/2022/09/26/bumblebee-round-two/
- https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/
- https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_weak_or_abused_passwords.yml)
