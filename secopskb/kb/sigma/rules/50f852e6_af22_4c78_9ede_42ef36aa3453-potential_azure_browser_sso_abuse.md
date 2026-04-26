---
sigma_id: "50f852e6-af22-4c78-9ede-42ef36aa3453"
title: "Potential Azure Browser SSO Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_azure_microsoft_account_token_provider_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_azure_microsoft_account_token_provider_dll_load.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "low"
logsource: "windows / image_load"
aliases:
  - "50f852e6-af22-4c78-9ede-42ef36aa3453"
  - "Potential Azure Browser SSO Abuse"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Azure Browser SSO Abuse

Detects abusing Azure Browser SSO by requesting OAuth 2.0 refresh tokens for an Azure-AD-authenticated Windows user (i.e. the machine is joined to Azure AD and a user logs in with their Azure AD account) wanting to perform SSO authentication in the browser.
An attacker can use this to authenticate to Azure AD in a browser as that user.

## Metadata

- Rule ID: 50f852e6-af22-4c78-9ede-42ef36aa3453
- Status: test
- Level: low
- Author: Den Iuzvyk
- Date: 2020-07-15
- Modified: 2023-04-18
- Source Path: rules/windows/image_load/image_load_dll_azure_microsoft_account_token_provider_dll_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded: C:\Windows\System32\MicrosoftAccountTokenProvider.dll
filter_main_bgtaskhost:
  Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  Image|endswith: \BackgroundTaskHost.exe
filter_optional_devenv:
  Image|startswith:
  - C:\Program Files\Microsoft Visual Studio\
  - C:\Program Files (x86)\Microsoft Visual Studio\
  Image|endswith: \IDE\devenv.exe
filter_optional_ie:
  Image:
  - C:\Program Files (x86)\Internet Explorer\iexplore.exe
  - C:\Program Files\Internet Explorer\iexplore.exe
filter_optional_edge_1:
- Image|startswith: C:\Program Files (x86)\Microsoft\EdgeWebView\Application\
- Image|endswith: \WindowsApps\MicrosoftEdge.exe
- Image:
  - C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  - C:\Program Files\Microsoft\Edge\Application\msedge.exe
filter_optional_edge_2:
  Image|startswith:
  - C:\Program Files (x86)\Microsoft\EdgeCore\
  - C:\Program Files\Microsoft\EdgeCore\
  Image|endswith:
  - \msedge.exe
  - \msedgewebview2.exe
filter_optional_onedrive:
  Image|endswith: \AppData\Local\Microsoft\OneDrive\OneDrive.exe
filter_optional_null:
  Image: null
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- False positives are expected since this rules is only looking for the DLL load event. This rule is better used in correlation with related activity

## References

- https://posts.specterops.io/requesting-azure-ad-request-tokens-on-azure-ad-joined-machines-for-browser-sso-2b0409caad30

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_azure_microsoft_account_token_provider_dll_load.yml)
