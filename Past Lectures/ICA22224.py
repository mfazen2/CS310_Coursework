import math
from riseset import riseandset 
class star:
    def __init__(self,name,ra,dec,dist,absmag):
        self.name = str(name)
        self.ra = tuple(ra)
        self.dec = tuple(dec)
        self.dist = float(dist)
        self.absmag=float(absmag)
    def appmag(self):
        return 5*(math.log(self.dist-1))+self.absmag
    def __str__(self)->str:
        return f"Star: {self.name}\nRA: {self.ra[0]}h {self.ra[1]}m {self.ra[2]}s\nDec: {self.dec[0]}d {self.dec[1]}\' {self.dec[2]}\"\nMag: {self.absmag}\nDist: {self.dist} pc"
    def riseandset(self,lat,long,year,month,date):
        return riseandset(self.ra,self.dec,lat,long,year,month,date)
    

temp = star("Betelguese",(5 ,55 ,10.3),(7, 24, 25.4),-5.85,220.0)
print(temp)
print(temp.riseandset(40.112,-88.221,2024,2,24))
