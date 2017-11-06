import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# File
f = open('text.txt','w')

# Connect to the BigIP
IP = "x.x.x.x"
mgmt = ManagementRoot(IP, "username", "password")

virtuals = mgmt.tm.ltm.virtuals.get_collection()
pools = mgmt.tm.ltm.pools.get_collection()

# RUN
for NUMBER, virtual in enumerate(virtuals):
    vip_address = virtual.destination
    vip_name = virtual.name
     
    print >> f,('VIP: {0} {1}'.format(vip_address, vip_name))

    for NUMBR, pool in enumerate(pools):
        if NUMBR == NUMBER:
            print >> f,('Pool: {0}'.format(pool.name))
            for NUM, member in enumerate(pool.members_s.get_collection()):
                address = member.address
                name = member.name
                print >>f, ('Node: {0} {1}'.format(address, name))
    print >> f, ","           
f.close() 
