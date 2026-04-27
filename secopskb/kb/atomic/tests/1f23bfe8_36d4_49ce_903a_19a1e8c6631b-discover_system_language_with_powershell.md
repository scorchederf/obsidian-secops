---
atomic_guid: "1f23bfe8-36d4-49ce-903a-19a1e8c6631b"
title: "Discover System Language with Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "1f23bfe8-36d4-49ce-903a-19a1e8c6631b"
  - "Discover System Language with Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This PowerShell script collects key system settings, such as the UI language, user language preferences, system locale, current culture, UI culture, and time zone, into a hash table. 

It then outputs these settings in a readable key-value format directly to the terminal. The script is simple and efficient for quickly displaying system configuration details.

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$info = @{
  UILanguage     = Get-WinUILanguageOverride
  UserLanguages  = (Get-WinUserLanguageList).LanguageTag -join ', '
  SystemLocale   = Get-WinSystemLocale
  CurrentCulture = [System.Globalization.CultureInfo]::CurrentCulture.Name
  CurrentUICulture = [System.Globalization.CultureInfo]::CurrentUICulture.Name
  TimeZone       = (Get-TimeZone).Id
}
$info.GetEnumerator() | ForEach-Object { "$($_.Name): $($_.Value)" }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
