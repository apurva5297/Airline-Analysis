import flightclass as flight
def getAllFight():
    flightdata = []
    filedata = open("Indigo.txt", "r")
    for row in filedata.readlines():
        src, dst = row.split(",")
        f = flight.Flight()
        f.setSrc(src)
        f.setDest(dst)
        flightdata.append(f)
    return flightdata
def getFlightinfo():
    src=input("enter source").strip().upper()
    dst=input("enter destination").strip().upper()
    dirflight=[]
    tempflight=[]
    allflight=getAllFight()
    print("direct flight")
    for f in allflight:
        print(f.getSrc(),f.getDest())
        if (f.getSrc==src and f.getDest==dst):
            dirflight.append(f)
        else:
            tempflight.append(f)
    for d in dirflight:
        print(d.getSrc(),d.getDest())
getFlightinfo()
