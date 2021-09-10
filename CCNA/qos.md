access-list 111 permit udp any any eq 5004

class-map voice
    match access-group 111

policy-map policy01
    class voice
        priority xxx
        class class-default
        fair-queue

int f0/0
    service-policy output policy01