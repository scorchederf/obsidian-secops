---
mitre_id: "T1680"
mitre_name: "Local Storage Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f2514ae4-4e9b-4f26-a5ba-c4ae85fe93c3"
mitre_created: "2025-09-25T21:09:38.677Z"
mitre_modified: "2025-10-22T02:09:54.940Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1680/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform [Lateral Movement](https://attack.mitre.org/tactics/TA0109), or as a precursor to [[T1006-direct_volume_access|T1006: Direct Volume Access]]. 

On ESXi systems, adversaries may use [[T1059-command_and_scripting_interpreter#^t1059012-hypervisor-cli|T1059.012: Hypervisor CLI]] commands such as `esxcli` to list storage connected to the host as well as `.vmdk` files.(Citation: TrendMicro)(Citation: TrendMicro ESXI Ransomware)

On Windows systems, adversaries can use `wmic logicaldisk get` to find information about local network drives. They can also use `Get-PSDrive` in PowerShell to retrieve drives and may additionally use Windows API functions such as `GetDriveType`.(Citation: Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024)(Citation: Volexity)

Linux has commands such as `parted`, `lsblk`, `fdisk`, `lshw`, and `df` that can list information about disk partitions such as size, type, file system types, and free space. The command `diskutil` on MacOS can be used to list disks while `system_profiler SPStorageDataType` can additionally show information such as a volume’s mount path, file system, and the type of drive in the system. 

Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as `describe volume` in AWS, `gcloud compute disks list` in GCP, and `az disk list` in Azure.(Citation: AWS docs describe volumes)(Citation: GCP gcloud compute disks list)(Citation: azure az disk)

## Workspace

- [[workspaces/attack/techniques/T1680-local_storage_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1680-local_storage_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools
- [[asyncrat|AsyncRAT (S1087)]]
- [[crackmapexec|CrackMapExec (S0488)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Windows

