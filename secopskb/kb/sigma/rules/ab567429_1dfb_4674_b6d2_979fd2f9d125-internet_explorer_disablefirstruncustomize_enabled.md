---
sigma_id: "ab567429-1dfb-4674-b6d2-979fd2f9d125"
title: "Internet Explorer DisableFirstRunCustomize Enabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_internet_explorer_disable_first_run_customize.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_internet_explorer_disable_first_run_customize.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "ab567429-1dfb-4674-b6d2-979fd2f9d125"
  - "Internet Explorer DisableFirstRunCustomize Enabled"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Internet Explorer DisableFirstRunCustomize Enabled

Detects changes to the Internet Explorer "DisableFirstRunCustomize" value, which prevents Internet Explorer from running the first run wizard the first time a user starts the browser after installing Internet Explorer or Windows.

## Metadata

- Rule ID: ab567429-1dfb-4674-b6d2-979fd2f9d125
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-16
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_set/registry_set_internet_explorer_disable_first_run_customize.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|endswith: \Microsoft\Internet Explorer\Main\DisableFirstRunCustomize
  Details:
  - DWORD (0x00000001)
  - DWORD (0x00000002)
filter_main_generic:
  Image:
  - C:\Windows\explorer.exe
  - C:\Windows\System32\ie4uinit.exe
filter_optional_avira:
  Image|contains|all:
  - \Temp\
  - \.cr\avira_
  Details|contains: DWORD (0x00000001)
filter_optional_foxit:
  Image:
  - C:\Program Files (x86)\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe
  - C:\Program Files\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe
  Details|contains: DWORD (0x00000001)
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- As this is controlled by group policy as well as user settings. Some false positives may occur.

## References

- https://www.ncsc.gov.uk/static-assets/documents/malware-analysis-reports/devil-bait/NCSC-MAR-Devil-Bait.pdf
- https://unit42.paloaltonetworks.com/operation-ke3chang-resurfaces-with-new-tidepool-malware/
- https://admx.help/?Category=InternetExplorer&Policy=Microsoft.Policies.InternetExplorer::NoFirstRunCustomise

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_internet_explorer_disable_first_run_customize.yml)
