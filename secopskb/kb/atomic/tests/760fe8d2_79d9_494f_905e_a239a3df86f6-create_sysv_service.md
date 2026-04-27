---
atomic_guid: "760fe8d2-79d9-494f-905e-a239a3df86f6"
title: "Create SysV Service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.002"
attack_technique_name: "Create or Modify System Process: SysV/Systemd Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.002/T1543.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "760fe8d2-79d9-494f-905e-a239a3df86f6"
  - "Create SysV Service"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test creates a SysV service unit file and enables it as a service.

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]

## Input Arguments

### rc_service_file

- description: File name of rc service file
- type: string
- default: art-test

### rc_service_path

- description: Path to rc service file
- type: path
- default: /usr/local/etc/rc.d

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo '#\!/bin/sh' > #{rc_service_path}/#{rc_service_file}
echo ' ' >> #{rc_service_path}/#{rc_service_file}
echo '#' >> #{rc_service_path}/#{rc_service_file}
echo '# PROVIDE: art-test' >> #{rc_service_path}/#{rc_service_file}
echo '# REQUIRE: LOGIN' >> #{rc_service_path}/#{rc_service_file}
echo '# KEYWORD: shutdown' >> #{rc_service_path}/#{rc_service_file}
echo ' ' >> #{rc_service_path}/#{rc_service_file}
echo '. /etc/rc.subr' >> #{rc_service_path}/#{rc_service_file}
echo ' ' >> #{rc_service_path}/#{rc_service_file}
echo 'name="art_test"' >> #{rc_service_path}/#{rc_service_file}
echo 'rcvar=art_test_enable' >> #{rc_service_path}/#{rc_service_file}
echo 'load_rc_config ${name}' >> #{rc_service_path}/#{rc_service_file}
echo 'command="/usr/bin/touch"' >> #{rc_service_path}/#{rc_service_file}
echo 'start_cmd="art_test_start"' >> #{rc_service_path}/#{rc_service_file}
echo '' >> #{rc_service_path}/#{rc_service_file}
echo 'art_test_start()' >> #{rc_service_path}/#{rc_service_file}     
echo '{' >> #{rc_service_path}/#{rc_service_file}
echo '  ${command} /tmp/art-test.marker' >> #{rc_service_path}/#{rc_service_file}
echo '}' >> #{rc_service_path}/#{rc_service_file}
echo ' ' >> #{rc_service_path}/#{rc_service_file}     
echo 'run_rc_command "$1"' >> #{rc_service_path}/#{rc_service_file}
chmod +x #{rc_service_path}/#{rc_service_file}
service art-test enable
service art-test start
```

### Cleanup

```bash
sysrc -x art_test_enable
rm -f #{rc_service_path}/#{rc_service_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.002/T1543.002.yaml)
