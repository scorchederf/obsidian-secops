---
sigma_id: "4c6ca276-d4d0-4a8c-9e4c-d69832f8671f"
title: "Antivirus Ransomware Detection"
framework: "sigma"
generated: "true"
source_path: "rules/category/antivirus/av_ransomware.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_ransomware.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "critical"
logsource: "antivirus"
aliases:
  - "4c6ca276-d4d0-4a8c-9e4c-d69832f8671f"
  - "Antivirus Ransomware Detection"
attack_technique_ids:
  - "T1486"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a highly relevant Antivirus alert that reports ransomware.
This event must not be ignored just because the AV has blocked the malware but investigate, how it came there in the first place.

## Logsource

- category: antivirus

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]

## Detection

```yaml
selection:
  Signature|contains:
  - BlackWorm
  - Chaos
  - Cobra
  - ContiCrypt
  - Crypter
  - CRYPTES
  - Cryptor
  - CylanCrypt
  - DelShad
  - Destructor
  - Filecoder
  - GandCrab
  - GrandCrab
  - Haperlock
  - Hiddentear
  - HydraCrypt
  - Krypt
  - Lockbit
  - Locker
  - Mallox
  - Phobos
  - Ransom
  - Ryuk
  - Ryzerlo
  - Stopcrypt
  - Tescrypt
  - TeslaCrypt
  - WannaCry
  - Xorist
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.nextron-systems.com/?s=antivirus
- https://www.virustotal.com/gui/file/43b0f7872900bd234975a0877744554f4f355dc57505517abd1ef611e1ce6916
- https://www.virustotal.com/gui/file/c312c05ddbd227cbb08958876df2b69d0f7c1b09e5689eb9d93c5b357f63eff7
- https://www.virustotal.com/gui/file/20179093c59bca3acc6ce9a4281e8462f577ffd29fd7bf51cf2a70d106062045
- https://www.virustotal.com/gui/file/554db97ea82f17eba516e6a6fdb9dc04b1d25580a1eb8cb755eeb260ad0bd61d
- https://www.virustotal.com/gui/file/69fe77dd558e281621418980040e2af89a2547d377d0f2875502005ce22bc95c
- https://www.virustotal.com/gui/file/6f0f20da34396166df352bf301b3c59ef42b0bc67f52af3d541b0161c47ede05

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/category/antivirus/av_ransomware.yml)
