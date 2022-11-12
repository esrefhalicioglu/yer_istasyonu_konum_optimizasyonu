from asyncio import sleep
from sgp4.api import Satrec
from sgp4.api import jday
from skyfield.api import load
from skyfield.api import wgs84
from skyfield.api import EarthSatellite
import time

ts = load.timescale()

# YYYY[0] MM[1] DD[2] HH[3] MM[4] SS[5]
#date=input("Başlangıç değerlerini girin. FORMAT = YYYY MM DD HH MM SS  (Ay ve Gün değerleri 0 ile başlayamaz)")
#dateStart=date.split(" ")
#print("Başlangıç değerlerini girin")
#sec=int(input("Saniye = "))
#min=int(input("Dakika = "))
#hr=int(input("Saat = "))
#day=int(input("Gün = "))
#mm=int(input("Ay = "))
#yy=int(input("Yıl = "))
#date=input("Başlangıç değerlerini girin. FORMAT = YYYY MM DD HH MM SS  (Ay ve Gün değerleri 0 ile başlayamaz)")
#dateEnd=date.split(" ")
#print("Bitiş değerlerini girin")
#Esec=int(input("Saniye = "))
#Emin=int(input("Dakika = "))
#Ehr=int(input("Saat = "))
#Eday=int(input("Gün = "))
#Emm=int(input("Ay = "))
#Eyy=int(input("Yıl = "))

s1 = '1 00001U 22057A   22307.37500000 -.00001397  00000-0 -76360-4 0 00007'
t1 = '2 00001 097.4774 222.6086 0010653 270.7467 089.2496 15.14327510000013'

s2 ='1 00002U 22057B   22307.37500000 -.00001704  00000-0 -88087-4 0 00009'
t2 ='2 00002 097.4545 224.9163 0010666 270.7403 089.2560 15.16303447000012'

s3 ='1 00003U 22057C   22307.37500000 -.00001050  00000-0 -44789-4 0 00005'
t3 ='2 00003 049.0198 169.0033 0008233 268.9774 091.0234 15.22246908000016'

s4 ='1 00004U 22057D   22307.37500000  .00003774  00000-0  36004-3 0 00009'
t4 ='2 00004 078.8925 064.6273 0091267 126.2799 351.7935 14.90232971000016'

s5 ='1 00005U 22057E   22307.37500000 -.00000116  00000-0 -12113-4 0 00005'
t5 ='2 00005 125.9981 355.3340 0008660 269.1871 217.3510 14.89302971000013'

#satellite1 = Satrec.twoline2rv(s1, t1)
#jdS, frS = jday(2022, 11, 4, 15, 0, 0)
#jdE, frE = jday(2022, 11, 11, 15, 0, 0)
#jd, fr = 2458827, 0.362605
#e, r, v = satellite1.sgp4(jdS, frS)
#eS, rS, vS = satellite1.sgp4(jdE, frE)





t_start = ts.utc(2022, 11, 4, 15, 0, 0)
#t_temp=ts.utc(year,month,day,hour,min,sec)
t_end = ts.utc(2022 ,11 ,11 ,15 ,0 ,0)
satellite1 = EarthSatellite(s1, t1)
satellite2 = EarthSatellite(s2, t2)
satellite3 = EarthSatellite(s3, t3)
satellite4 = EarthSatellite(s4, t4)
satellite5 = EarthSatellite(s5, t5)
satellites = [satellite1,satellite2,satellite3,satellite4,satellite5]
konum=[]
print(satellite1)
print(type(satellite1))
datetime_list = []
data1=0
print("Yer Istasyonu Konumlari: ")
            
print("Yer Istasyonu 1")
print("Enlem: ",35.52545242773814)
print("Boylam: ",38.90974475726466)
print("Rakım: ",1000)
print("\n....\n")
print("##### Yer Istasyonu 1 Geçişleri:\n")            

print("         Zaman                     Uydu            Azm           Elv        İndirilen Data Boyutu")
print("-----------------------          ------------    ------        -----        ----------------------")

for i in satellites:
    uydu = ""
    data1 = 0
    sec=0
    min=0
    hour=15
    day=4
    month=11
    year=2022
    if(i==satellite1):
        uydu = "satellite1"
    if(i==satellite2):
        uydu = "satellite2"
    if(i==satellite3):
        uydu = "satellite3"
    if(i==satellite4):
        uydu = "satellite4"
        
    if(i==satellite5):
        uydu = "satellite5"
    while True:
        t_temp=ts.utc(year,month,day,hour,min,sec)
        indirilen_veri = 0
        temp = i.at(t_temp)
        bluffton = wgs84.latlon(35.52545242773814, 38.90974475726466,1000)
        difference = i - bluffton
        topocentric = difference.at(t_temp)
        alt, az, distance = topocentric.altaz()
        sec+=30
        if alt.degrees>5:
            data1+=alt.degrees*0.04
            indirilen_veri = alt.degrees*0.04
        if sec==60:
            min+=1
            if(min %5 == 0):
                print(str(year)+"-"+str(month)+"-"+str(day)+"-"+str(hour)+"-"+str(min)+"-"+str(sec)+"                "+uydu + "      "+str(round(az.degrees,2))+"       "+str(round(alt.degrees,2))+"                "+str(indirilen_veri))
            sec=0
        if min==60:
            hour+=1
            
            min=0
        if hour==24:
            day+=1
            hour=0
            # print(alt.degrees, " temp = ",t_temp)
        if day==30:
            month+=1
            day=1
        if month==12:
            year+=1
            month=1
        if t_temp == t_end:
            print("MB = " , data1*30)
            time.sleep(10)
            break
#          elv=[]
#         largest=-91
#         for j in satellites:
#             t_temp=ts.utc(year,month,day,hour,min,sec)
#             #sleep(1)
#             temp = j.at(t_temp)
#             #lat,lon = wgs84.latlon_of(temp) #latitude: enlem #longitude:boylam
#             #lat, lon = wgs84.latlon_of(geocentric)
#             #g = geocoder.elevation([lat,lon])
#             bluffton = wgs84.latlon(35.52545242773814, 38.90974475726466,1000)
#             difference = j - bluffton
#             topocentric = difference.at(t_temp)
#             #print(topocentric.position.km)
#             alt, az, distance = topocentric.altaz()
#             elv.append(alt.degrees)
#             sayac = 0
#             largest_index =0
#             if(j == satellite5):
#                 for ele in elv:
#                     if (ele > largest):
#                         largest = ele
#                         largest_index = sayac
#                     sayac+=1
#                 while largest > 5:
#                     satellites[largest_index].at(t_temp)
#                     bluffton = wgs84.latlon(35.52545242773814, 38.90974475726466,1000)
#                     difference = satellites[largest_index] - bluffton
#                     topocentric = difference.at(t_temp)
#                     alt, az, distance = topocentric.altaz()
#                     largest = alt.degrees
#                     if alt.degrees > 5:
#                         data1+=alt.degrees*0.04
#                     sec+=20
#                     if sec==60:
#                         min+=1
#                         sec=0
#                     if min==60:
#                         hour+=1
#                         min=0
#                     if hour==24:
#                         day+=1
#                         hour=0
#                         print(alt.degrees, " temp = ",t_temp)
#                     if day==30:
#                         month+=1
#                         day=1
#                     if month==12:
#                         year+=1
#                         month=1 
        # t_temp=ts.utc(year,month,day,hour,min,sec)
        # temp = i.at(t_temp)
        # lat,lon = wgs84.latlon_of(temp) #latitude: enlem #longitude:boylam
        # bluffton = wgs84.latlon(35.52545242773814, 38.90974475726466,1000)
        # difference = i - bluffton
        # topocentric = difference.at(t_temp)
        # alt, az, distance = topocentric.altaz()
        #temp = i.at(t_temp)
        #lat,lon = wgs84.latlon_of(temp) #latitude: enlem #longitude:boylam
        #bluffton = wgs84.latlon(35.52545242773814, 38.90974475726466)
        #difference = i - bluffton
        #topocentric = difference.at(t_temp)
        #alt, az, distance = topocentric.altaz()
        
        #if(lat.degrees>25 and lat.degrees <46 and lon.degrees<42 and lon.degrees>36):
            #print(lat.degrees,lon.degrees)
            #konum.append([lat.degrees,lon.degrees])


            
# print(konum)
# print(len(konum))
# lat_toplam = 0
# lon_toplam = 0
# for ele in konum:
#     lat_toplam += ele[0]
#     lon_toplam += ele[1]
        #print('Elevation:', alt)
        #print('Azimuth:', az)
        #print('Distance: {:.1f} km'.format(distance.km))

# ortalama_lat = lat_toplam / len(konum)
# ortalama_lon = lon_toplam / len(konum)
# print(ortalama_lat, ortalama_lon)
#print('Latitude:', lat)
#print('Longitude:', lon)
#print(g.meters)

#print(e)
#print("Başlangıç konum(r) = ",r,"  hız(v) = ",v)
#print("Bitiş konum (rS) = ",rS," hız(vS) = ",vS)
