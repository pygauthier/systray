import ifaddr

adapters = ifaddr.get_adapters()

for adapter in adapters:
    for ip in adapter.ips:
        print (adapter.nice_name +"   %s/%s" % (ip.ip, ip.network_prefix))
'''

[
    Adapter(
        name=b'{2B46CD4B-DDF8-4273-8DE4-2B8EE885787C}', 
        nice_name='Fortinet Virtual Ethernet Adapter (NDIS 6.30)', 
        ips=[
            IP(ip=('fe80::c565:f98f:3dec:cd1c', 0, 6), 
            network_prefix=64, nice_name='Ethernet 2'), 
            IP(ip='169.254.205.28', network_prefix=16, nice_name='Ethernet 2')
            ]
        ), 
    
    Adapter(
        name=b'{9BEF06E7-2412-4BB9-8439-48808DE31DDA}', 
        nice_name='Hyper-V Virtual Ethernet Adapter #2', 
        ips=[
            IP(
                ip=('fe80::5c3f:dbb9:c5b:22a4', 0, 19), 
                network_prefix=64, 
                nice_name='vEthernet (DockerNAT)'
                ), 
            IP(
                ip='10.0.75.1', network_prefix=24, 
                nice_name='vEthernet (DockerNAT)')
        ]
    ), 
    Adapter(
        name=b'{3C80602A-FC05-43C8-9973-3850E1570962}', 
        nice_name='Intel(R) Ethernet Connection (4) I219-V', 
        ips=[
            IP(
                ip=('fe80::3005:2a0a:d2ac:6224', 0, 8), 
                network_prefix=64, nice_name='Ethernet'
            ), 
            IP(
                ip='10.1.0.102', 
                network_prefix=24, 
                nice_name='Ethernet')
        ]
    ), 
    Adapter(
        name=b'{D2D78099-01DE-4D34-BA8A-39843B406BF5}', 
        nice_name='Intel(R) Dual Band Wireless-AC 8265', 
        ips=[
            IP(
                ip=('fe80::40d4:401a:d00e:3e53', 0, 23), 
                network_prefix=64, 
                nice_name='Wi-Fi'
            ), 
            IP(
                ip='169.254.62.83', 
                network_prefix=16, 
                nice_name='Wi-Fi')
        ]
    ), 
    Adapter(
        name=b'{8FD056D7-E0ED-4126-8413-5BC3DB97E166}', 
        nice_name='Microsoft Wi-Fi Direct Virtual Adapter', 
        ips=[
            IP(
                ip=('fe80::f0b7:981d:c217:e48', 0, 17), 
                network_prefix=64, 
                nice_name='Connexion au réseau local* 2'
            ), 
            IP(
                ip='169.254.14.72', 
                network_prefix=16, 
                nice_name='Connexion au réseau local* 2'
            )
        ]
    ),
    Adapter(
        name=b'{8680B588-FBAC-403F-9A83-75A84472307E}', 
        nice_name='Microsoft Wi-Fi Direct Virtual Adapter #2', 
        ips=[
            IP(
                ip=('fe80::55ce:1cf4:117d:ed49', 0, 15), 
                network_prefix=64, 
                nice_name='Connexion au réseau local* 3'
            ), 
            IP(
                ip='169.254.237.73', 
                network_prefix=16, 
                nice_name='Connexion au réseau local* 3'
            )
        ]
    ), 
    Adapter(
        name=b'{4A87B248-5072-11E7-983A-806E6F6E6963}', 
        nice_name='Software Loopback Interface 1', 
        ips=[
            IP(
                ip=('::1', 0, 0), 
                network_prefix=128, 
                nice_name='Loopback Pseudo-Interface 1'
            ), 
            IP(
                ip='127.0.0.1', 
                network_prefix=8, 
                nice_name='Loopback Pseudo-Interface 1'
            )
        ]
    ), 
    Adapter(
        name=b'{FB60A114-D9EE-4FC7-A934-53372850E4E3}', 
        nice_name='Hyper-V Virtual Ethernet Adapter', 
        ips=[
            IP(
                ip=('fe80::456a:6020:1e5c:2d23', 0, 27), 
                network_prefix=64, 
                nice_name='vEthernet (Commutateur par)'
            ), 
            IP(
                ip='172.22.252.145', 
                network_prefix=28, 
                nice_name='vEthernet (Commutateur par)'
            )
        ]
    )
]
'''
"""
c:\Users\******\Desktop>ipconfig

Configuration IP de Windows


Carte Ethernet Ethernet 2 :

   Statut du média. . . . . . . . . . . . : Média déconnecté
   Suffixe DNS propre à la connexion. . . :

Carte Ethernet vEthernet (DockerNAT) :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::5c3f:dbb9:c5b:22a4%19
   Adresse IPv4. . . . . . . . . . . . . .: 10.0.75.1
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   Passerelle par défaut. . . . . . . . . :

Carte Ethernet Ethernet :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::3005:2a0a:d2ac:6224%8
   Adresse IPv4. . . . . . . . . . . . . .: 10.1.0.102
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   Passerelle par défaut. . . . . . . . . : 10.1.0.1

Carte réseau sans fil Wi-Fi :

   Statut du média. . . . . . . . . . . . : Média déconnecté
   Suffixe DNS propre à la connexion. . . :

Carte réseau sans fil Connexion au réseau local* 2 :

   Statut du média. . . . . . . . . . . . : Média déconnecté
   Suffixe DNS propre à la connexion. . . :

Carte réseau sans fil Connexion au réseau local* 3 :

   Statut du média. . . . . . . . . . . . : Média déconnecté
   Suffixe DNS propre à la connexion. . . :

Carte Ethernet vEthernet (Commutateur par) :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::456a:6020:1e5c:2d23%27
   Adresse IPv4. . . . . . . . . . . . . .: 172.22.252.145
   Masque de sous-réseau. . . . . . . . . : 255.255.255.240
   Passerelle par défaut. . . . . . . . . :

"""