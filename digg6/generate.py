from itertools import product
# from setuptools.dist import sequence
def extract_var(funct):
    list1=funct.split('+')



    var_list=[]
    operator=['+','.']
    text_variable=''
    for i in funct:
        
        if (i not in operator):
            text_variable+=i;
        else:
            if(text_variable not in var_list):
                var_list.append(text_variable)
            text_variable=''
    if(text_variable not in var_list):
        var_list.append(text_variable)


    return var_list

def extract_outs(var_list,funct):
    andy=[]
    cofac=[]
    for c in range(len(var_list)+1):
        cofac.append([])


    cofac[0].append(funct)
    for k in range(len(var_list)):
        andy.append(var_list[k].lower())



    for i in range(1,len(andy)+1):
        for k in range(2**i):
            cofac[i].append(cofac[i-1][int(k/2)])
            
        for j in range(2**i):
            if j%2==0:
                cofac[i][j]=cofac[i][j].replace(andy[i-1],'0')
                cofac[i][j]=cofac[i][j].replace(andy[i-1].upper(),'1')
            if j%2==1:
                cofac[i][j]=cofac[i][j].replace(andy[i-1],'1')
                cofac[i][j]=cofac[i][j].replace(andy[i-1].upper(),'0')
                
        


    k=[]
    l=[]
    h=2**len(andy)
    val=[0]*(h)
    val1=[]
    for i in range(0,h):
        k.append(cofac[len(andy)][i].split('+'))
        # print(k)
        
        value=0
        # print(i,j)
        for j in range(0,len(k[i])):
            if k[i][j].find('0')!=-1:
                val=0
            else :
                val=1
                value=val
                
        val1.append(value)
    return val1


def gen_result(var_list,inputs,possble_outs,my_dict):
    inp=[]
    li=[x.lower() for x in var_list]
#     print(li)
    for i in li:
#         print(i)
        inp.append(int(my_dict[i]))
    # print(inp)
    # print(inputs[1])
    ip=[]
    for j in inputs:
        z=list(j)
        ip.append(z)
    for i in range(len(inputs)):
        if(ip[i]==inp):
            result=possble_outs[i]
            # print(possble_outs[i])
            break
        else:
            continue
    return result





def testcases(expression,my_dict=None):
    # my_dict = dict()
    # n=int(input('enter the no of variables:'))
    # for i in range(n):
     
    #     key = input("Enter the key: ")
    #     value = input("Enter the value: ")
         
    #     my_dict[key] = value

    array = []
    freedom=[]
    # print(my_dict)
#     print ("enter the expression")
    # funct=input()
    funct=expression
    # print(funct)
    var_list=extract_var(funct)
    # print(var_list)
    # print('no of var:',len(var_list))
    possble_outs=extract_outs(var_list,funct)
    inputs = list(product([0, 1], repeat=len(var_list)))
    for i in range(len(var_list)):
        array.append(var_list[i])
    # array.sort()
    # for i in range(len(var_list)):
    #     if(array[i]!=var_list[i]):
    #         freedom.append(array.index(var_list[i]))
    # inp=[][]
    # p
    # for i in range(len(freedom)):
    #     p.append(freedom[i])
    # p.sort()
    if(my_dict==None):

        print('Possible outputs for given minimized expression are:')
        for i in range(len(possble_outs)):
            print inputs[i],'-->',possble_outs[i]
    else:
        result=gen_result(var_list,inputs,possble_outs,my_dict)

        return result


