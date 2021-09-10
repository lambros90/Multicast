ip sla 2
    icmp-echo 4.2.2.2
    timeout 1000
    frequency 25
    hustory hours-of-statistics-kept 25
    history distributions-of-statistics-kept 2
    history lives-kept 2
    history enhanced interval 3600 buckets 50
ip sla schedule 2 life forever start-time now
track 2 ip sla 2 reachability delay down 100 up 60

ip route 0.0.0.0 0.0.0.0 172.16.1.254 track 2 /ISP1
ip route 0.0.0.0 0.0.0.0 172.16.1.1 128       /ISP2