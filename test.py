from pyp2p.net import *
from pyp2p.unl import UNL
from pyp2p.dht_msg import DHT
import time


node1_dht = DHT()
node1_direct = Net(passive_bind="192.168.0.45", passive_port=44444, interface="eth0:2", net_type="direct", dht_node=node1_dht, debug=1)
node1_direct.start()

#Start Bob's direct server.
node2_dht = DHT()
node2_direct = Net(passive_bind="192.168.0.44", passive_port=44445, interface="eth0:1", net_type="direct", node_type="active", dht_node=node2_dht, debug=1)
node2_direct.start()

#Callbacks.
def success(con):
    print("Ishan successfully connected to Bob.")
    con.send_line("Sup Bob.")

def failure(con):
    print("Adam failed to connec to Bob\a")

events = {
    "success": success,
    "failure": failure
}

node1_direct.unl.connect(node2_direct.unl.construct(), events)

#Event loop.
while 1:
#Bob get reply.
    for con in node2_direct:
        for reply in con:
            print(reply)

#Alice accept con.
for con in node1_direct:
    x = 1

time.sleep(0.5)