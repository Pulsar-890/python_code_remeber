import os
path=os.getcwd()+"\\"
filename="管理内容.txt"
SEpa="\n"
def open_file(infor="",subpath=''):
    print("正在打开,请稍候...")
    os.startfile(path+subpath)
def txt(func, lis="", file=filename):    #txt('w',text);txt('a',text);
    import encodings;SEpa="\n"
    if func not in ['r','a','w']:raise ValueError("Invalid mode. Expected one of: ['r','a','w']")
    def oper_txt(encod,file=file):
        with open(file, func, encoding=encod) as f:
            if func == "r":return f.read().replace("\ufeff","").split(SEpa)
            else:f.write({"a":SEpa,"w":""}[func]+SEpa.join(lis));return 0
    for k in ['gbk', 'utf-8', 'utf-16']+list(set(encodings.aliases.aliases.values())):
        try:result=oper_txt(k);break
        except (UnicodeDecodeError, UnicodeEncodeError, FileNotFoundError,UnicodeError,LookupError):result=0
    if func=="r":return result

alpha="123456789abcdefghijklmnopqrstuvwxyz"
def create_number():
    for i in alpha:
        if i not in con:return i
    else:
        for i in alpha:
            for j in alpha:
                if i+j not in con:return i+j
        else:
            n=input("1260个序号怎么都被你用完了，还是你自己定一个吧：")
            while n in con:n=input("序号已存在：")
            return n

def initial(width=24):
    a=txt("r")
    width=int(a[0].split(":")[1])
    a=a[1:]
    blocks=120//width
    nums,con=0,{}
    for i in a:
        con[i[:i.find('.')]]=i[i.find('.')+1:]
        while i and len(i.encode('gbk'))>=(blocks-nums%blocks)*width:
            for j in range(blocks*width,-1,-1):
##                print(j,blocks,nums)
                if len(i[:j].encode('gbk'))<=(blocks-nums%blocks)*width:break
            print(i[:j])
            i,nums=i[j:],0
        if i:
            l=len(i.encode('gbk'))
##            print(l)
            print(i,end=(width-l%width)*" ")
            nums+=l//width+1
##            print(i,l,nums,1+(-l-1)//8%width)
            if nums%blocks==0:print()
    return con

if not os.path.exists(path+filename):
    print("初始化中...")
    txt("w",["选项显示宽度:24","0.管理内容"])
while 1:
    con=initial()
    a=input("\n请输入：")
    if a[0]=="0":
        if len(a)==1:a=input('''
管理选项：
0.修改文件
1.新建文件
2.打开文件夹
3.文件重命名
4.删除文件
5.更改选项显示宽度(1-120)
输入其他任意字符退出...
注：需要执行的语句加///，不需要打印的部分前后各加一行：###
请输入：''')
        else:a=a[1:]
        if a[0]=="2":open_file("文件夹")
        if a[0]=="5":
            if len(a)!=1:width=a[1:]
            else:width=input("请输入文本宽度：")
            while not width.isdigit() or not 1<=int(width)<=120:
                width=input("输入范围有误，请重新输入：")
            x=txt("r")
            x[0]="选项显示宽度(tab数):"+width
            txt("w",x)
            print("选项显示宽度调整成功！")
        elif a[0] in ["0","1","3","4"]:
            if len(a)!=1:name=a[1:]
            elif a[0]!="1":name=input("请输入文件序号：")
            else:name=input("请输入文件序号（回车则由系统选择）：")
            if a[0]=="1":
                name=name.split()
                while name and name[0] in con:name[0]=input(name[0]+" 序号已存在，请重新输入：")
                if not name[:1]:
                    name=[create_number()]+name[1:]
                    print("系统选择的序号为",name[0])
                if len(name)==1:name.append(input("请输入文件名："))
                while name[1] in con.values():name[1]=input(name[1]+" 文件已存在，请重新输入：")
                txt('a',[''],name[1]+'.txt')
                txt('a',[f"{name[0]}.{name[1]}"])
                open_file(f"文件{name[1]}.txt",name[1]+".txt")
            elif a[0]=="3":
                name=name.split()
                if name[0] not in con:
                    print(f"未找到序号！")
                    continue
                if len(name)==1:name.append(input("请输入新的文件名："))
                txt1=txt("r")
                txt1[txt1.index(name[0]+"."+con[name[0]])]=name[0]+"."+name[1]
                os.rename(con[name[0]]+'.txt',name[1]+'.txt')
                txt('w',txt1)
                print(f"\n文件{con[name[0]]}已重命名为{name[1]}")
            elif name not in con :print(f"未找到序号！")
            elif a[0]=="4":
                if input("删除后的文件无法找回，请确认你要删除这个文件?[Y/N]").lower() in ["y","yes"]:
                    txt1=txt("r")
                    txt1.pop(txt1.index(name+"."+con[name]))
                    os.remove(con[name]+'.txt')
                    txt('w',txt1)
                    print(f"\n文件{con[name]}已删除")
            else:open_file(f"文件{name}.txt",con[name]+".txt")
    else:
        if a in con:
            anno=1
            for i in ['']+txt('r',0,con[a]+'.txt'):
                if i[:3]=="///":eval(i[3:])
                elif i[:3]=="###":anno=1-anno
                elif anno:print(i)
        else:print("文件不存在！")
    print()


