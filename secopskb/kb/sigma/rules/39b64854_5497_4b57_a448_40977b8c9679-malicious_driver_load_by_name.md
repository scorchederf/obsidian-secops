---
sigma_id: "39b64854-5497-4b57-a448-40977b8c9679"
title: "Malicious Driver Load By Name"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_mal_drivers_names.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_mal_drivers_names.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / driver_load"
aliases:
  - "39b64854-5497-4b57-a448-40977b8c9679"
  - "Malicious Driver Load By Name"
attack_technique_ids:
  - "T1543.003"
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Malicious Driver Load By Name

Detects loading of known malicious drivers via the file name of the drivers.

## Metadata

- Rule ID: 39b64854-5497-4b57-a448-40977b8c9679
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-03
- Modified: 2023-12-02
- Source Path: rules/windows/driver_load/driver_load_win_mal_drivers_names.yml

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

## Detection

```yaml
selection:
  ImageLoaded|endswith:
  - \wfshbr64.sys
  - \ktmutil7odm.sys
  - \ktes.sys
  - \a26363e7b02b13f2b8d697abb90cd5c3.sys
  - \kt2.sys
  - \4748696211bd56c2d93c21cab91e82a5.sys
  - \malicious.sys
  - \a236e7d654cd932b7d11cb604629a2d0.sys
  - \spwizimgvt.sys
  - \c94f405c5929cfcccc8ad00b42c95083.sys
  - \fur.sys
  - \wantd.sys
  - \windbg.sys
  - \4118b86e490aed091b1a219dba45f332.sys
  - \gmer64.sys
  - \1fc7aeeff3ab19004d2e53eae8160ab1.sys
  - \poortry2.sys
  - \wintapix.sys
  - \daxin_blank6.sys
  - \6771b13a53b9c7449d4891e427735ea2.sys
  - \blacklotus_driver.sys
  - \air_system10.sys
  - \dkrtk.sys
  - \7.sys
  - \sense5ext.sys
  - \ktgn.sys
  - \ndislan.sys
  - \nlslexicons0024uvn.sys
  - \be6318413160e589080df02bb3ca6e6a.sys
  - \4.sys
  - \wantd_2.sys
  - \e29f6311ae87542b3d693c1f38e4e3ad.sys
  - \daxin_blank3.sys
  - \gftkyj64.sys
  - \daxin_blank2.sys
  - \wantd_4.sys
  - \reddriver.sys
  - \834761775.sys
  - \mlgbbiicaihflrnh.sys
  - \mjj0ge.sys
  - \daxin_blank.sys
  - \daxin_blank5.sys
  - \poortry1.sys
  - \msqpq.sys
  - \mimidrv.sys
  - \e939448b28a4edc81f1f974cebf6e7d2.sys
  - \prokiller64.sys
  - \nodedriver.sys
  - \wantd_3.sys
  - \lctka.sys
  - \kapchelper_x64.sys
  - \daxin_blank4.sys
  - \a9df5964635ef8bd567ae487c3d214c4.sys
  - \wantd_6.sys
  - \ntbios.sys
  - \wantd_5.sys
  - \pciecubed.sys
  - \mimikatz.sys
  - \nqrmq.sys
  - \2.sys
  - \poortry.sys
  - \ntbios_2.sys
  - \fgme.sys
  - \telephonuafy.sys
  - \typelibde.sys
  - \daxin_blank1.sys
  - \ef0e1725aaf0c6c972593f860531a2ea.sys
  - \5a4fe297c7d42539303137b6d75b150d.sys
condition: selection
```

## False Positives

- False positives may occur if one of the vulnerable driver names mentioned above didn't change its name between versions. So always make sure that the driver being loaded is the legitimate one and the non vulnerable version.
- If you experience a lot of FP you could comment the driver name or its exact known legitimate location (when possible)

## References

- https://loldrivers.io/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_mal_drivers_names.yml)
