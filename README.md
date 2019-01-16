# digisim
Inbuilt functions

Major functionalities provided in the library are as follows-
Expression minimization

Given a boolean algebraic expression, we use classic Quine-McCluskey algorithm to return a minimised expression, by removing redundancies.

To get your reduced expression, use following lines of code-


>>> from digisim.minimize import digi_minimize
>>> expr='a+ab'
>>> reduced_expr=digi_minimize(2,expr)  # 2 represents number of boolean variables
>>> print (reduced_expr)

Note: Use lowercase notations to represent boolean variables in uncomplemented form, and uppercase notations to represent in complemented form.
Test case generator

Given a boolean algebraic expression, we can get all possible inputs acquired by it, along with corresponding outputs in table form on the terminal.

To get your test cases for the expression, use following lines of code-


>>> from digisim.generate import testcases
>>> expr='a+a.b'    # remember to add '.' for AND operation while using this function 
>>> testcases(expr) # prints all valid input-output combinations on the terminal.

To get a specific output of a given input for the expression, use following lines of code-


>>> from digisim.generate import testcases
>>> expr='a+a.b'    # remember to add '.' for AND operation while using this function
>>> out=testcases(expr,{'a':'1','b':'0'}) # dict contains values of a and b.
>>> print (out)

Note: Use lowercase notations to represent boolean variables in uncomplemented form, and uppercase notations to represent in complemented form.
Logic gates representation

Given a boolean algebraic expression, we can get a diagrammatic representation of logic circuit, employing AND, OR, NAND,and NOR gates.

To view general gates representation, use following lines of code-


>>> from digisim.gate import gates
>>> expr='a+b+c'
>>> gates(expr)  # make sure to pass minimised expression in this function via digi_minimize() method


To view NAND gates representation, use following lines of code-


>>> from digisim.gate import gnand
>>> expr='a+b+c'
>>> gnand(expr)  # make sure to pass minimised expression in this function via digi_minimize() method


To view NOR gates representation, use following lines of code-


>>> from digisim.gate import gnor
>>> expr='a+b+c'
>>> gnor(expr)  # make sure to pass minimised expression in this function via digi_minimize() method


Sequential circuits

We can simulate working of a sequentail circuit employing D, T, or J-K flip-flops. You just need to pass in number of flip-flops, and number of cycles after which you want to see the output.

For example,


>>> from digisim.sequential import FlipFlop
>>> FlipFlop(3,3)  # 3 flip-flops to be used, and 3 cycles need to iterated

('The flipflop names are: ', ['f1', 'f2', 'f3'], 'and its complements are: ', ['F1', 'F2', 'F3'])
('FlipFlop No', 1, ': ')
Enter the choice for type of flipflop as 
1.T-FlipFlop
2.D-FlipFlop
3.J-K FlipFlop
Enter it here:  2
Enter initial value in 0 or 1: 0
Enter the equation: f2
('FlipFlop No', 2, ': ')
Enter the choice for type of flipflop as 
1.T-FlipFlop
2.D-FlipFlop
3.J-K FlipFlop
Enter it here:  1
Enter initial value in 0 or 1: 1
Enter the equation: f1
('FlipFlop No', 3, ': ')
Enter the choice for type of flipflop as 
1.T-FlipFlop
2.D-FlipFlop
3.J-K FlipFlop
Enter it here:  2
Enter initial value in 0 or 1: 1
Enter the equation: f2+f3

sequence:  011 --> 111 --> 101 --> 011
Sequence Value at cycle 3 :  011


Similarly, for asynchronous sequential circuits-


>>> from digisim.sequential import FlipFlop_async
>>> FlipFlop_async(3,3)  # 3 flip-flops to be used, and 3 cycles need to iterated

('The flipflop names are: ', ['f1', 'f2', 'f3'], 'and its complements are: ', ['F1', 'F2', 'F3'])
['f1', 'f2', 'f3', 'F1', 'F2', 'F3', '+', '.']
FlipFlop No 1 : 
Enter the choice for type of flipflop as 
1.T-FlipFlop
2.D-FlipFlop
3.J-K FlipFlop
Enter it here:  1
Enter initial value in 0 or 1: 1
Enter clock equationf1
Enter the equation: f1
FlipFlop No 2 : 
Enter the choice for type of flipflop as 
1.T-FlipFlop
2.D-FlipFlop
3.J-K FlipFlop
Enter it here:  2
Enter initial value in 0 or 1: 0
Enter clock equationf2
Enter the equation: f1
FlipFlop No 3 : 
Enter the choice for type of flipflop as 
1.T-FlipFlop
2.D-FlipFlop
3.J-K FlipFlop
Enter it here:  2
Enter initial value in 0 or 1: 1
Enter clock equationf1
Enter the equation: f3

sequence:  101 --> 001 --> 001
Sequence Value at cycle 3 :  001


