#! /usr/bin/python
#-*-encoding : utf-8-*-
from decimal import *
import threading
import math
import time
f=open('function.txt','r')
y=f.read()
y=y.replace(' ','')
y=y.replace('\n','')
e=Decimal(str(math.exp(1)))
pi=Decimal(str(math.pi))
sin=math.sin
cos=math.cos
tan=math.tan
c=Decimal('180')
def rad(x):
    return x*pi/c
def f(x):
    return eval(y)
def getRootFromf(b):
    n=Decimal('0')
    h=Decimal(b)
    t=abs(h)
    while(True):
        check=Decimal(str(f(n)*f(n+h)))
        if(check<0):
            if(h==Decimal(b)*Decimal('0.0000001')):
                print('%s~%s에 근이 적어도 하나 존재합니다.'%(n,(n+h)))
                n=Decimal(n+h)
                h=Decimal(b)
                continue
            h*=t
            continue
        if(check==0):
            if(f(n)==0):
                print('%s'%n)
                n=Decimal(n+h)
                h=Decimal(b)
                continue
                print('%s'%(n+h))
                n=Decimal(n+2*h)
                h=Decimal(b)
                continue
        n=n+h
plus = threading.Thread(target=getRootFromf, args=('0.1',),daemon=True)
minus = threading.Thread(target=getRootFromf, args=('-0.1',),daemon=True)
plus.start()
minus.start()
while(True):
    time.sleep(1)
