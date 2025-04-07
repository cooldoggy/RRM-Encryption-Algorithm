import random
def meshmaker(inputstring):
    return [list(inputstring[i*8:(i+1)*8]) for i in range(8)]
def xorutil(a,b):
    return (int(hex(ord(str(a)[:1])^int(b,16)),16))

def substitutionboxencrypt(a,b):
    encrypttable=list([["97", "96", "42", "20", "36", "78", "16", "63", "11", "08"],
                ["13", "30", "68", "09", "95", "89", "05", "99", "65", "35"],
                ["01", "44", "72", "46", "04", "71", "02", "22", "29", "90"],
                ["61", "81", "62", "21", "34", "32", "73", "53", "45", "80"],
                ["98", "49", "93", "41", "60", "64", "70", "47", "40", "69"],
                ["87", "54", "24", "84", "18", "77", "66", "26", "38", "85"],
                ["59", "43", "48", "91", "92", "00", "14", "58", "03", "75"],
                ["28", "67", "17", "15", "83", "12", "94", "23", "39", "86"],
                ["52", "27", "37", "88", "82", "51", "06", "55", "10", "33"],
                ["57", "07", "76", "50", "56", "31", "25", "74", "19", "79"]])
    return(encrypttable[a][b])

def subsitutionboxdecrypt(a,b):
    decrypttable=list([['65', '20', '26', '68', '24', '16', '86', '91', '09', '13'], 
                       ['88', '08', '75', '10', '66', '73', '06', '72', '54', '98'], 
                       ['03', '33', '27', '77', '52', '96', '57', '81', '70', '28'], 
                       ['11', '95', '35', '89', '34', '19', '04', '82', '58', '78'], 
                       ['48', '43', '02', '61', '21', '38', '23', '47', '62', '41'], 
                       ['93', '85', '80', '37', '51', '87', '94', '90', '67', '60'], 
                       ['44', '30', '32', '07', '45', '18', '56', '71', '12', '49'], 
                       ['46', '25', '22', '36', '97', '69', '92', '55', '05', '99'], 
                       ['39', '31', '84', '74', '53', '59', '79', '50', '83', '15'], 
                       ['29', '63', '64', '42', '76', '14', '01', '00', '40', '17']])
    return(decrypttable[a][b])
