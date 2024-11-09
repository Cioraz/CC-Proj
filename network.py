from mininet.node import Controller, OVSKernelAP
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet_wifi.net import Mininet_wifi
from mininet_wifi.cli import CLI
from mininet_wifi.link import wmediumd, mesh
from mininet_wifi.wmediumdConnector import interference

def topology():
    net = Mininet_wifi(controller=Controller, link=TCLink, accessPoint=OVSKernelAP, link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid='RSU1', mode='g', channel='5', position='50,50,0')
    ap2 = net.addAccessPoint('ap2', ssid='RSU2', mode='g', channel='5', position='150,50,0')
    c1 = net.addController('c1', controller=Controller, port=6633)

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Adding cars\n")
    cars = []
    num_cars = 5
    for i in range(num_cars):
        car = net.addStation('car%s' % (i+1), ip='10.0.0.%s/24' % (i+1), position='%s,30,0' % (50 + i*20))
        cars.append(car)

    info("*** Creating links\n")
    net.addLink(ap1, c1)
    net.addLink(ap2, c1)

    for car in cars:
        net.addLink(car, ap1)

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()

