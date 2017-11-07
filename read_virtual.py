from f5.bigip import ManagementRoot
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# File
f = open('test.txt','w')

# Connect to the BigIP
IP = "x.x.x.x"
mgmt = ManagementRoot(IP, "XXXXX", "XXXXXXXXX")

pools = mgmt.tm.ltm.pools.get_collection()

virt = mgmt.tm.ltm.virtuals.get_collection()
for virtual in virt:
    vip_address = virtual.destination
    vip_name = virtual.name
    print >> f,('VIP: {0} {1}'.format(vip_address, vip_name))
    print ('VIP: {0} {1}'.format(vip_address, vip_name))
    try:
        vip_pool = virtual.pool
        for pool in pools:
             if str("/Common/" + pool.name) == str(vip_pool):
                print ('Pool: {0}'.format(pool.name))
                print >> f,('Pool: {0}'.format(pool.name))
                for NUM, member in enumerate(pool.members_s.get_collection()):
                    address = member.address
                    name = member.name
                    print ('Node: {0} {1}'.format(address, name))
                    print >> f, ('Node: {0} {1}'.format(address, name))
        print >> f, ","
        print ","
    except Exception:
            continue
            
f.close()     
        
