import pandas as pd

airmod_file="airports_mod.dat"
final_file="Final_airlines"
routes_file="routes.dat"

airmod_name=['ID','Name','City','Country','FAA','IATA','ICAO','Latitude','Longitude','Altitude','Timezone','DST','Timezone']
final_name=['ID','Name','Alias','IATA','ICAO','CallSign','Country','Active']
routes_name=['Airline','ID','Src','SID','Dst','DID','CS','Stops','Equip']

airmod_data=pd.read_csv(airmod_file,sep=',',names=airmod_name)
final_data=pd.read_csv(final_file,sep=',',names=final_name)
routes_data=pd.read_csv(routes_file,sep=',',names=routes_name)

#print(airmod_data)
#print(final_data)
#print(routes_data)
def ind():
    l=[]
    g1=airmod_data.groupby(['Name','Country'])
    for i in g1:
        if i[0][1]=='India':
            l.append(i)
    print(l)
def stps():
    l=[]
    g2=routes_data.groupby(['Stops','Airline'])
    for i in g2:
        if i[0][0]==0:
            l.append(i)
    print(l)
def cds():
    l=[]
    g3=routes_data.groupby(['Airline','CS'])
    for i in g3:
        if i[0][1]=='Y':
            l.append(i)
    print(l)
def maxair():
    l = []
    g4 = airmod_data.groupby('Altitude')
    for i in g4:
        l.append(i)
    print(max(l))


def actv():
    g5=final_data.groupby(['Country','Active'])
    for i in g5:
        if(i[0][0]=='United States' and i[0][1]=='Y'):
            print(i)

flag = 1


while (flag == 1):
    print('1. Find list of Airports operating in the Country India ')
    print('2. Find the list of Airlines having zero stops')
    print('3. List of Airlines operating with code share')
    print('4. Which country (or) territory having highest Airports')
    print('5. Find the list of Active Airlines in United state')
    print('6.Exit')

    a=int(input("Select desired operation to perform="))

    if a==1:
        ind()
    elif a==2:
        stps()
    elif a==3:
        cds()
    elif a==4:
        maxair()
    elif a==5:
        actv()
    elif a==6:
        flag=0
        break
    else:
        continue

