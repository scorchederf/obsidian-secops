---
sigma_id: "d223b46b-5621-4037-88fe-fda32eead684"
title: "New Root or CA or AuthRoot Certificate to Store"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_install_root_or_ca_certificat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_install_root_or_ca_certificat.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "d223b46b-5621-4037-88fe-fda32eead684"
  - "New Root or CA or AuthRoot Certificate to Store"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Root or CA or AuthRoot Certificate to Store

Detects the addition of new root, CA or AuthRoot certificates to the Windows registry

## Metadata

- Rule ID: d223b46b-5621-4037-88fe-fda32eead684
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-04
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_install_root_or_ca_certificat.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \SOFTWARE\Microsoft\SystemCertificates\Root\Certificates\
  - \SOFTWARE\Policies\Microsoft\SystemCertificates\Root\Certificates\
  - \SOFTWARE\Microsoft\EnterpriseCertificates\Root\Certificates\
  - \SOFTWARE\Microsoft\SystemCertificates\CA\Certificates\
  - \SOFTWARE\Policies\Microsoft\SystemCertificates\CA\Certificates\
  - \SOFTWARE\Microsoft\EnterpriseCertificates\CA\Certificates\
  - \SOFTWARE\Microsoft\SystemCertificates\AuthRoot\Certificates\
  - \SOFTWARE\Policies\Microsoft\SystemCertificates\AuthRoot\Certificates\
  - \SOFTWARE\Microsoft\EnterpriseCertificates\AuthRoot\Certificates\
  TargetObject|endswith: \Blob
  Details: Binary Data
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.004/T1553.004.md#atomic-test-6---add-root-certificate-to-currentuser-certificate-store
- https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_install_root_or_ca_certificat.yml)
