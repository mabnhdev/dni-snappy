To build an ONIE NOS installer...

* Create a symbolic link snapcraft.yaml to platform-specific yaml file.
* cp /boot/config-`uname -r` 4.4-config
* snapcraft clean && snapcraft
* When prompted, go to the driver dir and build the driver snap.
* Press any key when OpenSwitch build completes.
* Run tools/make-onie-installer <kernel-snap>
* The *.bin file is the onie installer.
