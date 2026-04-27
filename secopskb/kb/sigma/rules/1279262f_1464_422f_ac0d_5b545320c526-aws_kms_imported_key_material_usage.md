---
sigma_id: "1279262f-1464-422f-ac0d-5b545320c526"
title: "AWS KMS Imported Key Material Usage"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_kms_import_key_material.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_kms_import_key_material.yml"
build_date: "2026-04-27 19:13:50"
status: "experimental"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "1279262f-1464-422f-ac0d-5b545320c526"
  - "AWS KMS Imported Key Material Usage"
attack_technique_ids:
  - "T1486"
  - "T1608.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the import or deletion of key material in AWS KMS, which can be used as part of ransomware attacks. This activity is uncommon and provides a high certainty signal.

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]
- [[kb/attack/techniques/T1608-stage_capabilities#^t1608003-install-digital-certificate|T1608.003: Install Digital Certificate]]

## Detection

```yaml
selection:
  eventSource: kms.amazonaws.com
  eventName:
  - ImportKeyMaterial
  - DeleteImportedKeyMaterial
condition: selection
```

## False Positives

- Legitimate use cases for imported key material are rare, but may include, Organizations with hybrid cloud architectures that import external key material for compliance requirements.
- Development or testing environments that simulate external key management scenarios. Even in these cases, such activity is typically infrequent and should not add significant noise.

## References

- https://www.chrisfarris.com/post/effective-aws-ransomware/
- https://docs.aws.amazon.com/kms/latest/developerguide/ct-importkeymaterial.html
- https://docs.aws.amazon.com/kms/latest/developerguide/ct-deleteimportedkeymaterial.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_kms_import_key_material.yml)
