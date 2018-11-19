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





def generate_results(expression,my_dict=None):
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




def D_flipflop(previous_value,input_value,clock):
    if(clock==1):
        return input_value
    else:
        return previous_value
def not_function(input):
    if(input==0):
        return 1
    else:
        return 0
def T_flipflop(previous_value,input_value,clock):
    if(clock==1):
        if(input_value==1):
            return not_function(previous_value)
        else:
            return previous_value
    else:
        return previous_value
def JK_flipflop(previous_value,input_value_j,input_value_k,clock):
    if(clock==1):
        if(input_value_j==0 and input_value_k==0):
            return previous_value
        elif(input_value_j==0 and input_value_k==1):
            return 0
        elif(input_value_j==1 and input_value_k==0):
            return 1
        else:
            return not_function(previous_value)
def print_sequence(sequence_list,cyclecount):
    print 'sequence: ', 
    for i in range(len(sequence_list)):
        if(i!=(len(sequence_list)-1)):
            # print(sequence_list[i],'-->',end='')
            print sequence_list[i],'-->',
        else:
            print sequence_list[i] 
    # sequence_list=sequence_list[:len(sequence_list)-1]
    # sequence_list=sequence_list[:]
    j=0
    for i in range(cyclecount):
        # print(sequence_list,j)
        if(sequence_list[j] in sequence_list[:j]):
            ind=sequence_list.index(sequence_list[j])
            sequence_list=sequence_list[ind+1:]
        if(j>=len(sequence_list)-1):
            j=0
        else:
            j+=1
    # cycle_value=((cyclecount%len(sequence_list)))%len(sequence_list)
    cycle_value=j
    # print('hi',sequence_list,j)
    print 'Sequence Value at cycle',cyclecount,': ',sequence_list[cycle_value]
    
def cyclecount_function(flipflops,cyclecount):
    l=[]
    x=''
    for i in flipflops.keys():
        x+=str(flipflops[i]['initial'])
    cycle=0
    
    while(x not in l):
#     while(1):
        if(x not in l):
            l.append(x)
#         if(cycle>=cyclecount ):
#             break
        x=''
        flip_flop_values={}
        for ff in flipflops.keys():
            flip_flop_values[ff]=flipflops[ff]['initial']
        
#         print(flipflops.keys())
        for i in flipflops.keys():
            
            if (flipflops[i]['type']==1):
#                 print(flipflops[i]['type'])
                gen_inp_res=generate_results(flipflops[i]['input'], flip_flop_values)
#                 flipflops[i]['initial']=T_flipflop(flipflops[i]['initial'], 
#                                                    flipflops[flipflops[i]['input']]['previous'],
#                                                     flipflops[i]['clock'])
                flipflops[i]['initial']=T_flipflop(flipflops[i]['initial'], 
                                                   gen_inp_res,
                                                    flipflops[i]['clock'])
            elif (flipflops[i]['type']==2):
                gen_inp_res=generate_results(flipflops[i]['input'], flip_flop_values)
                flipflops[i]['initial']=D_flipflop(flipflops[i]['initial'], 
                                                   gen_inp_res,
                                                    flipflops[i]['clock'])
            else:
                gen_inp_res_j=generate_results(flipflops[i]['input_j'], flip_flop_values)
                gen_inp_res_k=generate_results(flipflops[i]['input_k'], flip_flop_values)
#                 flipflops[i]['initial']=JK_flipflop(flipflops[i]['initial'], 
#                                                    flipflops[flipflops[i]['input_j']]['previous'],
#                                                    flipflops[flipflops[i]['input_k']]['previous'],
#                                                     flipflops[i]['clock'])
                flipflops[i]['initial']=JK_flipflop(flipflops[i]['initial'], 
                                                   gen_inp_res_j,
                                                   gen_inp_res_k,
                                                    flipflops[i]['clock'])
            x+=str(flipflops[i]['initial'])
            
        for i in flipflops.keys():
            flipflops[i]['previous']=flipflops[i]['initial']
        cycle+=1
    l.append(x)
    print_sequence(l,cyclecount)
#     print(l)
#     print(x)
    return l
        
        
    pass
def FlipFlop(no_of_flipflops,no_of_cycles):
    
    if(no_of_flipflops>10):
        print('Kindly enter a no of flipflops below 10')
        exit()
    elif(no_of_flipflops<=0):
        print('Kindly enter a valid no of flipflop value.')
        exit()
    if(no_of_cycles>10000):
        print('Kindly enter a no of cycles below 10000')
        exit()
    elif(no_of_cycles<=0):
        print('Kindly enter a valid no of cycles value.')
        exit()
    flipflops={}
    flipflop_names=[]
    flipflop_names_complemented=[]
    for i in range(no_of_flipflops):
        name_of_flipflop='f'+str(i+1)
        name_of_flipflop_comp='F'+str(i+1)
        flipflop_names.append(name_of_flipflop)
        flipflop_names_complemented.append(name_of_flipflop_comp)
    print("The flipflop names are: ",flipflop_names,"and its complements are: ",flipflop_names_complemented)
    input_value=['0','1']
    type_value=['1','2','3']
    all_operator_operands=flipflop_names + flipflop_names_complemented + ['+','.']
#     print(all_operator_operands)
    for i in range(no_of_flipflops):
        print('FlipFlop No',i+1,': ')
        type_of_flipflop=raw_input('Enter the choice for type of flipflop as \n1.T-FlipFlop\n2.D-FlipFlop\n3.J-K FlipFlop\nEnter it here:  ')
        # print(type_of_flipflop)
        if(type_of_flipflop not in type_value):
            print(type_of_flipflop)
            print('wrong value entered')
            exit()
        else:
            type_of_flipflop=int(type_of_flipflop)
    
        name_of_flipflop='f'+str(i+1)
        initial_value=raw_input('Enter initial value in 0 or 1: ')
        while(initial_value not in ['0','1']):
            print('Wrong value entered')
            initial_value=raw_input('Enter intial value in 0 or 1: ')
        initial_value=int(initial_value)
        clock_equation=1
        if(type_of_flipflop==3):
            input_equation_j=raw_input('Enter the equation for J: ')
#             for j in input_equation_j:
#                 if(j not in all_operator_operands):
#                     print("Enter valid equation")
#                     exit()
            input_equation_k=raw_input('Enter the equation for K: ')
#             for j in input_equation_k:
#                 if(j not in all_operator_operands):
#                     print("Enter valid equation")
#                     exit()
            x={'type':type_of_flipflop,'clock':clock_equation,'input_j':input_equation_j,'input_k':input_equation_k,'initial':initial_value,'previous':initial_value}
            
        else:
            input_equation=raw_input('Enter the equation: ')
#             print(input_equation.split(''))
#             for j in input_equation:
#                 if(j not in all_operator_operands):
#                     print("not a valid equation")
#                     exit()
            x={'type':type_of_flipflop,'clock':clock_equation,'input':input_equation,'initial':initial_value,'previous':initial_value}
        flipflops[name_of_flipflop]=x
#     print(flipflops)
    cyclecount_function(flipflops,no_of_cycles)

def cyclecount_function_async(flipflops,cyclecount):
    l=[]
    x=''
    for i in flipflops.keys():
        x+=str(flipflops[i]['initial'])
    cycle=0
    
    while(x not in l):
#     while(1):
        if(x not in l):
            l.append(x)
#         if(cycle>=cyclecount ):
#             break
        x=''
        flip_flop_values={}
        for ff in flipflops.keys():
            flip_flop_values[ff]=flipflops[ff]['initial']
        
#         print(flipflops.keys())
        for i in flipflops.keys():
            
            if (flipflops[i]['type']==1):
#                 print(flipflops[i]['type'])
                gen_inp_res=generate_results(flipflops[i]['input'], flip_flop_values)
                gen_inp_res_clk=generate_results(flipflops[i]['clock'], flip_flop_values)
#                 flipflops[i]['initial']=T_flipflop(flipflops[i]['initial'], 
#                                                    flipflops[flipflops[i]['input']]['previous'],
#                                                     flipflops[i]['clock'])
                flipflops[i]['initial']=T_flipflop(flipflops[i]['initial'], 
                                                   gen_inp_res,
                                                    gen_inp_res_clk)
            elif (flipflops[i]['type']==2):
                gen_inp_res=generate_results(flipflops[i]['input'], flip_flop_values)
                gen_inp_res_clk=generate_results(flipflops[i]['clock'], flip_flop_values)
                flipflops[i]['initial']=D_flipflop(flipflops[i]['initial'], 
                                                   gen_inp_res,
                                                    gen_inp_res_clk)
            else:
                gen_inp_res_j=generate_results(flipflops[i]['input_j'], flip_flop_values)
                gen_inp_res_k=generate_results(flipflops[i]['input_k'], flip_flop_values)
                gen_inp_res_clk=generate_results(flipflops[i]['clock'], flip_flop_values)
#                 flipflops[i]['initial']=JK_flipflop(flipflops[i]['initial'], 
#                                                    flipflops[flipflops[i]['input_j']]['previous'],
#                                                    flipflops[flipflops[i]['input_k']]['previous'],
#                                                     flipflops[i]['clock'])
                flipflops[i]['initial']=JK_flipflop(flipflops[i]['initial'], 
                                                   gen_inp_res_j,
                                                   gen_inp_res_k,
                                                    gen_inp_res_clk)
            x+=str(flipflops[i]['initial'])
            
        for i in flipflops.keys():
            flipflops[i]['previous']=flipflops[i]['initial']
        cycle+=1
    l.append(x)
    print_sequence(l, cyclecount)
#     print(l)
#     print(x)
#     return l
        
        
    pass


def FlipFlop_async(no_of_flipflops,no_of_cycles):
    if(no_of_flipflops>10):
        print('Kindly enter a no of flipflops below 10')
        exit()
    elif(no_of_flipflops<=0):
        print('Kindly enter a valid no of flipflop value.')
        exit()
    if(no_of_cycles>10000):
        print('Kindly enter a no of cycles below 10000')
        exit()
    elif(no_of_cycles<=0):
        print('Kindly enter a valid no of cycles value.')
        exit()
    flipflops={}
    flipflop_names=[]
    flipflop_names_complemented=[]
    for i in range(no_of_flipflops):
        name_of_flipflop='f'+str(i+1)
        name_of_flipflop_comp='F'+str(i+1)
        flipflop_names.append(name_of_flipflop)
        flipflop_names_complemented.append(name_of_flipflop_comp)
    print("The flipflop names are: ",flipflop_names,"and its complements are: ",flipflop_names_complemented)
    input_value=['0','1']
    type_value=['1','2','3']
    all_operator_operands=flipflop_names + flipflop_names_complemented + ['+','.']
    print(all_operator_operands)
    for i in range(no_of_flipflops):
        print('FlipFlop No',i+1,': ')
        type_of_flipflop=input('Enter the choice for type of flipflop as \n1.T-FlipFlop\n2.D-FlipFlop\n3.J-K FlipFlop\nEnter it here:  ')
        if(type_of_flipflop not in type_value):
            print('wrong value entered')
            exit()
        else:
            type_of_flipflop=int(type_of_flipflop)
    
        name_of_flipflop='f'+str(i+1)
        initial_value=input('Enter initial value in 0 or 1: ')
        while(initial_value not in ['0','1']):
            initial_value=input('Enter intial value in 0 or 1: ')
        initial_value=int(initial_value)
        clock_equation=input('Enter clock equation')
        if(type_of_flipflop==3):
            input_equation_j=input('Enter the equation for J: ')
#             for j in input_equation_j:
#                 if(j not in all_operator_operands):
#                     print("Enter valid equation")
#                     exit()
            input_equation_k=input('Enter the equation for K: ')
#             for j in input_equation_k:
#                 if(j not in all_operator_operands):
#                     print("Enter valid equation")
#                     exit()
            x={'type':type_of_flipflop,'clock':clock_equation,'input_j':input_equation_j,'input_k':input_equation_k,'initial':initial_value,'previous':initial_value}
            
        else:
            input_equation=input('Enter the equation: ')
#             print(input_equation.split(''))
#             for j in input_equation:
#                 if(j not in all_operator_operands):
#                     print("not a valid equation")
#                     exit()
            x={'type':type_of_flipflop,'clock':clock_equation,'input':input_equation,'initial':initial_value,'previous':initial_value}
        flipflops[name_of_flipflop]=x
#     print(flipflops)
    cyclecount_function_async(flipflops,no_of_cycles)
# FlipFlop(3, 3)
# FlipFlop_async(3,4)
        
            
        