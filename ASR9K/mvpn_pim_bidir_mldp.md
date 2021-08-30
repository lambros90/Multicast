```sh
multicast-routing
vrf blue
    address-family ipv4
    mdt partitioned mldp ipv4 mp2mp bidir
    interface all enable
    bgp auto-discovery mldp
    address-family ipv6
    mdt partitioned mldp ipv4 mp2mp bidir
    interface all enable
    bgp auto-discovery mldp
router pim
vrf blue
    address-family ipv4
    rpf topology route-policy mp2mp-part
    rp-address 120.120.120.120 bidir-acl-blue-v4-bidir
    address-family ipv6
    rpf topology route-policy mp2mp-part
    rp-address 120:120::120:120 bidir-acl-bue-v6-bidir
```