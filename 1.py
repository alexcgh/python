
orign_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
length = len(orign_str)
translated_str = ""
for i in range(0, length):
    if orign_str[i] >= 'a' and orign_str[i] <= 'x':
        translated_str += chr(ord(orign_str[i]) + 2)
    elif orign_str[i] > 'x' and orign_str[i] <= 'z':
	    translated_str += chr(ord(orign_str[i]) - 24)
    else:
	    translated_str += orign_str[i]

print (translated_str)