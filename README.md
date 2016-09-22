To build an ONIE NOS installer...

* Create a symbolic link snapcraft.yaml to platform-specific yaml file.
* cp /boot/config-`uname -r` 4.4-config
* snapcraft clean && snapcraft
* When prompted, go to the driver dir and build the driver snap.
* Press any key when OpenSwitch build completes.
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
  * Late in the first boot, you may not see a promt 'Press ENTER to continue'.  The boot will seem to freeze up.  Press ENTER to continue the first boot.
