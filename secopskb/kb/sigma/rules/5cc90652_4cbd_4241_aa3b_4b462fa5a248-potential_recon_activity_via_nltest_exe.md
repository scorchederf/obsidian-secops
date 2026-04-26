---
sigma_id: "5cc90652-4cbd-4241-aa3b-4b462fa5a248"
title: "Potential Recon Activity Via Nltest.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_nltest_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nltest_recon.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5cc90652-4cbd-4241-aa3b-4b462fa5a248"
  - "Potential Recon Activity Via Nltest.EXE"
attack_technique_ids:
  - "T1016"
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Recon Activity Via Nltest.EXE

Detects nltest commands that can be used for information discovery

## Metadata

- Rule ID: 5cc90652-4cbd-4241-aa3b-4b462fa5a248
- Status: test
- Level: medium
- Author: Craig Young, oscd.community, Georg Lauenstein
- Date: 2021-07-24
- Modified: 2023-12-15
- Source Path: rules/windows/process_creation/proc_creation_win_nltest_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
selection_nltest:
- Image|endswith: \nltest.exe
- OriginalFileName: nltestrk.exe
selection_recon:
- CommandLine|contains|all:
  - server
  - query
- CommandLine|contains:
  - /user
  - all_trusts
  - 'dclist:'
  - 'dnsgetdc:'
  - domain_trusts
  - 'dsgetdc:'
  - parentdomain
  - trusted_domains
condition: all of selection_*
```

## False Positives

- Legitimate administration use but user and host must be investigated

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731935(v=ws.11)
- https://thedfirreport.com/2021/08/16/trickbot-leads-up-to-fake-1password-installation/
- https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/
- https://book.hacktricks.xyz/windows/basic-cmd-for-pentesters
- https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-3-0-ransomware-attack/
- https://eqllib.readthedocs.io/en/latest/analytics/03e231a6-74bc-467a-acb1-e5676b0fb55e.html
- https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/
- https://github.com/redcanaryco/atomic-red-team/blob/5360c9d9ffa3b25f6495f7a16e267b719eba2c37/atomics/T1482/T1482.md#atomic-test-2---windows---discover-domain-trusts-with-nltest

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nltest_recon.yml)
