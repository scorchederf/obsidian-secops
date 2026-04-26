---
sigma_id: "10cb6535-b31d-4512-9962-513dcbc42cc1"
title: "PUA - System Informer Driver Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_pua_system_informer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_pua_system_informer.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / driver_load"
aliases:
  - "10cb6535-b31d-4512-9962-513dcbc42cc1"
  - "PUA - System Informer Driver Load"
attack_technique_ids:
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - System Informer Driver Load

Detects driver load of the System Informer tool

## Metadata

- Rule ID: 10cb6535-b31d-4512-9962-513dcbc42cc1
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2023-05-08
- Modified: 2024-11-23
- Source Path: rules/windows/driver_load/driver_load_win_pua_system_informer.yml

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]]

## Detection

```yaml
selection:
- ImageLoaded|endswith: \SystemInformer.sys
- Hashes|contains:
  - SHA256=8B9AD98944AC9886EA4CB07700E71B78BE4A2740934BB7E46CA3B56A7C59AD24
  - SHA256=A41348BEC147CA4D9EA2869817527EB5CEA2E20202AF599D2B30625433BCF454
  - SHA256=38EE0A88AF8535A11EFE8D8DA9C6812AA07067B75A64D99705A742589BDD846D
  - SHA256=A773891ACF203A7EB0C0D30942FB1347648F1CD918AE2BFD9A4857B4DCF5081B
  - SHA256=4C3B81AC88A987BBDF7D41FA0AECC2CEDF5B9BD2F45E7A21F376D05345FC211D
  - SHA256=3241BC14BEC51CE6A691B9A3562E5C1D52E9D057D27A3D67FD0B245C350B6D34
  - SHA256=047C42E9BBA28366868847C7DAFC1E043FB038C796422D37220493517D68EE89
  - SHA256=18931DC81E95D0020466FA091E16869DBE824E543A4C2C8FE644FA71A0F44FEB
  - SHA256=B4C2EF76C204273132FDE38F0DED641C2C5EE767652E64E4C4071A4A973B6C1B
  - SHA256=640954AFC268565F7DAA6E6F81A8EE05311E33E34332B501A3C3FE5B22ADEA97
  - SHA256=251BE949F662C838718F8AA0A5F8211FB90346D02BD63FF91E6B224E0E01B656
  - SHA256=E2606F272F7BA054DF16BE464FDA57211EF0D14A0D959F9C8DCB0575DF1186E4
  - SHA256=3A9E1D17BEEB514F1B9B3BACAEE7420285DE5CBDCE89C5319A992C6CBD1DE138
condition: selection
```

## False Positives

- System Informer is regularly used legitimately by system administrators or developers. Apply additional filters accordingly

## References

- https://systeminformer.sourceforge.io/
- https://github.com/winsiderss/systeminformer

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_pua_system_informer.yml)
