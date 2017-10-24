# Performance of SDN Routing in Comparison with Legacy Routing Protocols
#### Matúš Brandýs, Dominik Pastierovič
#### Cvičiaci: Ing. Pavol Helebrant, PhD.

## Úvod
Staršie routovacie protokoly ako napríklad OSPF a BGP sa vyvinuli do veľmi obsiahlej podoby, ale ich neflexibilný systém sa nestíha prispôsobovať rýchlo rastúcemu internetu. Ako jedno z riešení tohto problému sa ukazuje použitie softvérovo definovaných sietí. SDN siete dokážu dosiahnuť efektivitu v routovaní pomocou výhod centralizovanej kontroly. Je však výkon SDN sietí naozaj lepší ako starších routovacích protokolov? V našej práci sa zameriame na porovnanie výkonnosti protokolu OSPF s SDN na veľkostne rôznych topológiách.

# Návrh
Postup riešenia:
  - Vytvorenie topológie s 16 switchami a 2 hostmi
  - Vytvorenie topológie so 120 switchami a 2 hostmi
  - Otestovanie doby odozvy v oboch topológiách OSPF aj SDN
  - Porovnanie času potrebného na skonvergovanie OSPF a SDN
  - Porovnanie času potrebného na skonvergovanie OSPF a SDN počas rôzných link delay (2ms, 16ms, 26ms)
  
#### *Poznámka
Smerovače v rámci OSPF topolóogie, budú všetky v patriť do area 0.

Riešenie vyžaduje:
  - Mininet v2.1.0
  - Mininext
  - Floodlight controler pre SDN

