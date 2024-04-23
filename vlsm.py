#costum utility to solve some exercises at school

import sys

#example of a call: vlsm -a 192.168.10.100 -m 24  -n  2000 4 4 5500

def usage():
    print("vlsm -a <base_addr> -m <base_net_mask> -n (<necessity>  ... )")
    print("    -a        specifies the base network address for creating the subnets.")
    print("    -m        specifies the base net mask")
    print("    -n        a space separated list of the needs for each network")


def break_out(message : str = None):
    if message is not None:
        print(message)
    usage()
    exit(1)

def int_to_str_ip(ip: int) -> str:
    repr=""
    for i in range(4):
        octect = ip & 0xFF
        ip >>= 8
        if(0 < i < 4):
            repr = "." + repr
        repr =  str(octect) + repr 
    return repr


def str_to_int_ip(ip: str) -> int:
    res=0
    for (i, v) in enumerate(ip.split('.')):
        res += int(v) * (256 ** (3 - i)) 
    return res

class subnet_entry:
    def __init__(self, ip: int, mask: int):
        self.ip = ip
        self.mask = mask

    def first_host() -> int :
        pass

    def last_host() -> int:
        pass

    def gateway() -> int:
        pass



def get_ipv4(val: str) -> int:
    ls = val.split('.')
    result = len(ls) == 4
    for v in ls:
        result = result or str.isnumeric(v) and 0 <= int(v) < 256
    if result:
        return str_to_int_ip(val)
    break_out(f"invalid ip: {val}")


def get_valid_num(val: str, message : str = None, min : int = 0, max : int = 0xFFFFFFFF):
    if str.isnumeric(val) and min <= int(val) <= max:
        return int(val)
    break_out(message)


def shift_list(args):
    return args[0], args[1:]

def parse_args(argv : list[str]) -> tuple[int, int, list[int]]:
    #values to return
    ip   : int = 0
    mask : int = 0
    needs: list[int] = []

    #flags (to verify if command is complete)
    got_ip = False
    got_mask = False
    got_needs = False

    #parse arguments
    while len(argv) > 0:
        if len(argv) < 2:
            break_out("not enough arguments")
        option, argv = shift_list(argv)
        match option:
            case "-a":
                if got_ip: break_out()
                val, argv = shift_list(argv)
                ip = get_ipv4(val)
                got_ip = True
            case "-m":
                val, argv = shift_list(argv)
                mask = get_valid_num(val, "Invalid mask, mask mast be between 0 and 32 ", 0, 32)
                got_mask = True
            case "-n":
                while len(argv) > 0 and (argv[0] != '-a' or argv[0] != 'm'):
                    val, argv = shift_list(argv)
                    needs.append(get_valid_num(val, "necessity must be positive"))
                got_needs = True
            case _ :
                break_out(f"unknown option {option}")

    #incomplete command specification            
    if(not(got_ip and got_mask and got_needs)):
         break_out()
  
    #to fill the table the needs must be in descending order
    needs.sort(reverse=True) 
    #valid arguments (from here is only happy path)  
    return (ip, mask, needs)

def build_table(base_ip: int, mask : int, necessities : list[int]) -> dict[subnet_entry]:
    pass

def print_table(entries: dict[subnet_entry]):
    pass


if __name__ == '__main__':
    program = sys.argv[0]
    argv = sys.argv[1:]
    entries = parse_args(argv)
    print(entries)
    exit(0)