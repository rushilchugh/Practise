def get_other(a):
    ascii_char = chr(ord(a) + 2)
    if (a == 'y'):  return 'a'
    if (a == 'z'):  return 'b'
    return ascii_char

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

for i in string.split(" "):
	for j in i:
		if j.isalpha():
			print(get_other(j) , end = '')
	print('' , end = " ")

