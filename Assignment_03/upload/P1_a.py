#!/usr/bin/env python
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.nodelib import LinuxBridge
from mininet.log import setLogLevel

if __name__ == '__main__':
    setLogLevel('info')

    net = Mininet(switch=LinuxBridge, controller=None)
    # Adding main hosts
    h1 = net.addHost('h1', ip=None)
    h2 = net.addHost('h2', ip=None)

    # Creating routers as hostes with forwarding capabilities
    r1 = net.addHost('r1', ip=None)
    print r1.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")
    r2 = net.addHost('r2', ip=None)
    print r2.cmd("sysctl -w net.ipv6.conf.all.forwarding=1")

    # configure IPv6 addresses and forwarding table entries here
    s0 = net.addSwitch('s0')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    # setup links between hosts, routers, switches (order matters)
    net.addLink(h1, s1)
    net.addLink(r1, s1)
    net.addLink(r1, s0)
    net.addLink(r2, s0)
    net.addLink(r2, s2)
    net.addLink(h2, s2)
    # Setting all IPv6 addresses using the IP(8) command
    print h1.cmd("ip -6 address add 2001:638:709:a::1/64 dev h1-eth0")
    print h2.cmd("ip -6 address add 2001:638:709:b::1/64 dev h2-eth0")
    print r1.cmd("ip -6 address add 2001:638:709:a::f/64 dev r1-eth0")
    print r1.cmd("ip -6 address add 2001:638:709:f::1/64 dev r1-eth1")
    print r2.cmd("ip -6 address add 2001:638:709:f::2/64 dev r2-eth0")
    print r2.cmd("ip -6 address add 2001:638:709:b::f/64 dev r2-eth1")
    # forwarding table between h1 and r1
    print h1.cmd("ip -6 route add 2001:638:709::/48 via 2001:638:709:a::f dev h1-eth0")
    print r1.cmd("ip -6 route add 2001:638:709:a::/64 dev r1-eth0")
    print r1.cmd("ip -6 route add 2001:638:709:f::/64 dev r1-eth1")
    print r1.cmd("ip -6 route add 2001:638:709:b::/64 via 2001:638:709:f::2 dev r1-eth1")
    # forwarding table between h2 and r2
    print r2.cmd("ip -6 route add 2001:638:709:f::/64 dev r2-eth0")
    print r2.cmd("ip -6 route add 2001:638:709:b::/64 dev r2-eth1")
    print r2.cmd("ip -6 route add 2001:638:709:a::/64 via 2001:638:709:f::1 dev r2-eth0")
    print h2.cmd("ip -6 route add 2001:638:709::/48 via 2001:638:709:b::f dev h2-eth0")
    net.start()
    CLI(net)
    net.stop()
