import MySQLdb
import math
def dbConnection():

    conn = MySQLdb.connect(host="sql12.freesqldatabase.com", user="sql12245338", passwd="jKTYhdgkdF", db="sql12245338")
    cursor = conn.cursor()
    return cursor;

cursor=dbConnection()
Id="12345"

cursor.execute('SELECT RouteID FROM Device WHERE DeviceID='+Id)
rID = cursor.fetchone()
routeID=rID[0]
halt

print routeID

def closestHaltCal(halt_detail,gps_reading):
    halt_data_list=halt_detail
    halt_lat=float(halt_data_list[3])
    halt_lng=float(halt_data_list[4])

    gps_lat=float(gps_reading[0])
    gps_lng=float(gps_reading[1])

    diff=math.sqrt((halt_lat-gps_lat)**2+(halt_lng-gps_lng)**2)
    return diff


cursor.execute('SELECT * FROM Route')
halt_data=cursor.fetchall()
halt_det={}
in_diff={}
out_diff={}
def haltDetails(halt_data):
    for row in halt_data:
        halt_det[row[1]]=[row[2],row[3],row[4]]
        
haltDetails(halt_data)    


def retriveUserGPS(user_id):
    cursor.execute('SELECT * FROM UserStats WHERE UserId='+user_id)#where user should be added
    user_data=cursor.fetchall()
    ingps=[]
    outgps=[]
    for user_detail in user_data:
        inLat=user_detail[1]
        inLng=user_detail[2]
        outLat=user_detail[3]
        outLng=user_detail[4]
        
        ingps.append(inLat)
        ingps.append(inLng)
        outgps.append(outLat)
        outgps.append(outLng)
    return ingps,outgps
    
inGPS,outGPS=retriveUserGPS(900)
for row in halt_data:
    in_dis_diff=closestHaltCal(row,inGPS) #in_gps should be the gps_reading
    
    in_diff[row[1]]=in_dis_diff
    
    out_dis_diff=closestHaltCal(row,outGPS) #in_gps should be the gps_reading
    out_diff[row[1]]=out_dis_diff

closet_in_halt=min(in_diff, key=in_diff.get)#haltid_in
closet_out_halt=min(out_diff, key=out_diff.get)#haltid_out





    
    

    
    

