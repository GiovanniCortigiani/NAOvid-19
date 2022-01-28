#!/usr/bin/env python
## Script to check JSON requests

import requests
import json
r = requests.post('http://0.0.0.0:8000', json={"dcc": "HC1:6BFOXN*TS0BI$ZDFRH%YJLABRKAIPH769WFI3XHP+56R55JPEZP.TMNV4J16D8N:UC*GPXS40 LHZA KE3%G%9DJ6K1AD1WMN+I0JK1WLBUKDJL HG JM5JISILNVA$TJ+6HM9M-PA28LC4G479CEL.19GPM1JAF.7-FODXI47T9ZI4Q5%H0AN8.L86YB:WOP+P6OIB.VT*QNC2BFUF$SU%BO*N5PIBPIAOI-+R2YBV44PZBSK0HJOJ0RIE9WT0K3M9UVZSVV*001HW%8UE9ZC55B9-NT0 2$$0X4PCY0+-CVYCDEBD0HX2JR$4O1K8KES/F-1JF.K+D7W 17O4B-S-*O5W41FDOD5EC7F.O9NT4FF/HL-DF-FHL85W7U3NV:OT1FDIV4F5U52ITNP8EF4FFE1ML.FC:H+$5$7U/487S47*KB*KYQTKWT4S8W%U:T6X MC6DJ37O-M-B7UZ539WYJ7+5GAWQG.DD RK7N/80E8NKBMU3EBWU$FOHXBL7PRRJDHC*5O:-NMWK-SI*IADPHNLA*3E961L50W2081"})
#r.status_code
data = r.json()
val = False
if (data.get('valid') == True):
    val = True

print("Covid Certificate is ")
print(val)

#loads = json.loads(r)
name = data['dccdata']['-260']['1']['nam']['fn'] + ' ' + data['dccdata']['-260']['1']['nam']['gn']
print(name)
