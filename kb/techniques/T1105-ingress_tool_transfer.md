---
id: T1105
name: Ingress Tool Transfer
created: 2017-05-31 21:31:16.408000+00:00
modified: 2025-10-24 17:49:32.714000+00:00
type: attack-pattern
x_mitre_version: 2.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as [ftp](https://attack.mitre.org/software/S0095). Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570)). 

On Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, [certutil](https://attack.mitre.org/software/S0160), and [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands such as <code>IEX(New-Object Net.WebClient).downloadString()</code> and <code>Invoke-WebRequest</code>. On Linux and macOS systems, a variety of utilities also exist, such as `curl`, `scp`, `sftp`, `tftp`, `rsync`, `finger`, and `wget`.(Citation: t1105_lolbas)  A number of these tools, such as `wget`, `curl`, and `scp`, also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via `certutil -hashfile`).(Citation: Google Cloud Threat Intelligence COSCMICENERGY 2023)

Adversaries may also abuse installers and package managers, such as `yum` or `winget`, to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows `search-ms` protocol handler, to deliver malicious files to victims through remote file searches invoked by [User Execution](https://attack.mitre.org/techniques/T1204) (typically after interacting with [Phishing](https://attack.mitre.org/techniques/T1566) lures).(Citation: T1105: Trellix_search-ms)

Files can also be transferred using various [Web Service](https://attack.mitre.org/techniques/T1102)s as well as native or otherwise present tools on the victim system.(Citation: PTSecurity Cobalt Dec 2016) In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine.(Citation: Dropbox Malware Sync)

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

## Tools

- [[asyncrat|AsyncRAT]]
- [[bitsadmin|BITSAdmin]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[carrotball|CARROTBALL]]
- [[certutil|certutil]]
- [[cmd|cmd]]
- [[cspy_downloader|CSPY Downloader]]
- [[donut|Donut]]
- [[empire|Empire]]
- [[esentutl|esentutl]]
- [[ftp|ftp]]
- [[koadic|Koadic]]
- [[mcmd|MCMD]]
- [[pupy|Pupy]]
- [[quasarrat|QuasarRAT]]
- [[remcos|Remcos]]
- [[remoteutilities|RemoteUtilities]]
- [[shimratreporter|ShimRatReporter]]
- [[silenttrinity|SILENTTRINITY]]
- [[sliver|Sliver]]

