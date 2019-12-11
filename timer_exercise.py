import time

class Timer:
    '''
    timer.start()
    开始计算时间
    timer.end()
    计算出相隔时间
    停止计时
    '''
    
    def start(self):
        self.a=time.localtime()
        print('计时开始')
    def end(self):
        self.b=time.localtime()
        print(self.timeSub())
        print('停止计时')
    def timeSub(self):
        self.year=self.b[0]-self.a[0]
        self.month=self.b[1]-self.a[1] 
        self.day=self.b[2]-self.a[2]
        self.hour=self.b[3]-self.a[3]
        self.min=self.b[4]-self.a[4]
        self.second=self.b[5]-self.a[5]
        return (self.year,self.month,self.day,self.hour,self.min,self.second)

print(type(time.localtime()))
print(list(time.localtime()))
t = Timer()
t.start()
time.sleep(1)
t.end()