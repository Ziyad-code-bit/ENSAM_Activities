adresse_ip=["192.168.0.1","10.0.0.1","172.32.0.1","200.100.50.1","169.254.0.1"]
typeDesAdresses={
    "192.168.0.1":"classe C",
    "10.0.0.1":"classe A",
    "200.100.50.1":"IP P", #P as in Publique
    "169.254.0.1":"IP APIPA"
}
#1
print(adresse_ip[0])
#2
print(adresse_ip[len(adresse_ip)-1])
#3
print(adresse_ip[2])
#4
adresse_ip.append("172.31.0.1")
#5
adresse_ip.remove("200.100.50.1")
#6
print(len(adresse_ip))
#7
print("192.168.0.1" in adresse_ip)
#8
if typeDesAdresses.get("10.0.0.1").split()[0]=="classe":
    print("10.0.0.1 est de "+typeDesAdresses.get("10.0.0.1")+".")
else:
    print("10.0.0.1 n'est pas une adresse avec une classe.")
#9
adresse_ip.sort(key = lambda x:[int(p) for p in x.split('.')])
print(adresse_ip)
#10
f=True
for adress in adresse_ip:
    if typeDesAdresses.get(adress)!="classe C":
        f=False
if f:
    print("All registered IP adresses are of class C.")
else:
    print("Some IP adresses are not of class C.")
#11
s=0
for adress in adresse_ip:
    if typeDesAdresses.get(adress)=="IP P":
        s+=1
print("Le nombre d'adress de type publique est",s,".")