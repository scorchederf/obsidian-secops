---
id: T1016
name: System Network Configuration Discovery
created: 2017-05-31 21:30:27.342000+00:00
modified: 2025-10-24 17:48:56.618000+00:00
type: attack-pattern
x_mitre_version: 1.7
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include [Arp](https://attack.mitre.org/software/S0099), [ipconfig](https://attack.mitre.org/software/S0100)/[ifconfig](https://attack.mitre.org/software/S0101), [nbtstat](https://attack.mitre.org/software/S0102), and [route](https://attack.mitre.org/software/S0103).

Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. <code>show ip route</code>, <code>show ip interface</code>).(Citation: US-CERT-TA18-106A)(Citation: Mandiant APT41 Global Intrusion ) On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the command `esxcli network nic list` will retrieve the MAC address, while `esxcli network ip interface ipv4 get` will retrieve the local IPv4 address.(Citation: Trellix Rnasomhouse 2024)

Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016) during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 

## Subtechniques

### T1016.001: Internet Connection Discovery

^t1016001-internet-connection-discovery

**Parent Technique**
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using [Ping](https://attack.mitre.org/software/S0097), <code>tracert</code>, and GET requests to websites, or performing initial speed testing to confirm bandwidth.

Adversaries may use the results and responses from these requests to determine if the system is capable of communicating with their C2 servers before attempting to connect to them. The results may also be used to identify routes, redirectors, and proxy servers.

### T1016.002: Wi-Fi Discovery

^t1016002-wi-fi-discovery

**Parent Technique**
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromised systems. Adversaries may use Wi-Fi information as part of [Account Discovery](https://attack.mitre.org/techniques/T1087), [Remote System Discovery](https://attack.mitre.org/techniques/T1018), and other discovery or [Credential Access](https://attack.mitre.org/tactics/TA0006) activity to support both ongoing and future campaigns.

Adversaries may collect various types of information about Wi-Fi networks from hosts. For example, on Windows names and passwords of all Wi-Fi networks a device has previously connected to may be available through `netsh wlan show profiles` to enumerate Wi-Fi names and then `netsh wlan show profile “Wi-Fi name” key=clear` to show a Wi-Fi network’s corresponding password.(Citation: BleepingComputer Agent Tesla steal wifi passwords)(Citation: Malware Bytes New AgentTesla variant steals WiFi credentials)(Citation: Check Point APT35 CharmPower January 2022) Additionally, names and other details of locally reachable Wi-Fi networks can be discovered using calls to `wlanAPI.dll` [Native API](https://attack.mitre.org/techniques/T1106) functions.(Citation: Binary Defense Emotes Wi-Fi Spreader)

On Linux, names and passwords of all Wi-Fi-networks a device has previously connected to may be available in files under ` /etc/NetworkManager/system-connections/`.(Citation: Wi-Fi Password of All Connected Networks in Windows/Linux) On macOS, the password of a known Wi-Fi may be identified with ` security find-generic-password -wa wifiname` (requires admin username/password).(Citation: Find Wi-Fi Password on Mac)


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

