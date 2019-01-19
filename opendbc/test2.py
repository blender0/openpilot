import os
import csv

cur_path = os.path.dirname(os.path.realpath(__file__))
msgs = []

def logical_xor(str1, str2):
    return "%0.2X" %(int(str1, 16) ^ int(str2, 16))

def logical_and(str1, str2):
    return "%0.2X" %(int(str1, 16) & int(str2, 16))

def read_file(dir_name, filename):
    with open(os.path.join(dir_name, filename)) as file_in:
        return file_in.read()

def open_data(dir_name, filename):
    addrs = {}

    with open(filename) as f:
        rdr = csv.reader(f, delimiter=',')
        cnt = 0
        for r in rdr:
            if cnt == 0:
                print r
                cnt += 1
            else:
                # addrs[r[1]] = r[3]
                # msgs[float(r[0])] = addrs
                # msgs.append( (float(r[0]), 
                #                 {(r[1], r[2]), r[3]}))
                msgs.append( (float(r[0]), r[1], r[2], r[3]) )
                cnt += 1

            if (cnt % 5000) == 0:
                print cnt

            if cnt > 465000:
                break

def get_vals_at_time(time):
    ret = {}

    for m in msgs:
        # print m
        if m[0] >= time:
            break
        ret[m[1]] = m[3]
        # print m[1]

    # print ret
    return ret

def comp_state_dif(s1, s2):
    ret = {}
   
    for addr in s2.keys():
        addrs = {}
        if s1.has_key(addr):
            # print s1[addr]
            # print s2[addr]
            x = logical_xor(s1[addr], s2[addr])
            # print x
            if int(x, 16) > 0:
                addrs[addr] = x
                ret[addr] = x
                # ret.append(addrs.copy())

    return ret

def comp_state_eq(s1, s2):
    ret = {}

    for addr in s2.keys():
        addrs = {}
        if s1.has_key(addr):
            x = logical_and(s1[addr], s2[addr])

            if int(x, 16) > 0:
                addrs[addr] = x
                ret[addr] = x
    return ret

def match_state(on_tms, off_tms):
    ret_on = get_vals_at_time(on_tms[0])
    ret_off = get_vals_at_time(off_tms[0])

    for on in on_tms:
        ret_on = comp_state_eq(ret_on, get_vals_at_time(on))

    for off in off_tms:
        ret_off = comp_state_eq(ret_off, get_vals_at_time(off))

    ret = comp_state_dif(ret_on, ret_off)

    return ret

def add_bus_name(x):
    bus_def = {'1017':'ECS12:','1024':'CLU_CFG11:','1040':'CGW_USM1:','1056':'SCC11:','1057':'SCC12:','1064':'_4WD11:','1065':'_4WD12:','1066':'_4WD13:',
                '1078':'PAS11:','1151':'ESP11:','1168':'EPB11:','1170':'EMS19:','1265':'CLU11:','1268':'SPAS12:','127':'CGW5:','128':'EMS_DCT11:',
                '1280':'ACU14:','1281':'ECS11:','1282':'TCU14:','1287':'TCS15:','129':'EMS_DCT12:','1290':'SCC13:','1292':'CLU13:','1301':'CLU14:',
                '1307':'CLU16:','1312':'CGW3:','1313':'GW_DDM_PE:','1314':'GW_IPM_PE_1:','1315':'GW_SWRC_PE:','1316':'GW_HU_E_00:','1317':'GW_HU_E_01:','1318':'HU_GW_E_00:',
                '1319':'HU_GW_E_01:','1322':'CLU15:','1338':'TMU_GW_E_01:','1342':'LKAS12:','1345':'CGW1:','1349':'EMS14:','1350':'DI_BOX12:','1351':'EMS15:',
                '1353':'BAT11:','1356':'TCU_DCT14:','1360':'IAP11:','1362':'SNV11:','1363':'CGW2:','1365':'FPCM11:','1366':'EngFrzFrm11:','1367':'EngFrzFrm12:',
                '1369':'CGW4:','1370':'HU_AVM_PE_00:','1371':'AVM_HU_PE_00:','1378':'HUD11:','1379':'PGS_HU_PE_01:','1393':'OPI11:','1395':'HU_AVM_E_01:','1397':'HU_AVM_E_00:',
                '1407':'HU_MON_PE_01:','1411':'CUBIS11:','1412':'AAF11:','1414':'EVP11:','1415':'TMU11:','1419':'LCA11:','1425':'AFLS11:','1427':'TPMS11:',
                '1434':'PSB11:','1437':'AHLS11:','1440':'ACU11:','1441':'ACU12:','1456':'CLU12:','1472':'GW_Warning_PE:','1479':'EMS21:','1490':'HU_DATC_E_02:',
                '1491':'HU_DATC_PE_00:','1492':'TMU_GW_PE_01:','1530':'ODS11:','1531':'ODS12:','1532':'ODS13:','16':'ACU13:','1984':'CAL_SAS11:','273':'TCU11:',
                '274':'TCU12:','275':'TCU13:','339':'TCS11:','354':'TCU_DCT13:','356':'VSM11:','387':'REA11:','399':'EMS_H12:','48':'EMS18:',
                '512':'EMS20:','544':'ESP12:','593':'MDPS12:','608':'EMS16:','625':'LPI11:','64':'DATC14:','640':'EMS13:','66':'DATC12:',
                '67':'DATC13:','68':'DATC11:','688':'SAS11:','790':'EMS11:','809':'EMS12:','832':'LKAS11:','871':'LVR12:','872':'LVR11:',
                '896':'DI_BOX13:','897':'MDPS11:','899':'FATC11:','900':'EMS17:','902':'WHL_SPD11:','903':'WHL_PUL11:','906':'ABS11:','912':'SPAS11:',
                '915':'TCS12:','916':'TCS13:' }
    dct = {}

    for k in x.keys():
        if bus_def.has_key(k):
            dct[(k, hex(int(k)), bus_def[k])] = x[k]
        else:
            dct[(k, hex(int(k)), 'undefined')] = x[k]

    return dct

###############################################################

open_data(cur_path, "test.csv")

known_on = [12.2, 14.555, 15.123, 16.456, 17.951, 18, 19, 20, 21, 22, 23, 24.24, 25, 26, 27, 28, 29, 30, 31.1, 42.1, 43, 44]
known_off = [35.1, 37.37, 39, 47.5, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 100, 115]

# known_on = [31]
# known_off = [35.123]

# 12.2, 31.7, 40, 44.1

res = match_state(known_on, known_off)
print "res:"
print res
print ""
res2 = add_bus_name(res)
print(res2)
print ""


for k in res2.keys():
    print str(k) + "," + res2[k]
    # if k[2] == 'undefined':  # and res2[k] != '4044'
    #     print str(k) + "," + res2[k]




# # TEST
# n1 = get_vals_at_time(29.1)
# n2 = get_vals_at_time(42.1)
# f1 = get_vals_at_time(35.1)
# f2 = get_vals_at_time(48.1)

# print "n1-n2"
# print n1["688"]
# print n2["688"]

# print "f1-f2"
# print f1["688"]
# print f2["688"]

# a = comp_state_eq(n1, n2)
# b = comp_state_eq(f1, f2)
# c = comp_state_dif(a, b)
