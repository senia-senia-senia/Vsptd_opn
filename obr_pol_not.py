def Vhodnaya_obrabotka(sstr):
    sstr = sstr.replace(" ","")
    otkr_skobka = []
    zakr_skobka = []
    #Проверка на правильный ввод скобок
    k = 0
    z = 0
    i = 0
    j = len(sstr)-1
    while i <= j:
        if sstr[i] == "(":
            otkr_skobka.append(k)
            k+=1
            i+=1
        else:
            i += 1
            k+=1
    print(otkr_skobka)
    i = 0
    z = 0
    while i <= j:
        if sstr[i] == ")":
            zakr_skobka.append(z)
            z+=1
            i+=1
        else:
            i += 1
            z+=1
    print(zakr_skobka)
    i = 0
    k = len(otkr_skobka)-1
    z = len(zakr_skobka)-1
    if k>z:
        vyvod = 'В вашем выражении открывающих скобок больше чем закрывающих'
    elif k<z:
        vyvod = 'В вашем выражении закрывающих скобок больше чем открывающих'
    elif z == k:
        while i <= k:
            if otkr_skobka[i] > zakr_skobka[i]:
                vyvod = 'В вашем выражении допущена ошибка(расстановка скобок)'
                break
            else:
                vyvod = 'Проверка прошла успешно'
                i+=1
            
    return(vyvod)
def preobrazovaniye_v_opn(s):
    vyhod_str = ''
    stack = ''
    reserv_symbol=['+','-','*','/','(',')','**']
    prioritet_1={'(':0,'+':1,'*':2,')':0,'-':1,'/':2} #Словарь, включающий приоритет операций  
    j = len(s)-1
    i=0
    count_stack = 0
    while i <= j:
        if s[i] >= 'A' and s[i]<='z':
            vyhod_str = vyhod_str + s[i]
            i+=1
        elif s[i]==')':
            while stack[count_stack]!='(':
                vyhod_str += stack[count_stack]
                stack = stack[0:-1]
                count_stack = count_stack-1
            stack = stack[0:-1]
            i+=1
        elif (stack == '') :
            stack += s[i]
            i+=1
        elif s[i]=='(':
            stack += s[i]
            i+=1
            count_stack+=1
        elif (prioritet_1.get(s[i]) >= prioritet_1.get(stack[count_stack]))or\
        (prioritet_2.get(s[i]) >= prioritet_2.get(stack[count_stack]))or\
        (prioritet_1.get(s[i]) >= prioritet_2.get(stack[count_stack]))or\
        (prioritet_2.get(s[i]) >= prioritet_1.get(stack[count_stack])):
            stack += s[i]
            count_stack += 1
            i+=1
        else:
            vyhod_str += stack[i]
            stack[i]=''
            i+=1
        
        
        print(stack)
        print(count_stack)
        #print(s[i])
        print(i)
        print(vyhod_str)
        stack_count = len(stack)-1
    while stack_count >= 0:
        vyhod_str+=stack[stack_count]
        stack_count -=1
    return vyhod_str

def proverka_trpstr(s):
    reserv_symbol_1 = ['+','-','*','/','(',')','**']
    reserv_symbol_2 = ['$','.']
    i = 0
    trp_str = s
    trp_str = trp_str.replace('+','|')
    trp_str = trp_str.replace('-','|')
    trp_str = trp_str.replace('*','|')
    trp_str = trp_str.replace('/','|')
    trp_str = trp_str.replace('(','')
    trp_str = trp_str.replace(')','')
    trp_str = trp_str.split('|')
    return trp_str

def zamena(s):
    trp_str = proverka_trpstr(s)
    print(trp_str)
    vyrageniye = s
    i = 0
    alphavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while i<=(len(trp_str)-1):
        vyrageniye = vyrageniye.replace(trp_str[i],alphavit[i] )
        i+=1
    print(vyrageniye)
    #vyrageniye = Vhodnaya_obrabotka(vyrageniye)
    vyrageniye = preobrazovaniye_v_opn(vyrageniye)
    i = 0
    while i<=(len(trp_str)-1):
        vyrageniye = vyrageniye.replace(alphavit[i],trp_str[i])
        i+=1
        
    return s, vyrageniye
    
        
a = input('Введите исходную формулу\n')

grab, c = zamena(a)
print(grab,'\n', c)

        
        
