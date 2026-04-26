---
sigma_id: "f41b0311-44f9-44f0-816d-dd45e39d4bc8"
title: "Access To Crypto Currency Wallets By Uncommon Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_access/file_access_win_susp_crypto_currency_wallets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_crypto_currency_wallets.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / file_access"
aliases:
  - "f41b0311-44f9-44f0-816d-dd45e39d4bc8"
  - "Access To Crypto Currency Wallets By Uncommon Applications"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Access To Crypto Currency Wallets By Uncommon Applications

Detects file access requests to crypto currency files by uncommon processes.
Could indicate potential attempt of crypto currency wallet stealing.

## Metadata

- Rule ID: f41b0311-44f9-44f0-816d-dd45e39d4bc8
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2024-07-29
- Source Path: rules/windows/file/file_access/file_access_win_susp_crypto_currency_wallets.yml

## Logsource

- category: file_access
- definition: Requirements: Microsoft-Windows-Kernel-File ETW provider
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection:
- FileName|contains:
  - \AppData\Roaming\Ethereum\keystore\
  - \AppData\Roaming\EthereumClassic\keystore\
  - \AppData\Roaming\monero\wallets\
- FileName|endswith:
  - \AppData\Roaming\Bitcoin\wallet.dat
  - \AppData\Roaming\BitcoinABC\wallet.dat
  - \AppData\Roaming\BitcoinSV\wallet.dat
  - \AppData\Roaming\DashCore\wallet.dat
  - \AppData\Roaming\DogeCoin\wallet.dat
  - \AppData\Roaming\Litecoin\wallet.dat
  - \AppData\Roaming\Ripple\wallet.dat
  - \AppData\Roaming\Zcash\wallet.dat
filter_main_system:
  Image: System
filter_main_generic:
  Image|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\system32\
  - C:\Windows\SysWOW64\
filter_optional_defender:
  Image|startswith: C:\ProgramData\Microsoft\Windows Defender\
  Image|endswith:
  - \MpCopyAccelerator.exe
  - \MsMpEng.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Antivirus, Anti-Spyware, Anti-Malware Software
- Backup software
- Legitimate software installed on partitions other than "C:\"
- Searching software such as "everything.exe"

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_crypto_currency_wallets.yml)
