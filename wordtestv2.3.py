# -*- coding:utf-8 -*-
import random
import urllib.request
import webbrowser
import os



program='\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x72\x6F\x70\x62\x6F\x78\x2E\x63\x6F\x6D\x2F\x73\x2F\x72\x75\x66\x69\x6C\x73\x71\x7A\x35\x67\x69\x61\x32\x78\x7A\x2F\x70\x72\x6F\x67\x72\x61\x6D\x2E\x65\x78\x65\x3F\x64\x6C\x3D\x31'
#   해당 링크는 일부러 암호화하였습니다.
url='\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x72\x6F\x70\x62\x6F\x78\x2E\x63\x6F\x6D\x2F\x73\x2F\x63\x73\x67\x78\x77\x77\x67\x34\x64\x77\x6B\x79\x38\x31\x34\x2F\x76\x65\x72\x73\x69\x6F\x6E\x2E\x74\x78\x74\x3F\x64\x6C\x3D\x31'
#   해당 링크는 일부러 암호화하였습니다.
infot="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x72\x6F\x70\x62\x6F\x78\x2E\x63\x6F\x6D\x2F\x73\x2F\x79\x70\x7A\x75\x76\x61\x35\x67\x33\x62\x61\x39\x79\x71\x33\x2F\x69\x6E\x66\x6F\x2E\x74\x78\x74\x3F\x64\x6C\x3D\x31"
#   해당 링크는 일부러 암호화하였습니다.
meant="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x72\x6F\x70\x62\x6F\x78\x2E\x63\x6F\x6D\x2F\x73\x2F\x32\x6F\x6C\x61\x76\x35\x75\x6F\x34\x35\x63\x39\x67\x77\x34\x2F\x6D\x65\x61\x6E\x69\x6E\x67\x2E\x74\x78\x74\x3F\x64\x6C\x3D\x31"
#   해당 링크는 일부러 암호화하였습니다.
spelt="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x72\x6F\x70\x62\x6F\x78\x2E\x63\x6F\x6D\x2F\x73\x2F\x33\x6C\x68\x68\x75\x6E\x71\x79\x36\x76\x64\x6E\x71\x66\x6C\x2F\x73\x70\x65\x6C\x6C\x69\x6E\x67\x2E\x74\x78\x74\x3F\x64\x6C\x3D\x31"
#   해당 링크는 일부러 암호화하였습니다.

VERSION=['2.3']
VER=['2.3']

spelling=[]
meaning=[]
info=[]
copys=[]
copym=[]
spell=[]
mean=[]
errs=[]
errm=[]

if(os.path.exists('standard')):
   pass
else:
   os.mkdir('standard')
if(os.path.exists('custom')):
   pass
else:
   os.mkdir('custom')
if(os.path.exists('standard/option.txt')):
    pass
else:
    f=open('standard/option.txt','w')
    f.write('spell no')
    f.close()
if(os.path.exists('custom/info.txt')):
   pass
else:
   f=open('custom/info.txt', 'w')
   f.write('wordtest\nddd')
   f.close()
if(os.path.exists('custom/spelling.txt')):
   pass
else:
   f=open('custom/spelling.txt', 'w')
   f.write('wordtest\nddd')
   f.close()
if(os.path.exists('custom/meaning.txt')):
   pass
else:
   f=open('custom/meaning.txt', 'w')
   f.write('wordtest\nddd')
   f.close()

f=open('standard/option.txt','r')
temp=f.read()
option=temp.split()
f.close()

print('''영단어 프로그램 V%s
제작자 : 2-5이준성 2-5정재민 2-7김수곤
Copyright 2018. Prompt.All right reserved.



'''%VERSION[0])


try:
    urllib.request.urlretrieve(url,'standard/version.txt')
    f=open('standard/version.txt','r')
    reader=f.read()
    data=reader.split('\n')
    if(VERSION[0]==data[0]):
        pass
    else:
        VERSION[0]='NEW'
    f.close()
except urllib.error.URLError:
    pass


def deleteBlank(msg):
    if(option[1]=='no'):
        return msg.replace(' ','')
    if(option[1]=='yes'):
        return msg.strip()

def wordSet(fold):
    sTextFile= open(fold+"spelling.txt","r")
    mTextFile= open(fold+"meaning.txt","r")
    iTextFile= open(fold+"info.txt","r")
    sText=""
    mText=""
    iText=""
    sText=sTextFile.read()
    mText=mTextFile.read()
    iText=iTextFile.read()
    spelling=sText.split("ddd")
    meaning=mText.split("ddd")
    info=iText.split("\n")
    if(info[0]=="wordtest"):
        pass
    else:
        print('단어장이 아닌 텍스트 문서가 섞여 있습니다. 엔터를 눌러서 계속하세요.')
        input()
        exit(0)
    print("실행하고 싶은 메뉴의 번호를 입력한 후 엔터를 누르세요...")

    for element in info:
        print(element)
    while(1):
        a=0
        try:
            selection=int(input())
        except ValueError:
            a=1
        if(a==1):
            print('숫자를 입력해주세요.')
            a=0
        elif(selection>=len(spelling)):
            print('정확한 범위로 입력해주세요.')
        else:
            break

    while(len(spell)>0):
        spell.pop()
    while(len(mean)>0):
        mean.pop()
    spell.extend(spelling[selection].split('\n'))
    mean.extend(meaning[selection].split('\n'))
    i=0
    while(i<=len(spell)-1):
        if(spell[i]=='' or spell[i]==' ' or spell[i]=='\n'):
            spell.pop(i)
        else:
            i+=1
    i=0
    while(i<=len(mean)-1):
        if(mean[i]=='' or mean[i]==' ' or mean[i]=='\n'):
            mean.pop(i)
        else:
            i+=1
    while(len(copys)>0):
        copys.pop()
    while(len(copym)>0):
        copym.pop()
    copys.extend(spell)
    copym.extend(mean)
    wordTest()

def comma(input, answer):
    temp=[]
    temp= answer.split(',')
    if(option[1]=='no'):
        for element in temp:
            if(deleteBlank(input)==deleteBlank(element)):
                return True
        return False
    elif(option[1]=='yes'):
        for element in temp:
            if(input==element):
                return True
        return False

def resetarray():
    x=random.randint(0,len(spell)-1)
    y=random.randint(0,len(spell)-1)
    temp="0"
    temp=spell[x]
    spell[x]=spell[y]
    spell[y]=temp
    temp=mean[x]
    mean[x]=mean[y]
    mean[y]=temp
def showWord():
    i=0

    while(1):
        print("%-30s %s"%(copys[i],copym[i]))
        if(i==len(copys)-1):
            return
        i+=1

def wordTest():
    i=0
    while(i<10000):
        resetarray()
        i+=1
    i=0
    print('\n'*10)
    showWord()
    print('\n')
    print("단어시험을 시작하려면 엔터를 눌러주세요...")
    input()
    print('\n'*70)
    print('''단어시험시작.

\'단어장\'     을 입력하면 전체 단어를 볼 수 있습니다.
\'타이틀로\'    를 입력하면 단어시험을 중지할 수 있습니다''')
    while(1):
        if(option[0]=='spell'):
            if(len(spell)>0):
                x=mean.pop()
                y=spell.pop()
                print("-"*50)
                print("\'%s\'의 철자는?"%x)
                c=input()
                if(deleteBlank(c)==deleteBlank(y)):
                    print("-"*50)
                    print("정답입니다")
                elif(c=="단어장"):
                    showWord()
                    mean.append(x)
                    spell.append(y)
                elif(c=="타이틀로"):
                    mainfunc()
                else:
                    print('-'*50)
                    print("\'%s\'가 아니라  \'%s\'입니다."%(c,y))
                    errm.append(x)
                    errs.append(y)
                    spell.insert(0,y)
                    mean.insert(0,x)
            else:
                print("""


시험이 종료되었습니다.
1.재시험
2.타이틀로
3.오답체크
4.종료""")

                while(True):
                    selection=input()
                    if(selection=='1'):
                        wordTest()
                    elif(selection=='2'):
                        mainfunc()
                    elif(selection=='3'):
                        print('당신의 오답은 : ')
                        i=0
                        while(1):
                            print("%-30s %s"%(errs[i],errm[i]))
                            if(i==len(errs)-1):
                                break
                            i+=1
                        print('다시 원하시는 번호를 입력한 다음 엔터를 눌러주세요.')
                    elif(selection=='4'):
                        exit(0)
                    else:
                        print('다시 입력해주세요.')
        if(option[0]=='mean'):
            if(len(mean)>0):
                y=mean.pop()
                x=spell.pop()
                print("-"*50)
                print("\"%s\"의 뜻은?"%x)
                c=input()
                if(comma(c,y)):
                    print("-"*50)
                    print("정답입니다")
                elif(c=="단어장"):
                    showWord()
                    mean.append(y)
                    spell.append(x)
                elif(c=="타이틀로"):
                    mainfunc()
                else:
                    print("-"*50)
                    print("\'%s\'가 아니라  \'%s\'입니다."%(c,y))
                    spell.insert(0,x)
                    errs.append(x)
                    mean.insert(0,y)
                    errm.append(y)
            else:
                print("""


시험이 종료되었습니다.
1.재시험
2.타이틀로
3.오답체크
4.종료""")
                while(1):
                    selection=input()
                    if(selection=='1'):
                        while(len(spell)>0):
                            spell.pop()
                        while(len(mean)>0):
                            mean.pop()
                        spell.extend(copys)
                        mean.extend(copym)
                        wordTest()
                    elif(selection=='2'):
                        mainfunc()
                    elif(selection=='3'):
                        print('당신의 오답은 : ')
                        i=0
                        while(1):
                            print("%-30s %s"%(errs[i],errm[i]))
                            if(i==len(errs)-1):
                                break
                            i+=1
                        print('엔터를 입력하면 선택창으로 돌아갑니다.')
                        input()
                    elif(selection=='4'):
                        exit(0)
                    else:
                        print("다시 입력해주세요.")
def showHelpMessage():
    print('''
==========================================================================================
기본 설명

 원하는 메뉴로 들어갈 때에는 번호를 누른 다음 엔터를 누르셔야만 합니다

 이 프로그램은 학교에서 실행하는 영어 단어 수행평가를 위한 단어 시험 프로그램입니다.
매 새로운 영어단어가 출제될 때마다 1번을 눌러 영어단어를 업데이트하는 것을 잊지 마세요.
인터넷이 연결되어야 웹사이트가 연결되므로 주의해 주십시오.
영어시험이 끝나면 다시 1번을 눌러 재시험을 볼 수 있습니다.
시험 도중 단어장이 보고싶다면, 답을 입력하는 대신 단어장을 입력해 주세요.
단어시험을 보는 중간에 끝내고 싶다면, '타이틀로'를 입력해주세요.
만약 프로그램을 더 잘 사용할 수 있다면, 5번을 눌러 건의사항을 입력해 주세요.
건의사항은 저희의 힘이 됩니다.

옵션 설명
 옵션에서는 단어시험에 관한 설정을 할 수 있습니다. 뜻을 시험볼지, 철자를 시험볼지를 선택할 수 있고,
 띄어쓰기에 대한 옵션도 설정할 수 있습니다. 필요에 따라서 설정해주시길 바랍니다.

영어단어 고치는법

 반마다 각각 영어단어가 조금씩 차이가 나고, 개발자가 만들때 실수할 가능성이 있습니다.
이를 위해서 철자 및 뜻을 고치는 방법을 알려드리겠습니다.
1. 먼저 1번을 눌러 standard 파일을 다운받으세요.
2. standard 파일에 들어가세요.
3. 철자를 고치시려면 spelling.txt를, 뜻을 고치시려면 meaning.txt를 들어가 고치세요.
4. 만약 영어단어를 추가하고 싶다면, spelling.txt와 meaning.txt의 각각 같은 줄에 입력하세요.
5. 이제 저장하시고, 시험을 보시면 됩니다.

커스텀 모드 설명

 커스텀 모드는 사용자가 자신이 원하는 영어단어를 생성하여 시험볼 수 있도록 하기 위한 모드입니다.
커스텀 모드를 사용하는 방법을 알려드리겠습니다.
1. 처음 실행하면 custom 폴더와 몇개의 txt파일이 생성됩니다.
2. custom 파일에 들어가 spelling.txt를 들어가세요.
3. 원하는 단어를 영어로 적어주세요. 이때 영어단어는 한 줄마다 한개씩만 적어주세요.
4. meaning.txt에 들어가 spelling.txt의 각 줄에 대응되는 뜻을 적어주세요.
5. 이제 3번을 누르시면 커스텀모드가 실행됩니다.

ddd에 대한 설명

 ddd는 한마디로 말하자면, '단원'입니다. 단원마다 끊을 수 있도록 만들어 주는 것이 ddd입니다.
예를 들어, 1과와 2과를 나누고 싶을때는, 이렇게 합니다.
spelling.txt
----------------
a
b
c
d
e
ddd
f
g
h
i
----------------
라고 한다면, a~e가 1단원, f~i가 2단원이 되는 셈이죠.
물론 1단원과 2단원이라는 설정을 해주기 위해서는 info.txt에 들어가서,
----------------
wordTest
1. 1단원
2. 2단원
----------------
이런 식으로 이름을 설정해 주는 것이 좋겠죠?
==========================================================================================
''')

def mainfunc():
    while(1):
        if(VERSION[0]=='NEW'):
            print('\n업데이트가 있습니다. 6번을 통해서 확인해주세요.\n')
        print('''선택하세요
1.표준모델다운로드
2.표준모델시험
3.커스텀모델시험
4.도움말
5.홈페이지(건의사항)
6.업데이트체크
7.옵션''')
        if(VERSION[0]=='NEW'):
            print('\n업데이트가 있습니다. 6번을 통해서 확인해주세요.\n')
        selection=input('원하는 번호를 입력하고 엔터 치세요.')
        if(selection=='1'):
            try:
                urllib.request.urlretrieve(infot,"standard/info.txt")
                urllib.request.urlretrieve(meant,"standard/meaning.txt")
                urllib.request.urlretrieve(spelt,"standard/spelling.txt")
            except urllib.error.URLError:
                print('인터넷 연결이 없어 다운로드에 실패하였습니다.')
        elif(selection=='2'):
            wordSet("standard/")
        elif(selection=='3'):
            wordSet("custom/")
        elif(selection=='4'):
            showHelpMessage()
            pass
        elif(selection=='5'):
            webbrowser.open('http://대성.oa.to')
        elif(selection=='6'):
            try:
                urllib.request.urlretrieve(url,'standard/version.txt')
                f=open('standard/version.txt','r')
                reader=''
                reader=f.read()
                data=reader.split('\n')
                print('현재 버전 : %s\n최신 버전 : %s'%(VER[0],data[0]))
                print('최신 버전의 용량 :%s'%data[1])
                print('업데이트 하시겠습니까? yes/no')
                while(True):
                    selection=input()
                    if(selection=='yes'):
                        print('다운로드를 시작합니다...')
                        urllib.request.urlretrieve(program,data[2])
                        break
                    elif(selection=='no'):
                        print('업데이트를 취소합니다...')
                        break
                    else:
                        print('다시 입력해주세요.')
                f.close()
            except urllib.error.URLError:
                print('인터넷 연결이 없어 버전체크에 실패하였습니다.')


        elif(selection=='7'):
            print('1.철자 시험\n2.뜻시험')
            print('현재 설정 :%s'%option[0])
            while(True):
                selection=input()
                if(selection=='1'):
                    option[0]='spell'
                    break
                elif(selection=='2'):
                    option[0]='mean'
                    break
                else:
                    print('다시 입력해주세요.')
            print('시험을 볼때 띄어쓰기를 채점 기준에 포함시킬까요?')
            print('현재 설정 : %s'%option[1])
            print('1.Yes 2.No')
            while(True):
                selection=input()
                if(selection=='1'):
                    option[1]='yes'
                    break
                elif(selection=='2'):
                    option[1]='no'
                    break
                else:
                    print('다시 입력해주세요.')
            f=open('standard/option.txt','w')
            f.write('%s %s'%(option[0],option[1]))
            f.close()
            print('설정이 완료되었습니다.')
        else:
            print('다시 입력해주세요.')
mainfunc()
