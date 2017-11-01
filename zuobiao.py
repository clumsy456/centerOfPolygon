f = open('zuobiao.txt')

zuobiaoList = list()
num = 0
for line in f.readlines():
	lineInfo = line.split(',')
	Xaxis = float(lineInfo[0])
	Yaxis = float(lineInfo[1])
	zuobiaoList.append([Xaxis, Yaxis])
	num = num + 1
num = num - 1

dingdian = zuobiaoList[0]
zongFenziX = 0
zongFenziY = 0
zongFenmu = 0
for i in range(1,num-1):
	xia = zuobiaoList[i]
	shang = zuobiaoList[i+1]
	sanjiaoZhixin = [(dingdian[0]+xia[0]+shang[0])/3, (dingdian[1]+xia[1]+shang[1])/3]
	xiaXiangliang = [xia[0]-dingdian[0], xia[1]-dingdian[1]]
	shangXiangliang = [shang[0]-dingdian[0], shang[1]-dingdian[1]]
	sanjiaoMianji = (xiaXiangliang[0]*shangXiangliang[1]-xiaXiangliang[1]*shangXiangliang[0])/2
	zongFenziX += sanjiaoZhixin[0]*sanjiaoMianji
	zongFenziY += sanjiaoZhixin[1]*sanjiaoMianji
	zongFenmu += sanjiaoMianji

zuobiaoX = round(zongFenziX/zongFenmu, 4)
zuobiaoY = round(zongFenziY/zongFenmu, 4)
print([zuobiaoX,zuobiaoY])