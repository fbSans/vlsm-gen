Usage:
python vlsm.py -a <base_adrress> -m <netmask> -n (<needs>...)
whare:
  <base_address> : ipv4 network address like 192.16.0.0
  <netmask>: mask that delimits the network bits like 24 (stands for /24)
  <needs>: number of hosts to be allocated for subnetworks

Example:
  python vlsm.py -a 192.16.0.0 -m 16 -n 200 100 1000

  output:
+----------+----------------+------+----------------+----------------+----------------+
|num-hosts | subnetwork ip  | mask |  first valid   |   last valid   |   broadcast    |
+----------+----------------+------+----------------+----------------+----------------+
|   1024   |   192.16.0.0   | /22  |   192.16.0.1   |  192.16.3.254  |  192.16.3.255  |
|   256    |   192.16.4.0   | /24  |   192.16.4.1   |  192.16.4.254  |  192.16.4.255  |
|   128    |   192.16.5.0   | /25  |   192.16.5.1   |  192.16.5.126  |  192.16.5.127  |
+----------+----------------+------+----------------+----------------+----------------+
  
