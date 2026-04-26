---
sigma_id: "f5fe36cf-f1ec-4c23-903d-09a3110f6bbb"
title: "Potential ClickFix Execution Pattern - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_potential_clickfix_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_potential_clickfix_execution.yml"
build_date: "2026-04-26 15:01:48"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "f5fe36cf-f1ec-4c23-903d-09a3110f6bbb"
  - "Potential ClickFix Execution Pattern - Registry"
attack_technique_ids:
  - "T1204.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential ClickFix Execution Pattern - Registry

Detects potential ClickFix malware execution patterns by monitoring registry modifications in RunMRU keys containing HTTP/HTTPS links.
ClickFix is known to be distributed through phishing campaigns and uses techniques like clipboard hijacking and fake CAPTCHA pages.
Through the fakecaptcha pages, the adversary tricks users into opening the Run dialog box and pasting clipboard-hijacked content,
such as one-liners that execute remotely hosted malicious files or scripts.

## Metadata

- Rule ID: f5fe36cf-f1ec-4c23-903d-09a3110f6bbb
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-03-25
- Modified: 2025-11-19
- Source Path: rules/windows/registry/registry_set/registry_set_potential_clickfix_execution.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.001]]

## Detection

```yaml
selection_registry:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU\
selection_details:
  Details|contains:
  - http://
  - https://
selection_susp_pattern:
- Details|contains:
  - account
  - anti-bot
  - botcheck
  - captcha
  - challenge
  - confirmation
  - fraud
  - human
  - identification
  - identificator
  - identity
  - robot
  - validation
  - verification
  - verify
- Details|contains:
  - '%comspec%'
  - bitsadmin
  - certutil
  - cmd
  - cscript
  - curl
  - finger
  - mshta
  - powershell
  - pwsh
  - regsvr32
  - rundll32
  - schtasks
  - wget
  - wscript
condition: all of selection_*
```

## False Positives

- Legitimate applications using RunMRU with HTTP links

## References

- https://github.com/JohnHammond/recaptcha-phish
- https://www.zscaler.com/blogs/security-research/deepseek-lure-using-captchas-spread-malware
- https://www.threatdown.com/blog/clipboard-hijacker-tries-to-install-a-trojan/
- https://app.any.run/tasks/5c16b4db-4b36-4039-a0ed-9b09abff8be2
- https://www.esentire.com/security-advisories/netsupport-rat-clickfix-distribution
- https://medium.com/@boutnaru/the-windows-foreniscs-journey-run-mru-run-dialog-box-most-recently-used-57375a02d724
- https://unit42.paloaltonetworks.com/preventing-clickfix-attack-vector/
- https://medium.com/@poudelswachchhanda123/preventing-lnk-and-fakecaptcha-threats-a-system-hardening-approach-2f7b7ed2e493
- https://www.scpx.com.au/2025/11/16/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_potential_clickfix_execution.yml)
