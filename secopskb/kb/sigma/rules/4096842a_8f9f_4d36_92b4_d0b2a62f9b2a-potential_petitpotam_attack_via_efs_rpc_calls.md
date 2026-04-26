---
sigma_id: "4096842a-8f9f-4d36-92b4-d0b2a62f9b2a"
title: "Potential PetitPotam Attack Via EFS RPC Calls"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dce_rpc_potential_petit_potam_efs_rpc_call.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_potential_petit_potam_efs_rpc_call.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "zeek / dce_rpc"
aliases:
  - "4096842a-8f9f-4d36-92b4-d0b2a62f9b2a"
  - "Potential PetitPotam Attack Via EFS RPC Calls"
attack_technique_ids:
  - "T1557.001"
  - "T1187"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential PetitPotam Attack Via EFS RPC Calls

Detects usage of the windows RPC library Encrypting File System Remote Protocol (MS-EFSRPC). Variations of this RPC are used within the attack refereed to as PetitPotam.
The usage of this RPC function should be rare if ever used at all.
Thus usage of this function is uncommon enough that any usage of this RPC function should warrant further investigation to determine if it is legitimate.
 View surrounding logs (within a few minutes before and after) from the Source IP to. Logs from from the Source IP would include dce_rpc, smb_mapping, smb_files, rdp, ntlm, kerberos, etc..'

## Metadata

- Rule ID: 4096842a-8f9f-4d36-92b4-d0b2a62f9b2a
- Status: test
- Level: medium
- Author: @neu5ron, @Antonlovesdnb, Mike Remen
- Date: 2021-08-17
- Modified: 2022-11-28
- Source Path: rules/network/zeek/zeek_dce_rpc_potential_petit_potam_efs_rpc_call.yml

## Logsource

- product: zeek
- service: dce_rpc

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557.001]]
- [[kb/attack/techniques/T1187-forced_authentication|T1187]]

## Detection

```yaml
selection:
  operation|startswith: efs
condition: selection
```

## False Positives

- Uncommon but legitimate windows administrator or software tasks that make use of the Encrypting File System RPC Calls. Verify if this is common activity (see description).

## References

- https://github.com/topotam/PetitPotam/blob/d83ac8f2dd34654628c17490f99106eb128e7d1e/PetitPotam/PetitPotam.cpp
- https://msrc.microsoft.com/update-guide/vulnerability/ADV210003
- https://vx-underground.org/archive/Symantec/windows-vista-network-attack-07-en.pdf
- https://threatpost.com/microsoft-petitpotam-poc/168163/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_potential_petit_potam_efs_rpc_call.yml)
