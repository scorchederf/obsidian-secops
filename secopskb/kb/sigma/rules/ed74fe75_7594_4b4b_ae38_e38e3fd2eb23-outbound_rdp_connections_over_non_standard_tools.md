---
sigma_id: "ed74fe75-7594-4b4b-ae38-e38e3fd2eb23"
title: "Outbound RDP Connections Over Non-Standard Tools"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_rdp_outbound_over_non_standard_tools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rdp_outbound_over_non_standard_tools.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "ed74fe75-7594-4b4b-ae38-e38e3fd2eb23"
  - "Outbound RDP Connections Over Non-Standard Tools"
attack_technique_ids:
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Non-Standard tools initiating a connection over port 3389 indicating possible lateral movement.
An initial baseline is required before using this utility to exclude third party RDP tooling that you might use.

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Detection

```yaml
selection:
  DestinationPort: 3389
  Initiated: 'true'
filter_main_mstsc:
  Image:
  - C:\Windows\System32\mstsc.exe
  - C:\Windows\SysWOW64\mstsc.exe
filter_optional_dns:
  Image: C:\Windows\System32\dns.exe
  SourcePort: 53
  Protocol: udp
filter_optional_avast:
  Image|endswith:
  - \Avast Software\Avast\AvastSvc.exe
  - \Avast\AvastSvc.exe
filter_optional_sysinternals_rdcman:
  Image|endswith: \RDCMan.exe
filter_optional_chrome:
  Image: C:\Program Files\Google\Chrome\Application\chrome.exe
filter_optional_third_party:
  Image|endswith:
  - \FSAssessment.exe
  - \FSDiscovery.exe
  - \MobaRTE.exe
  - \mRemote.exe
  - \mRemoteNG.exe
  - \Passwordstate.exe
  - \RemoteDesktopManager.exe
  - \RemoteDesktopManager64.exe
  - \RemoteDesktopManagerFree.exe
  - \RSSensor.exe
  - \RTS2App.exe
  - \RTSApp.exe
  - \spiceworks-finder.exe
  - \Terminals.exe
  - \ws_TunnelService.exe
filter_optional_thor:
  Image|endswith:
  - \thor.exe
  - \thor64.exe
filter_optional_splunk:
  Image|startswith: C:\Program Files\SplunkUniversalForwarder\bin\
filter_optional_sentinel_one:
  Image|endswith: \Ranger\SentinelRanger.exe
filter_optional_firefox:
  Image: C:\Program Files\Mozilla Firefox\firefox.exe
filter_optional_tsplus:
  Image:
  - C:\Program Files\TSplus\Java\bin\HTML5service.exe
  - C:\Program Files (x86)\TSplus\Java\bin\HTML5service.exe
filter_optional_null:
  Image: null
filter_optional_empty:
  Image: ''
filter_optional_unknown:
  Image: <unknown process>
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Third party RDP tools

## References

- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0708

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_rdp_outbound_over_non_standard_tools.yml)
