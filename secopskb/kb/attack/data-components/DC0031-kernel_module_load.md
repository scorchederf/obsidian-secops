---
mitre_id: "DC0031"
mitre_name: "Kernel Module Load"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--23e4ee78-26f3-4fcf-ba43-ab953962f96c"
mitre_created: "2021-10-20T15:05:19.272Z"
mitre_modified: "2025-10-21T15:14:39.179Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

The process of loading a kernel module into the operating system kernel. Kernel modules are object files that extend the kernel’s functionality, such as adding support for device drivers, new filesystems, or additional system calls. This action can be legitimate (e.g., loading a driver) or malicious (e.g., adding a rootkit). 

*Data Collection Measures:*

- Linux:
    - Auditd: Enable auditing of kernel module loading. Example rule: `-a always,exit -F arch=b64 -S init_module,delete_module`.
    - Syslog: Monitor `/var/log/syslog` or `/var/log/messages` for entries related to kernel module loads.
    - Systemd Journal: Use `journalctl` to query logs for module loading events: `journalctl -k | grep "Loading kernel module"`
- macOS:
    - Unified Logs: Use the `log` command to query kernel module events: `log show --predicate 'eventMessage contains "kextload"' --info`
    - Endpoint Security Framework (ESF): Monitor for `ES_EVENT_TYPE_AUTH_KEXTLOAD` (kernel extension loading events).
- Kernel-Specific Tools:
    - Lsmod: Use `lsmod` to list loaded kernel modules in real-time.
    - Kprobe/eBPF: Use extended Berkeley Packet Filter (eBPF) or Kernel Probes (kprobes) to monitor kernel events, including module loading. Example using eBPF tools like BCC:
`sudo python /path/to/bcc/tools/kprobe -v do_init_module`
- Enable EDR Monitoring:
    - Configure alerts for: Suspicious kernel module loads from non-standard paths (e.g., /tmp). Unexpected or unsigned kernel modules.
    - Review detailed telemetry data provided by the EDR for insight into who initiated the module load, the file path, and whether the module was signed.

## Workspace

- [[workspaces/attack/data-components/DC0031-kernel_module_load-note|Open workspace note]]

![[workspaces/attack/data-components/DC0031-kernel_module_load-note]]

