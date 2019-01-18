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

# def open_dbc(dir_name, filename):
#     dbc_file_in = read_file(dir_name, filename)

def open_data(dir_name, filename):
    # data_file_in = read_file(dir_name, filename)

    # with open(filename) as f:
    #   txt = f.read().split("\n")
    #   print txt
    #   print "-----\n"

    addrs = {}

    with open(filename) as f:
        rdr = csv.reader(f, delimiter=',')
        cnt = 0
        for r in rdr:
            if cnt == 0:
                print r
                cnt += 1
            else:
                # print r[0], r[1], r[2], r[3]
                addrs[r[1]] = r[3]
                # msgs[float(r[0])] = addrs
                msgs.append((float(r[0]), addrs.copy()))
                cnt += 1

            if (cnt % 5000) == 0:
                print cnt

            if cnt > 465000:
                break

        # print msgs[100]
        # print " "
        # print msgs[1000]
        # print " "
        # print msgs[1000][0]

        print msgs[100][1]
        print " "
        print len(msgs)
        print " "

def get_last_addr_vals(time):
    for m in msgs:
        if m[0] >= time:
            break
    return m[1]

def comp_state_dif1(time1, time2):
    # print msgs[0][0]
    for m1 in msgs:
        if m1[0] >= time1:
            break
        # print m[0]

    # print "-------------- MESSAGE 1:"
    # print m1

    for m2 in msgs:
        if m2[0] >= time2:
            break
        # print m[0]

    # print " "
    # print "-------------- MESSAGE 2:"
    # print m2

    # print cmp(m1[1], m2[1])

    for addr in m2[1].keys():
        # print addr
        if m1[1].has_key(addr):
            # print str(addr) + "  m1: " + str(m1[1].get(addr)) + "  m2: " + str(m2[1].get(addr))
            df = False
            # if (int(m1[1].get(addr),16) & 0xff00000000000000) != (int(m2[1].get(addr),16) & 0xff00000000000000):
            #     df = True
            if (int(m1[1].get(addr),16) & 0x00ff000000000000) != (int(m2[1].get(addr),16) & 0x00ff000000000000):
                df = True
            if (int(m1[1].get(addr),16) & 0x0000ff0000000000) != (int(m2[1].get(addr),16) & 0x0000ff0000000000):
                df = True
            if (int(m1[1].get(addr),16) & 0x000000ff00000000) != (int(m2[1].get(addr),16) & 0x000000ff00000000):
                df = True
            if (int(m1[1].get(addr),16) & 0x00000000ff000000) != (int(m2[1].get(addr),16) & 0x00000000ff000000):
                df = True
            if (int(m1[1].get(addr),16) & 0x0000000000ff0000) != (int(m2[1].get(addr),16) & 0x0000000000ff0000):
                df = True
            if (int(m1[1].get(addr),16) & 0x000000000000ff00) != (int(m2[1].get(addr),16) & 0x000000000000ff00):
                df = True
            if (int(m1[1].get(addr),16) & 0x00000000000000ff) != (int(m2[1].get(addr),16) & 0x00000000000000ff):
                df = True
            if df:
                 print str(addr) + "  m1: " + str(m1[1].get(addr)) + "  m2: " + str(m2[1].get(addr))

        else:
            print addr + " NOT FOUND"



def comp_state_dif2(time1, time2):
    ret = []

    m1 = get_last_addr_vals(time1)
    m2 = get_last_addr_vals(time2)

    print "-------------- MESSAGE 1:"
    print m1
    print ""
    print ""
    # print "-------------- MESSAGE 2:"
    # print m2

    
    for addr in m2.keys():
        # print addr
        addrs = {}
        if m1.has_key(addr):
            x = logical_xor(m1.get(addr), m2.get(addr))

            if int(x, 16) > 0:
                # print x
                # print str(addr) + "  m1: " + str(m1.get(addr)) + "  m2: " + str(m2.get(addr))
                addrs[addr] = x
                ret.append(addrs.copy())
        else:
            print addr + " NOT FOUND"
    return ret

def comp_state_eq2(time1, time2):
    ret = []

    for m1 in msgs:
        if m1[0] >= time1:
            break

    # print "-------------- MESSAGE 1:"
    # print m1

    for m2 in msgs:
        if m2[0] >= time2:
            break

    # print "-------------- MESSAGE 2:"
    # print m2

    addrs = {}
    for addr in m2[1].keys():
        # print addr
        if m1[1].has_key(addr):
            x = logical_and(m1[1].get(addr), m2[1].get(addr))

            if int(x, 16) > 0:
                # print x
                # print str(addr) + "  m1: " + str(m1[1].get(addr)) + "  m2: " + str(m2[1].get(addr))
                addrs[addr] = x
                ret.append(addrs.copy())

        else:
            print addr + " NOT FOUND"
    return ret

def comp_state_dif(s1, s2):
    ret = {}

    # print s1
    # print s2
    
    for addr in s2.keys():
        addrs = {}
        if s1.has_key(addr):
            x = logical_and(s1.get(addr), s2.get(addr))

            if int(x, 16) > 0:
                # print x
                # print str(addr) + "  s1: " + str(s1[1].get(addr)) + "  s2: " + str(s2[1].get(addr))
                addrs[addr] = x
                ret[addr] = x
                # ret.append(addrs.copy())

        # else:
        #     print addr + " NOT FOUND"
    return ret

def comp_state_eq(s1, s2):
    ret = {}

    # print s1
    # print s2
    
    for addr in s2.keys():
        addrs = {}
        if s1.has_key(addr):
            x = logical_and(s1.get(addr), s2.get(addr))

            if int(x, 16) > 0:
                # print x
                # print str(addr) + "  s1: " + str(s1[1].get(addr)) + "  s2: " + str(s2[1].get(addr))
                addrs[addr] = x
                ret[addr] = x
                # ret.append(addrs.copy())

        # else:
        #     print addr + " NOT FOUND"
    return ret


open_data(cur_path, "test.csv")

rets = []

# print comp_state_dif(get_last_addr_vals(29.1), get_last_addr_vals(35.1))
print ""
print ""
    
rets.append(comp_state_dif(get_last_addr_vals(29.1), get_last_addr_vals(35.1)))
rets.append(comp_state_dif(get_last_addr_vals(35.1), get_last_addr_vals(42.1)))
rets.append(comp_state_dif(get_last_addr_vals(42.1), get_last_addr_vals(48.1)))
rets.append(comp_state_eq(get_last_addr_vals(29.1), get_last_addr_vals(42.1)))
rets.append(comp_state_eq(get_last_addr_vals(35.1), get_last_addr_vals(48.1)))

print "a"
print comp_state_eq(comp_state_eq(comp_state_eq(rets[0], rets[1]), comp_state_eq(rets[2], rets[3])), rets[4])
print "b"

# rets.append(comp_state_dif(29.1, 35.1))
# rets.append(comp_state_dif(35.1, 42.1))
# rets.append(comp_state_dif(42.1, 48.1))
# rets.append(comp_state_eq(29.1, 42.1))
# rets.append(comp_state_eq(35.1, 48.1))


known_on = [29, 42]
known_off = [35, 48]

# match_state(known_on, known_off)

# 29
# 35
# 42
# 48

# {'1304': '31D880000000080', '1305': '32A200000000081', '1306': '32E380000000080', '1307': '330180000000081', '1300': '302800000000080', '1301': '300D80000000080', '1302': '315B80000000081', '1303': '318700000000081', '127': '53', '1308': '33EF00000000081', '1309': '34AB00000000081', '1265': '620000000000', '544': '4822000810C14', '2017': '319020DAAAAAAAA', '2016': '319020DAAAAAAAA', '2012': '2105600000000000', '1317': '3FFF80000000081', '1316': '3FFF80000000081', '1315': '3FFF80000000081', '1314': '3FFF80000000081', '1313': '3FFF80000000081', '1312': '3FFF80000000081', '1311': '316F80000000081', '1310': '306F80000000081', '1151': 'FFFA00000000', '1319': '3FFF80000000081', '1318': '3FFF80000000081', '1491': 'F00000000000000', '1952': '319020CAAAAAAAA', '1419': '100040000000020', '1415': '0C', '1322': '3FFF80000000081', '1323': '3FFF80000000081', '593': 'C0020000000000', '1321': '3FFF80000000081', '1326': '300000000000000', '1327': '300000000000000', '1324': '3FFF80000000081', '1325': '300000000000000', '688': '10000702000000', '1328': '300000000000000', '1329': '300000000000000', '809': 'B0810C10200014', '273': '4561FF5312000C', '274': 'FF300000FF120000', '275': '2000800000018C', '399': 'FA20000000400020', '832': '400002414001418', '790': '4520000020000078', '897': '8000000000011005', '1254': '4880000089898880', '1255': '2100000700800000', '1253': '8032000648830000', '916': '1080', '1407': '6800000200000000', '1339': '300000000000000', '1338': '300000000000000', '1335': '300000000000000', '1334': '300000000000000', '1337': '300000000000000', '1336': '300000000000000', '1331': '300000000000000', '1330': '300000000000000', '1333': '300000000000000', '1332': '300000000000000', '902': '1000020000800000', '903': '2000002000880000', '909': '480003000008', '1530': '10000', '512': 'AF0000000000', '1348': 'FF77FFFF00000000', '1349': 'E8000088000000BC', '339': '10FF00FF000E', '1340': '300000000000000', '1341': '300000000000000', '1342': '300000000000000', '1343': '300000000000000', '1344': '300000000000000', '1345': '300000000000000', '1346': '200000000000000', '1347': '200000000000000', '64': '110400000000', '66': 'FF14FF1400000000', '67': 'D10000203000040', '68': '20000FF55000000', '1904': '4008010000000000', '1902': 'C002100C1EF20D00', '1903': 'C302000000000000', '1900': '909F8F1442D70100', '1901': 'CE03000000000010', '1427': 'FFFFFFFF0000', '1988': '319020CAAAAAAAA', '356': '8040400000000', '784': '60000000007FBC00', '1216': '2FD000000000000', '785': '80000000000', '1353': '2844E00401D645B', '1351': '7438CD002F00', '1040': '1000000', '1996': '759028956118708', '1186': '100000000000000', '2024': '35902FFAAAAAAAA', '2025': '35902CFAAAAAAAA', '1456': '1232000000000000', '1487': '3C08000000808000', '1486': '1002F01006026', '884': '2000000000000008', '1168': '82100003C00', '608': '20203000C80024', '1899': '4BF5070600', '1894': '4A0F0000000010', '1896': '40C1000000000010', '1365': 'A0000000188080AF', '1057': 'FFE37F0010', '1191': '100000000000000', '1960': '3590209AAAAAAAA', '1470': '40000FF00000000', '1298': '305500000000080', '1299': '305080000000081', '1440': '400000029000000', '1292': '2000000000080', '1293': '300600000000080', '1290': '302000000000081', '1291': '302100000000080', '1296': '300000000000080', '1297': '300800000000080', '1294': '300200000000080', '1295': '300000000000080', '2004': '30080AAAAAAAAAAA', '1170': '802F9C805E88', '899': '102B045C40000008', '1285': '3FFF80000000000', '1284': '3FFF80000000000', '1287': '100000000', '1286': '3FFF80000000000', '1281': '302000000000000', '1280': '300000000000300', '1283': '302280000000000', '1282': '306180000000000', '1289': '3000801000000C0', '1288': '3000400000000E0', '1366': '217E000000220200', '1367': '80000010100600', '2000': '319020CAAAAAAAA', '2001': '319020CAAAAAAAA', '1363': '51060100C000', '1320': '3FFF80000000081', '2008': '3590289AAAAAAAA', '2009': '359020CAAAAAAAA', '1369': '40'}
