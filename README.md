# ** VLSM table generator**
## **Usage:**
``` python vlsm.py -a <base_adrress> -m <netmask> -n (<needs>...). ```
## Where:
  * **base_address:**  ipv4 network address like 192.16.0.0
  * **netmask:** mask that delimits the network bits like 24 (stands for /24)
  * **needs:** number of hosts to be allocated for subnetworks

## **Example**:
  ```python vlsm.py -a 192.16.0.0 -m 16 -n 200 100 1000```


**Output**:
![image](https://github.com/fbSans/unitools/assets/95938238/098a3108-b43a-4d10-bf09-675f88371de2)
