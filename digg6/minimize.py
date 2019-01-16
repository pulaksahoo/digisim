import itertools


#compare two binary strings, check where there is one difference
def compBinary(s1,s2):
    count = 0
    pos = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
            pos = i
    if count == 1:
        return True, pos
    else:
        return False, None


#compare if the number is same as implicant term
#s1 should be the term
def compBinarySame(term,number):
    for i in range(len(term)):
        if term[i] != '-':
            if term[i] != number[i]:
                return False

    return True


#combine pairs and make new group
def combinePairs(group, unchecked):
    #define length
    l = len(group) -1

    #check list
    check_list = []

    #create next group
    next_group = [[] for x in range(l)]

    #go through the groups
    for i in range(l):
        #first selected group
        for elem1 in group[i]:
            #next selected group
            for elem2 in group[i+1]:
                b, pos = compBinary(elem1, elem2)
                if b == True:
                    #append the ones used in check list
                    check_list.append(elem1)
                    check_list.append(elem2)
                    #replace the different bit with '-'
                    new_elem = list(elem1)
                    new_elem[pos] = '-'
                    new_elem = "".join(new_elem)
                    next_group[i].append(new_elem)
    for i in group:
        for j in i:
            if j not in check_list:
                unchecked.append(j)

    return next_group, unchecked


#remove redundant lists in 2d list
def remove_redundant(group):
    new_group = []
    for j in group:
        new=[]
        for i in j:
            if i not in new:
                new.append(i)
        new_group.append(new)
    return new_group


#remove redundant in 1d list
def remove_redundant_list(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


#return True if empty
def check_empty(group):

    if len(group) == 0:
        return True

    else:
        count = 0
        for i in group:
            if i:
                count+=1
        if count == 0:
            return True
    return False


#find essential prime implicants ( col num of ones = 1)
def find_prime(Chart):
    prime = []
    for col in range(len(Chart[0])):
        count = 0
        pos = 0
        for row in range(len(Chart)):
            #find essential
            if Chart[row][col] == 1:
                count += 1
                pos = row

        if count == 1:
            prime.append(pos)

    return prime

def check_all_zero(Chart):
    for i in Chart:
        for j in i:
            if j != 0:
                return False
    return True

#find max value in list
def find_max(l):
    max = -1
    index = 0
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
            index = i
    return index

#multiply two terms (ex. (p1 + p2)(p1+p4+p5) )..it returns the product
def multiplication(list1, list2):
    list_result = []
    #if empty
    if len(list1) == 0 and len(list2)== 0:
        return list_result
    #if one is empty
    elif len(list1)==0:
        return list2
    #if another is empty
    elif len(list2)==0:
        return list1

    #both not empty
    else:
        for i in list1:
            for j in list2:
                #if two term same
                if i == j:
                    #list_result.append(sorted(i))
                    list_result.append(i)
                else:
                    #list_result.append(sorted(list(set(i+j))))
                    list_result.append(list(set(i+j)))

        #sort and remove redundant lists and return this list
        list_result.sort()
        return list(list_result for list_result,_ in itertools.groupby(list_result))

#petrick's method
def petrick_method(Chart):
    #initial P
    P = []
    for col in range(len(Chart[0])):
        p =[]
        for row in range(len(Chart)):
            if Chart[row][col] == 1:
                p.append([row])
        P.append(p)
    #do multiplication
    for l in range(len(P)-1):
        P[l+1] = multiplication(P[l],P[l+1])

    P = sorted(P[len(P)-1],key=len)
    final = []
    #find the terms with min length = this is the one with lowest cost (optimized result)
    min=len(P[0])
    for i in P:
        if len(i) == min:
            final.append(i)
        else:
            break
    #final is the result of petrick's method
    return final

#chart = n*n list
def find_minimum_cost(Chart, unchecked):
    P_final = []
    #essential_prime = list with terms with only one 1 (Essential Prime Implicants)
    essential_prime = find_prime(Chart)
    essential_prime = remove_redundant_list(essential_prime)

    # #print out the essential primes
    # if len(essential_prime)>0:
    #     s = "\nEssential Prime Implicants :\n"
    #     for i in range(len(unchecked)):
    #         for j in essential_prime:
    #             if j == i:
    #                 s= s+binary_to_letter(unchecked[i])+' , '
    #     print s[:(len(s)-3)]

    #modifiy the chart to exclude the covered terms
    for i in range(len(essential_prime)):
        for col in range(len(Chart[0])):
            if Chart[essential_prime[i]][col] == 1:
                for row in range(len(Chart)):
                    Chart[row][col] = 0

    #if all zero, no need for petrick method
    if check_all_zero(Chart) == True:
        P_final = [essential_prime]
    else:
        #petrick's method
        P = petrick_method(Chart)

        #find the one with minimum cost
        #see "Introduction to Logic Design" - Alan B.Marcovitz Example 4.6 pg 213
        '''
        Although Petrick's method gives the minimum terms that cover all,
        it does not mean that it is the solution for minimum cost!
        '''

        P_cost = []
        for prime in P:
            count = 0
            for i in range(len(unchecked)):
                for j in prime:
                    if j == i:
                        count = count+ cal_efficient(unchecked[i])
            P_cost.append(count)


        for i in range(len(P_cost)):
            if P_cost[i] == min(P_cost):
                P_final.append(P[i])

        #append prime implicants to the solution of Petrick's method
        for i in P_final:
            for j in essential_prime:
                if j not in i:
                    i.append(j)

    return P_final

#calculate the number of literals
def cal_efficient(s):
    count = 0
    for i in range(len(s)):
        if s[i] != '-':
            count+=1

    return count

#print the binary code to letter
def binary_to_letter(s):
    out = ''
    c = 'a'
    more = False
    n = 0
    for i in range(len(s)):
        #if it is a range a-zA-Z
        if more == False:
            if s[i] == '1':
                out = out + c
            elif s[i] == '0':
                out = out + c.upper()

        if more == True:
            if s[i] == '1':
                out = out + c + str(n)
            elif s[i] == '0':
                out = out + c.upper() + str(n)
            n+=1
        #conditions for next operations
        if c=='z' and more == False:
            c = 'A'
        elif c=='Z':
            c = 'a'
            more = True

        elif more == False:
            c = chr(ord(c)+1)
    return out

#nand gate representation
def nand(s2):
	s3 = []
	s2 = s2.split('+')
	for j in s2:
		s3.append("#"+'('+','.join(str(g) for g in j)+')')
	s4 = []
	for j in s3:
		j = list(j)
		for i in range(len(j)):
			if j[i].isupper():
				j[i] = str('#'+'('+j[i].lower()+','+j[i].lower()+')')
		s4.append(''.join([str(g) for g in j]))		
	s4 = ','.join([str(g) for g in s4])
	return '#('+s4+')'

def back(exp,firstchar):
	if firstchar == 'F':
		for i in range(len(exp)):
			if exp[i].isalpha():
			    if exp[i].isupper():
			        exp[i] = 'F' + str((ord(exp[i]) - 65) + 1)  
			    else:
			        exp[i] = 'f' + str((ord(exp[i]) - 97) + 1)  
		exp = ''.join([str(g) for g in exp])
	else:
		for i in range(len(exp)):
			if exp[i].isalpha():
			    if exp[i].isupper():
			        exp[i] = chr(ord(firstchar) + (ord(exp[i]) - 65))   
			    else:
			        exp[i] = chr((ord(firstchar) + 32) + (ord(exp[i]) - 97))   
		exp = ''.join([str(g) for g in exp])
	return exp
#main function
def digi_minimize(n,expression):
    #get the num of variables (bits) as input
    n_var = n
    # n_var = int(raw_input("Enter the number of variables(bits): "))
    #get the minterms as input
    expression=expression.replace(' ','')
    exp = list(expression)
    # exp = list(raw_input("Enter the expression: "))

    if '1' in exp:
    	firstchar = 'F'
    	exp = ''.join([str(g) for g in exp]).split('+')
    	newout = []
    	for i in exp:
    		ss = ''
    		for j in range(0,len(i),2):
    			s = chr(65+(int(i[j+1])-1))
    			if i[j].islower():
    				s = s.lower()	
    			ss += s
    		newout.append(ss)
    	exp = newout
    else:
        inp=[]
        for i in exp:
            if i != '+':
                inp.append(i.upper())
        firstchar = sorted(inp)[0]


    	for i in range(len(exp)):
		    if exp[i].isalpha():
		        if exp[i].isupper():
		            exp[i] = chr(65 + (ord(exp[i]) - ord(firstchar)))    
		        else:
		            exp[i] = chr(97 + (ord(exp[i]) - (ord(firstchar) + 32 )))    
    	exp = ''.join([str(g) for g in exp]).split('+')
    for i in exp:
        if '^' in i:
            if i[0].isupper() and i[-1].isupper():
            	exp.append(i[0].upper()+i[-1].lower())
            	exp.append(i[0].lower()+i[-1].upper())
            	exp.remove(i)
            if i[0].islower() and i[-1].islower():
            	exp.append(i[0].lower()+i[-1].upper())
            	exp.append(i[0].upper()+i[-1].lower())
            	exp.remove(i)
            if i[0].islower() and i[-1].isupper():
            	exp.append(i[0].upper()+i[-1].upper())
            	exp.append(i[0].lower()+i[-1].lower())
            	exp.remove(i)
            if i[0].isupper() and i[-1].islower():
            	exp.append(i[0].lower()+i[-1].lower())
            	exp.append(i[0].upper()+i[-1].lower())
            	exp.remove(i)
    	elif '~' in i:
    		if i[0].isupper() and i[-1].isupper():
	    		exp.append(i[0].upper()+i[-1].upper())
    			exp.append(i[0].lower()+i[-1].lower())
    			exp.remove(i)
    		if i[0].islower() and i[-1].islower():
	    		exp.append(i[0].lower()+i[-1].lower())
    			exp.append(i[0].upper()+i[-1].upper())
    			exp.remove(i)
    		if i[0].islower() and i[-1].isupper():
	    		exp.append(i[0].lower()+i[-1].upper())
    			exp.append(i[0].upper()+i[-1].lower())
    			exp.remove(i)
    		if i[0].isupper() and i[-1].islower():
	    		exp.append(i[0].upper()+i[-1].lower())
    			exp.append(i[0].lower()+i[-1].upper())
    			exp.remove(i)
    #print(exp)							
    exp2 = []
    for i in exp:
        if len(i) != n_var:
            i1 = ''        
            for j in range(0,n_var):
                alphabet1 , alphabet2 = chr(j+65) , chr(j+97) 
                if alphabet1 not in i and alphabet2 not in i:
                    i1 += '_'
                else:
                    if alphabet1 in i:
                        i1 += alphabet1

                    else:
                        i1 += alphabet2
            exp2.append(i1)
        else:
             exp2.append(i)                
    #print(exp2)
    for i in exp2:
        if '_' in i:
            count = i.count('_')
            miss = list(itertools.product([0, 1], repeat=count))
            for j in range(len(miss)):
                count = 0
                string = ''
                for z in i:
                    if z == '_':
                        string += str(miss[j][count])
                        count += 1
                    else:
                        string += z
                exp2.append(string)
    
    exp = []
    for i in exp2:
        if '_' not in i:
            exp.append(i)
    #print(exp)        
    # for i in exp:
    #     if(len(i)<n_var):
    #         while(len(i) != n_var):              
    minterms = []
    #converting expression terms into minterms 
    for i in exp:
        out = ''
        for j in i:
            if j.isalpha():
                if j.isupper():
                    out += '0'
                else:
                    out += '1'
            else:
                out += j
        #print(out)                       
        minterms.append(int(out,2))               

    #minterms = raw_input("Enter the minterms (ex. 0 1 2 5 9 10) : ")
    a = minterms#.split()
    
    #put the numbers in list in int form
    a = map(int, a)
    for i in a:
        c = bin(i)[2:]
        #print(binary_to_letter(c))

    #make a group list
    group = [[] for x in range(n_var+1)]

    for i in range(len(a)):
        #convert to binary
        a[i] = bin(a[i])[2:]
        if len(a[i]) < n_var:
            #add zeros to fill the n-bits
            for j in range(n_var - len(a[i])):
                a[i] = '0'+ a[i]
        #if incorrect input
        elif len(a[i]) > n_var:
            print '\nError : Choose the correct number of variables(bits)\n'
            return
        #count the num of 1
        index = a[i].count('1')
        #group by num of 1 separately
        group[index].append(a[i])


    all_group=[]
    unchecked = []
    #combine the pairs in series until nothing new can be combined
    while check_empty(group) == False:
        all_group.append(group)
        next_group, unchecked = combinePairs(group,unchecked)
        group = remove_redundant(next_group)

    # s = "\nPrime Implicants :\n"
    # for i in unchecked:
    #     s= s + binary_to_letter(i) + " , "
    # print s[:(len(s)-3)]

    #make the prime implicant chart
    Chart = [[0 for x in range(len(a))] for x in range(len(unchecked))]

    for i in range(len(a)):
        for j in range (len(unchecked)):
            #term is same as number
            if compBinarySame(unchecked[j], a[i]):
               Chart[j][i] = 1

    #prime contains the index of the prime implicant terms
    #prime = remove_redundant_list(find_minimum_cost(Chart))
    primes = find_minimum_cost(Chart, unchecked)
    primes = remove_redundant(primes)


    # print "\n--  Minimised Expression --\n"
    s2=''
    for prime in primes:
        s=''
        t=''
        for i in range(len(unchecked)):
            for j in prime:
                if j == i:
                    s= s+binary_to_letter(unchecked[i])+' + '
        t = s[:(len(s)-3)]
        q = back(list(t),firstchar)
        # print q
        
        s2 += q.replace(' ','')
	return s2        
	break
    # print('\n-- Universal Gate Expression --\n')
    # print(nand(s2))

if __name__ == "__main__":
    digi_minimize()
    # A = raw_input("\nPress Enter to Quit")
