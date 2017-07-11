import datetime
import time
import os
import random

global tab
tab = '\t'

sdsd = ''

class FlowSheet:
    def _init(self, mdn, msid, upFlowCount, downFlowCount):
        self._mdn = mdn
        self._msid = msid
        self._upFlowCount = upFlowCount
        self._downFlowCount = downFlowCount

    def setStreamId(self,streamId):
        self._streamId = streamId

    def getRandomId(self):
        chars = 'AaBbCcj78KkLlMmN_nOoPpQ+qR1234rSsTtUuVvDdEe/FfGgHhIiJWw-XxYyZz0569'
        a = []
        count = 0
        while count < 8:
            a.append(chars[random.randint(0, 65)])
            count = count + 1
        out = ''.join(a)
        return out

    def getflowSheet(self):
        return str(self._streamId) + '\t' + tab*3 + str(self._mdn) + '\t' + str(self._msid) + '\t' + tab*6 + self.getRandomId() +\
               tab + self.getRandomId() + tab*21 + str(self._upFlowCount) + '\t' + str(self._downFlowCount) + '\t\t' + str(int(time.time())) + '\t' + tab*29 + '\n'

#获取文件名
currentDate = datetime.datetime.now()
fileName = "AAA_99_" + currentDate.strftime('%Y%m%d') + "_" + currentDate.strftime('%H%M') + "_0000.TXT"
#写文件
fileHandle = open(fileName,'w+')
fileHead = "000000"+currentDate.strftime('%Y%m%d')+currentDate.strftime('%Y%m%d')+currentDate.strftime('%H%M%S')+\
           currentDate.strftime('%Y%m%d')+currentDate.strftime('%H%M%S')+"0000000000"+"\n"
fileHandle.write(fileHead)
recordCount = 0
while True:
    line = input("please inpt user data:")
    recordCount = recordCount + 1
    if line:
        inData = line.split()
        flowSheet = FlowSheet()
        flowSheet._init(inData[0],inData[1],inData[2],inData[3])
        flowSheet.setStreamId(recordCount)
        fileHandle.write(flowSheet.getflowSheet())
        #更新文件头
        currentDate = datetime.datetime.now()
        fileHandle.seek(28, 0)
        fileHandle.write(currentDate.strftime('%Y%m%d'))
        fileHandle.write(currentDate.strftime('%H%M%S'))
        fileHandle.write(str(recordCount).zfill(10))
        fileHandle.seek(0, os.SEEK_END)
    else:
        break
#关闭文件
fileHandle.close()

