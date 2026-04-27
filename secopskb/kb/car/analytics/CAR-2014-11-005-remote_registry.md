---
car_id: "CAR-2014-11-005"
title: "Remote Registry"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-11-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-005.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2014-11-005"
  - "Remote Registry"
attack_technique_ids:
  - "T1112"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary can remotely [manipulate the registry](https://attack.mitre.org/techniques/T1112) of another machine if the RemoteRegistry service is enabled and valid credentials are obtained. While the registry is remotely accessed, it can be used to prepare a [Lateral Movement](https://attack.mitre.org/tactics/TA0008) technique, [discover](https://attack.mitre.org/tactics/TA0007) the configuration of a host, achieve [Persistence](https://attack.mitre.org/tactics/TA0003), or anything that aids an adversary in achieving the mission. Like most ATT&CK techniques, this behavior can be used legitimately, and the reliability of an analytic depends on the proper identification of the pre-existing legitimate behaviors. Although this behavior is disabled in many Windows configurations, it is possible to [remotely enable](https://attack.mitre.org/techniques/T1569/002) the RemoteRegistry service, which can be detected with [[kb/car/analytics/CAR-2014-03-005-remotely_launched_executables_via_services|CAR-2014-03-005]].

Remote access to the registry can be achieved via

-   Windows API function [RegConnectRegistry](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724840.aspx)
-   command line via `reg.exe`
-   graphically via `regedit.exe`

All of these behaviors call into the Windows API, which uses the NamedPipe `WINREG` over SMB to handle the protocol information. This network can be decoded with wireshark or a similar sensor, and can also be detected by hooking the API function.

## ATT&CK Coverage

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]] (coverage: Moderate; tactics: TA0005)

## Implementations

### pseudocode

```pseudocode
flows = search Flow:Message
winreg = filter flows where (dest_port == 445 and proto_info.pipe == "WINREG")
winreg_modify = filter flows where (proto_info.function == "Create*" or proto_info.function == "SetValue*")

output winreg_modify
```

## Data Model References

- flow/message/dest_port
- flow/message/proto_info

## D3FEND Mappings

- [[kb/defend/techniques/D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-11-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-005.yaml)
