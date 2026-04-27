---
car_id: "CAR-2019-04-002"
title: "Generic Regsvr32"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2019-04-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-002.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2019-04-002"
  - "Generic Regsvr32"
attack_technique_ids:
  - "T1218"
  - "T1218.010"
platforms:
  - "Windows"
implementation_types:
  - "splunk"
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Regsvr32 can be used to execute arbitrary code in the context of a Windows signed binary, which can be used to bypass application whitelisting. This analytic looks for suspicious usage of the tool. It's not likely that you'll get millions of hits, but it does occur during normal activity so some form of baselining would be necessary for this to be an alerting analytic. Alternatively, it can be used for hunt by looking for new or anomalous DLLs manually.

## ATT&CK Coverage

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218010-regsvr32|T1218.010: Regsvr32]]

## Implementations

### splunk

This just looks for all executions of regsvr32.exe that have a parent of regsvr32.exe but are not regsvr32.exe themselves (which happens). This will have a very high FP rate, but likely not on the order of millions.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_data__ EventCode=1 regsvr32.exe | search ParentImage="*regsvr32.exe" AND Image!="*regsvr32.exe*"
```

### pseudocode

This is a pseudocode version of the above main pattern.

- Data Model: CAR

```pseudocode
processes = search Process:Create
regsvr_processes = filter processes where (
  parent_image_path == "*regsvr32.exe" and image_path != "*regsvr32.exe*"
 )
output regsvr_processes
```

### splunk

This uses the same logic as above, but adds lightweight baselining by ignoring all results that also showed up in the previous 30 days (it runs over 1 day).

- Data Model: Sysmon native

```splunk
index=__your_sysmon_data__ earliest=-d@d latest=now() EventCode=1 regsvr32.exe | search ParentImage="*regsvr32.exe" AND Image!="*regsvr32.exe*" | search NOT [
search index=__your_sysmon_data__ earliest=-60d@d latest=-30d@d EventCode=1 regsvr32.exe | search ParentImage="*regsvr32.exe" AND Image!="*regsvr32.exe*" | dedup CommandLine | fields CommandLine ]
```

### splunk

This looks for child processes that may be spawend by regsvr32, while attempting to eliminate some of the common false positives such as werfault (Windows Error Reporting).

- Data Model: Sysmon native

```splunk
index=__your_sysmon_data__ EventCode=1 (ParentImage="C:\\Windows\\System32\\regsvr32.exe" OR ParentImage="C:\\Windows\\SysWOW64\\regsvr32.exe") AND Image!="C:\\Windows\\System32\\regsvr32.exe" AND Image!="C:\\Windows\\SysWOW64\\regsvr32.exe" AND Image!="C:\\WINDOWS\\System32\\regsvr32.exe" AND Image!="C:\\WINDOWS\\SysWOW64\\regsvr32.exe" AND Image!="C:\\Windows\\SysWOW64\\WerFault.exe" AND Image!="C:\\Windows\\System32\\wevtutil.exe" AND Image!="C:\\Windows\\System32\\WerFault.exe"|stats values(ComputerName) as "Computer Name" values(ParentCommandLine) as "Parent Command Line" count(Image) as ImageCount by Image
```

### pseudocode

This is a pseudocode version of the above Splunk query for spawning child processes.

- Data Model: CAR

```pseudocode
processes = search Process:Create
regsvr_processes = filter processes where (
  (parent_image_path == "C:\Windows\System32\regsvr32.exe" or parent_image_path == "C:\Windows\SysWOW64\regsvr32.exe") and
  image_path != "C:\Windows\System32\regsvr32.exe" and
  image_path != "C:\Windows\SysWOW64\regsvr32.exe" and
  image_path != "C:\Windows\SysWOW64\WerFault.exe" and
  image_path != "C:\Windows\System32\WerFault.exe" and
  image_path != "C:\Windows\System32\wevtutil.exe"
 )
output regsvr_processes
```

### splunk

This looks for unsigned images that may be loaded by regsvr32, while attempting to eliminate false positives stemming from Windows/Program Files binaries.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_data__ EventCode=7 (Image="C:\\Windows\\System32\\regsvr32.exe" OR Image="C:\\Windows\\SysWOW64\\regsvr32.exe") Signed=false ImageLoaded!="C:\\Program Files*" ImageLoaded!="C:\\Windows\\*"|stats values(ComputerName) as "Computer Name" count(ImageLoaded) as ImageLoadedCount by ImageLoaded
```

### pseudocode

This is a pseudocode version of the above Splunk query for loading unsigned images.

- Data Model: CAR

```pseudocode
modules = search Module:Load
unsigned_modules = filter modules where (
  (image_path == "C:\Windows\System32\regsvr32.exe" or image_path == "C:\Windows\SysWOW64\regsvr32.exe") and
  signer == null and
  module_path != "C:\Program Files*" and
  module_path != "C:\Windows\*"
)
output unsigned_modules
```

## Data Model References

- process/create/exe
- process/create/parent_exe
- process/create/command_line
- process/create/image
- process/create/parent_image

## Unit Tests

Any of the [Atomic Red Team tests for regsvr32.exe](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1117/T1117.md) should trigger this.

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2019-04-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-002.yaml)
