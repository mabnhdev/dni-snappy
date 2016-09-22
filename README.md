To build an ONIE NOS installer...

* Create a symbolic link snapcraft.yaml to platform-specific yaml file.
* cp /boot/config-`uname -r` 4.4-config
* snapcraft login
 * Use your Ubuntu One credentials. 
* snapcraft clean && snapcraft
* When prompted, go to the driver dir and build the driver snap.
* Press any key when the driver snap build completes.
* Run tools/make-onie-installer <kernel-snap>
* The *.bin file is the onie installer.

Known Issues:
 * During Boot
  *  [FAILED] Failed to start Run snappy firstboot setup.
  *  [  OK  ] Started Update resolvconf for networkd DNS.
    * May take up to 60 seconds to complete.
  * [   89.265323] cloud-init[1678]: 2016-09-22 11:55:45,265 - url_helper.py[WARNING]: Callinng 'http://169.254.169.254/2009-04-04/meta-data/instance-id' failed [50/120s]: request error [HTTPConnectionPool(host='169.254.169.254', port=80): Max retries exceeded with url: /2009-04-04/meta-data/instance-id (Caused by ConnectTimeoutError(<requests.packages.urllib3.connection.HTTPConnection object at 0x7f6b93717a58>, 'Connection to 169.254.169.254 timed out. (connect timeout=50.0)'))]
    * May take up to 80 seconds to complete.
  * [  159.024879] cloud-init[1678]: 2016-09-22 11:56:55,342 - url_helper.py[WARNING]: Calling 'http://10.50.64.1/latest/meta-data/instance-id' failed [0/120s]: request error [HTTPConnectionPool(host='10.50.64.1', port=80): Max retries exceeded with url: /latest/meta-data/instance-id (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f6b93717470>: Failed to establish a new connection: [Errno 111] Connection refused',))]
    * May take up to 120 seconds to complete.
 * During First Boot
  * Late in the first boot, you may not see a promt 'Press ENTER to continue'.  The boot will seem to freeze up.  Press ENTER to continue the first boot.
  * You MUST have a console connection.
  * You SHOULD have a network connection with DHCP serving up an IP address, Gateway info, and DNS info.

First Boot Setup:
 * You MUST have a Ubuntu One account with an uploaded SSH key.
  * Go to https://login.ubuntu.com/ to set up an account if you don't already have one.
  * Go to SSH Keys tab to import your SSH key.
 * After you hit ENTER, you'll be presented with a Network Configuration Menu.
 * Press ENTER on intro screen to begin.
 * On the Interfaces screen, press TAB, then ENTER to take the default settings.
  * If you don't have DHCP, you'll have to setup the network interface manually.
 * On the Profile Setup Screen...
  * Enter the e-mail address associated with your Ubuntu One account, then press TAB, then ENTER.
 * On the Configuration Complete Screen...
  * Note the SSH command to log into the box.
  * Press enter to complete the setup.
 * On a remote system...
  * Use the SSH command line from above to log into the new switch.
  * Create a new user.
   * sudo adduser --extrausers newuser
  * Add the user to sudoers; set timeout to infinite.
   * echo "extreme ALL=(ALL,ALL) ALL" | sudo tee -a /etc/sudoers.d/90-sudo-users
   * echo "Defaults timestamp_timeout=-1" | sudo tee -a /etc/sudoers.d/90-sudo-users
  * sudo reboot
 
