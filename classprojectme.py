def converter(h,m,s):
        dlist = []
        dlist.extend([str(h),str(m),str(s)])
        for x in range(len(dlist)):
            if len(dlist[x]) == 1:
                dlist[x] = "0" + dlist[x]
        dlist = ":".join(dlist)
        return dlist

class CTimer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0 ):
        self.__ctimer = []
        self.__ctimer.extend([hours,minutes,seconds])
        self.__ctimer = converter(self.__ctimer[0],self.__ctimer[1],self.__ctimer[2])
    
    def __str__(self):
        return self.__ctimer

    def next_second(self):
        ndata = self.__ctimer.split(":")
        ndata[0] = int(ndata[0])
        ndata[1] = int(ndata[1])
        ndata[2] = int(ndata[2])

        ndata[-1] = ndata[-1] + 1
        if ndata[-1] == 60:
            ndata[-1] = 00
            ndata[-2] = ndata[-2] + 1
            if ndata[-2] == 60:
                ndata[-2]=00
                ndata[-3] = ndata[-3]+1
                if ndata[-3]==24:
                    ndata[-3] = 00
        
        self.__ctimer = converter(ndata[0],ndata[1],ndata[2])
        return self.__ctimer

    def prev_second(self):
        ndata = self.__ctimer.split(":")
        ndata[0] = int(ndata[0])
        ndata[1] = int(ndata[1])
        ndata[2] = int(ndata[2])

        ndata[-1] = ndata[-1] - 1
        if ndata[-1] == -1:
            ndata[-1] = 59
            ndata[-2] = ndata[-2] -1
            if ndata[-2] == -1:
                ndata[-2] = 59
                ndata [-3] = ndata[-3] -1
                if ndata[-3] == -1:
                    ndata[-3] = 23
        
        self.__ctimer = converter(ndata[0],ndata[1],ndata[2])
        return self.__ctimer


timer = CTimer(3, 2, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)


