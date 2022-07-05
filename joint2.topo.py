from node import *

class joint2(Topo):
    def build(self):
        self.add_node("0")
        self.add_node("1")
        self.add_node("2")
        self.add_node("3")
        self.add_node("4")
        self.add_node("5")
        self.add_node("6")
        self.add_node("7")
        self.add_node("8")
        self.add_node("9")
        self.add_node("11")
        self.add_node("12")
        self.add_node("13")
        self.add_node("14")
        self.add_link_name("0", "1", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("1", "0", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("1", "2", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("2", "1", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("2", "3", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("3", "2", cost=1000, delay=0.2, bw=4000000000000, directed=True)
        self.add_link_name("0", "4", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("4", "0", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("1", "4", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("4", "1", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("2", "4", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("4", "2", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("3", "4", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("4", "3", cost=4000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("11", "0", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("12", "0", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("13", "0", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("14", "0", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("0", "11", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("0", "12", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("0", "13", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("0", "14", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("4", "5", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("5", "4", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("5", "6", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("6", "5", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("6", "7", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("7", "6", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("7", "8", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("8", "7", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("9", "5", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("5", "9", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("9", "6", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("6", "9", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("9", "7", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("7", "9", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("9", "8", cost=1000, delay=0.2, bw=1000000000000, directed=True)
        self.add_link_name("8", "9", cost=1000, delay=0.2, bw=1000000000000, directed=True)
    
    def dijkstra_computed(self):
        # Demand from 11 to 9
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("11","4")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {4} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("11", f"ip -6 route add {{9}} metric 1 table 1 src {{11}}  {build_str}")
        # Demand from 12 to 9
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("12","1")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {1} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("12", f"ip -6 route add {{9}} metric 1 table 1 src {{12}}  {build_str}")
        # Demand from 13 to 9
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("13","2")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {2} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("13", f"ip -6 route add {{9}} metric 1 table 1 src {{13}}  {build_str}")
        # Demand from 14 to 9
        build_str = ""
        nhlist = self.get_dijkstra_route_by_name("14","3")
        for nh in nhlist:
            build_str += f" nexthop via {nh.nh} "+" encap seg6 mode inline segs {3} "+ f" weight {int(100/len(nhlist))} "
        self.add_command("14", f"ip -6 route add {{9}} metric 1 table 1 src {{14}}  {build_str}")
        self.add_command("11", "ip -6 rule add to {9/} iif lo table 1")
        self.add_command("12", "ip -6 rule add to {9/} iif lo table 1")
        self.add_command("13", "ip -6 rule add to {9/} iif lo table 1")
        self.add_command("14", "ip -6 rule add to {9/} iif lo table 1")
        self.add_command("9", "nuttcp -6 -S")
        self.add_command("11", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 11 nuttcp -T300 -i1 -R10000 -N32 {9} \>\>flow_11-9.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_11-9.txt\; done\\\" | at now+2min')
        self.add_command("12", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 12 nuttcp -T300 -i1 -R10000 -N32 {9} \>\>flow_12-9.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_12-9.txt\; done\\\" | at now+2min')
        self.add_command("13", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 13 nuttcp -T300 -i1 -R10000 -N32 {9} \>\>flow_13-9.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_13-9.txt\; done\\\" | at now+2min')
        self.add_command("14", 'echo bash -c \\\"START=\\\\\$SECONDS\; while \! ip netns exec 14 nuttcp -T300 -i1 -R10000 -N32 {9} \>\>flow_14-9.txt 2\>\&1 \; do sleep 1\; echo RTY\: \\\\\$SECONDS \>\>flow_14-9.txt\; done\\\" | at now+2min')

        self.enable_throughput()
        self.add_command("0", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("1", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("2", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("3", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("4", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("5", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("6", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("7", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("8", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("9", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("11", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("12", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("13", "sysctl net.ipv6.fib_multipath_hash_policy=1")
        self.add_command("14", "sysctl net.ipv6.fib_multipath_hash_policy=1")

topos = {'joint2': (lambda: joint2())}
