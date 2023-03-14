When installing Home Assistant OS (haos) in a VM on proxmox I've encountered a problem. Proxmox wants a boot image (e.g. iso file) to boot the VM from, but home assistant does not offer any of this.

To fix it, you simple have tu run this command:

`bash -c "$(wget -qLO - https://github.com/tteck/Proxmox/raw/main/vm/haos-vm-v5.sh)"`

This creates a VM with 4 GB RAM and 32GB storage. This configuration is not changeable and of course requires you to have the corresponding Hardware in your system.
