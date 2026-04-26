---
sigma_id: "6b98b92b-4f00-4f62-b4fe-4d1920215771"
title: "Potential DLL Sideloading Of Non-Existent DLLs From System Folders"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_non_existent_dlls.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_non_existent_dlls.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "6b98b92b-4f00-4f62-b4fe-4d1920215771"
  - "Potential DLL Sideloading Of Non-Existent DLLs From System Folders"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of Non-Existent DLLs From System Folders

Detects loading of specific system DLL files that are usually not present on the system (or at least not in system directories) but may be loaded by legitimate processes, potentially indicating phantom DLL hijacking attempts.
Phantom DLL hijacking involves placing malicious DLLs with names of non-existent system binaries in locations where legitimate applications may search for them, leading to execution of the malicious DLLs.

## Metadata

- Rule ID: 6b98b92b-4f00-4f62-b4fe-4d1920215771
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), SBousseaden
- Date: 2022-12-09
- Modified: 2026-01-24
- Source Path: rules/windows/image_load/image_load_side_load_non_existent_dlls.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith:
  - :\Windows\System32\axeonoffhelper.dll
  - :\Windows\System32\cdpsgshims.dll
  - :\Windows\System32\oci.dll
  - :\Windows\System32\offdmpsvc.dll
  - :\Windows\System32\shellchromeapi.dll
  - :\Windows\System32\TSMSISrv.dll
  - :\Windows\System32\TSVIPSrv.dll
  - :\Windows\System32\wbem\wbemcomn.dll
  - :\Windows\System32\WLBSCTRL.dll
  - :\Windows\System32\wow64log.dll
  - :\Windows\System32\WptsExtensions.dll
filter_main_ms_signed:
  Signed: 'true'
  SignatureStatus: Valid
  Signature: Microsoft Windows
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- http://remoteawesomethoughts.blogspot.com/2019/05/windows-10-task-schedulerservice.html
- https://clement.notin.org/blog/2020/09/12/CVE-2020-7315-McAfee-Agent-DLL-injection/
- https://decoded.avast.io/martinchlumecky/png-steganography/
- https://github.com/Wh04m1001/SysmonEoP
- https://itm4n.github.io/cdpsvc-dll-hijacking/
- https://posts.specterops.io/lateral-movement-scm-and-dll-hijacking-primer-d2f61e8ab992
- https://securelist.com/passiveneuron-campaign-with-apt-implants-and-cobalt-strike/117745/
- https://www.crowdstrike.com/en-us/blog/4-ways-adversaries-hijack-dlls/
- https://www.hexacorn.com/blog/2013/12/08/beyond-good-ol-run-key-part-5/
- https://www.hexacorn.com/blog/2025/06/14/wermgr-exe-boot-offdmpsvc-dll-lolbin/
- https://www.hexacorn.com/blog/2025/06/14/wpr-exe-boottrace-phantom-dll-axeonoffhelper-dll-lolbin/
- https://x.com/0gtweet/status/1564131230941122561

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_non_existent_dlls.yml)
