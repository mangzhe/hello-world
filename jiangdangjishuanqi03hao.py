from tkinter import *
windos=Tk()
windos.title('简单计算器')
windos.geometry('350x260+400+200')
windos.config(bg='#181d4b')
#不允许改变窗口大小--copy
windos.resizable(False,False)
#----输出框---------------------------------------------------------------
var_1=StringVar()
#var_time=StringVar()
var_1.set('0')
#var_time.set('0')
Label(windos,bg='dimgray',fg='lime',width='50',textvariable=var_1,anchor='w').place(x=0, y=0)
#--------显示当前的时间-------------------------------------------------------没成功
Label(windos,text='这是个功能不多的计算器半成品',width='50',bg='black',fg='#1d953f').place(x=0,y=20)

#-------定义函数------------
var_2=StringVar()
def put_num(n):
    t=var_1.get()
    if t=='0':
        var_1.set(n)
    else:
        var_2=t+n
        var_1.set(var_2)
def clear():
    var_1.set('0')
    
def calcgo():
    i=var_1.get()
    s=eval(i)
    var_1.set(s)
#-----------------------------------------
#使用小猿的方法建立多个button//-----后记：我错了还是他的方法只能‘作外观’，button只能显示，我只能一个一个的写了。
#1.建立一个表用来存列表元素
'''type_list=(
    ('1','2','3','+'),
    ('4','5','6','-'),
    ('7','8','9','*'),
    ('0','.','=','/'),
    ('**','(',')','C')
    )
#2.使用enumrate遍历
for a,b in enumerate(type_list):
    for i,j in enumerate(b):
        Button(windos,width='10',text=j,bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('6')).place(x=i*90, y=(a+1)*45)

        print(55)'''
#------------------------------------------------

Button(windos,width='10',text='1',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('1')).place(x=0*90, y=1*45)
Button(windos,width='10',text='2',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('2')).place(x=1*90, y=1*45)
Button(windos,width='10',text='3',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('3')).place(x=2*90, y=1*45)
Button(windos,width='10',text='+',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('+')).place(x=3*90, y=1*45)

Button(windos,width='10',text='4',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('4')).place(x=0*90, y=2*45)
Button(windos,width='10',text='5',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('5')).place(x=1*90, y=2*45)
Button(windos,width='10',text='6',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('6')).place(x=2*90, y=2*45)
Button(windos,width='10',text='-',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('-')).place(x=3*90, y=2*45)

Button(windos,width='10',text='7',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('7')).place(x=0*90, y=3*45)
Button(windos,width='10',text='8',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('8')).place(x=1*90, y=3*45)
Button(windos,width='10',text='9',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('9')).place(x=2*90, y=3*45)
Button(windos,width='10',text='*',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('*')).place(x=3*90, y=3*45)

Button(windos,width='10',text='0',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('0')).place(x=0*90, y=4*45)
Button(windos,width='10',text='.',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('.')).place(x=1*90, y=4*45)
Button(windos,width='10',text='=',bg='#121a2a',fg='#d1c7b7',command=calcgo).place(x=2*90, y=4*45)
Button(windos,width='10',text='/',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('/')).place(x=3*90, y=4*45)

Button(windos,width='10',text='**',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('**')).place(x=0*90, y=5*45)
Button(windos,width='10',text='(',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num('(')).place(x=1*90, y=5*45)
Button(windos,width='10',text=')',bg='#121a2a',fg='#d1c7b7',command=lambda:put_num(')')).place(x=2*90, y=5*45)
Button(windos,width='10',text='C',bg='#121a2a',fg='#d1c7b7',command=clear).place(x=3*90, y=5*45)
#------------------------------------
windos.mainloop()

