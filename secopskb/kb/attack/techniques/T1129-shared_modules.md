---
mitre_id: "T1129"
mitre_name: "Shared Modules"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0a5231ec-41af-4a35-83d0-6bdf11f28c65"
mitre_created: "2017-05-31T21:31:40.542Z"
mitre_modified: "2025-10-24T17:48:22.302Z"
mitre_version: "2.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1129/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions (i.e., [[T1106-native_api|T1106: Native API]]).

Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network communications or execution of specific actions on objective.

The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides in `dlfcn.h` in functions such as `dlopen` and `dlsym`. Although macOS can execute `.so` files, common practice uses `.dylib` files.(Citation: Apple Dev Dynamic Libraries)(Citation: Linux Shared Libraries)(Citation: RotaJakiro 2021 netlab360 analysis)(Citation: Unit42 OceanLotus 2017)

The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in `NTDLL.dll` and is part of the Windows [[T1106-native_api|T1106: Native API]] which is called from functions like `LoadLibrary` at run time.(Citation: Microsoft DLL)

## Workspace

- [[workspaces/attack/techniques/T1129-shared_modules-note|Open workspace note]]

![[workspaces/attack/techniques/T1129-shared_modules-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/7f843046_abf2_443f_b880_07a83cf968ec-esxi_install_a_custom_vib_on_an_esxi_host|ESXi - Install a custom VIB on an ESXi host (command_prompt; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1038-execution_prevention|M1038: Execution Prevention]]

## Platforms

- Linux
- macOS
- Windows

