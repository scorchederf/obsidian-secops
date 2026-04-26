---
car_id: "CAR-2014-11-007"
title: "Remote Windows Management Instrumentation (WMI) over RPC"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-11-007/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-007.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-11-007"
  - "Remote Windows Management Instrumentation (WMI) over RPC"
attack_technique_ids:
  - "T1047"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2014-11-007: Remote Windows Management Instrumentation (WMI) over RPC

## Metadata

- CAR ID: CAR-2014-11-007
- Submission Date: 2014/11/19
- Information Domain: Host, Network
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: API RPC, PCAP, Hostflow
- Contributors: MITRE

## Description

As described in ATT&CK, an adversary can use [Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047) (WMI) to view or manipulate objects on a remote host. It can be used to remotely edit configuration, start services, query files, and anything that can be done with a WMI class. When remote WMI requests are over RPC ([[kb/car/analytics/CAR-2014-05-001-rpc_activity|CAR-2014-05-001]]), it connects to a DCOM interface within the RPC group netsvcs. To detect this activity, a sensor is needed at the network level that can decode RPC traffic or on the host where the communication can be detected more natively, such as [Event Tracing for Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968803.aspx). Using wireshark/tshark decoders, the WMI interfaces can be extracted so that WMI activity over RPC can be detected.

Although the description details how to detect remote WMI precisely, a decent estimate has been to look for the string RPCSS within the initial RPC connection on 135/tcp. It returns a superset of this activity, and will trigger on all DCOM-related services running within RPC, which is likely to also be activity that should be detected between hosts.
More about RPCSS at : [rpcss_dcom_interfaces.html](http://www.hsc.fr/ressources/articles/win_net_srv/rpcss_dcom_interfaces.html)

### Output Description

Identifies the connection in which WMI traffic is seen, as well as the process(es) responsible for owning the connection.

## ATT&CK Coverage

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]] (coverage: Moderate; tactics: TA0002)

## Implementations

### pseudocode

To detect WMI over RPC (using DCOM), a sensor needs to exist that has the insight into individual connections and can actually decode and make sense of RPC traffic. Specifically, WMI can be detected by looking at RPC traffic where the target interface matches that of WMI, which is IRemUnknown2.

```pseudocode
flows = search Flow:Message
wmi_flow = filter flows where (dest_port == 135 and proto_info.rpc_interface == "IRemUnknown2")
output wmi_flow
```

## Data Model References

- flow/message/proto_info

## D3FEND Mappings

- [[kb/defend/techniques/D3-RTA-rpc_traffic_analysis|D3-RTA: RPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-11-007/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-007.yaml)
