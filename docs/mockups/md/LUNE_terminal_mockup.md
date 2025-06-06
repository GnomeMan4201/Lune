# LUNE terminal mockup

```shell
kali@lune-ops:~/LUNE$ ./lune-shell.sh

╔════════════════════════════════════════════════════════════╗
║           LUNE v1.0 – Shell Deception Interface            ║
╠════════════════════════════════════════════════════════════╣
║ Real Shell      : /bin/bash                                ║
║ Decoy Shells    : 3 spawned                                ║
║ Active Decoys   : fake_cron.sh, ps_inject.py, sftp_drain   ║
║ Noise Level     : HIGH                                     ║
║ Surveillance    : ENABLED                                  ║
╚════════════════════════════════════════════════════════════╝

 [1] Deploy Decoy Shell
 [2] Inject Noise Artifacts
 [3] Activate File System Fog
 [4] Begin Exfil from Real Shell
 [5] Monitor Target Confusion
 [6] Clear Trail / Wipe Session
 [Q] Exit

> 1

[+] Deploying decoy shell: /tmp/.bash_history_mimic
[+] Launching with fake admin commands...
[+] Watching for target interaction...

> 2

[+] Injecting noise artifacts:
    - /var/log/daemon-fail.log
    - /etc/fake_passwd
    - /home/admin/.ssh/phantom_key.pub
[+] Artifacts planted

> 5

╔══════════════════════════════════════════════════════╗
║     SURVEILLANCE CONSOLE – TARGET CONFUSION MAP     ║
╠══════════════════════════════════════════════════════╣
║ [✓] Target viewed decoy shell: /tmp/.bash_history_mimic      ║
║ [✓] Target listed fake /etc/passwd copy                      ║
║ [✓] Attempted to SCP phantom_key.pub                         ║
║ [!] Real shell untouched for 6 min                           ║
╚══════════════════════════════════════════════════════╝

Operator Status: Hidden  
Exfil Tunnel: Active (/tmp/.tunnel)

```
