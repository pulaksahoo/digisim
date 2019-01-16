import re
import Tkinter as tk
from Tkinter import Tk,Canvas,Frame,BOTH
from collections import OrderedDict
import minimize


def gates(inp):
	l=[]
	l=inp.split('+')
	print(l)

	n=len(l)
	orr=n-1
	nd=0
	temp=[0]*n
	d=OrderedDict()
	for i in range(n):
		if(len(l[i])>1):
			nd+=len(l[i])-1
			d[i+1]=len(l[i])-1
			s=''
			for j in l[i]:
				if(j!=l[i][-1:]):
					s+=j+'AND'
			s+=l[i][-1:]
			temp[i]=s
		else:
			temp[i]=l[i]

	# print(d)  print dictionary with index->no.of ands needed!
	val=temp[-1:][0]
	s=''
	
	for i in temp:
		# if(i!=val):
		s+='('+i+')'+' OR '

	s=s[:len(s)-4]

	print('OR--'+str(orr)+' AND--'+str(nd))
	print(s)
	
	data,data1,data2,data3=[],[],[],[]		
	for j in l:
		if(len(j)==1):
			data.append(j)
		if(len(j)==2):
			data1.append(j)
		if(len(j)==3):
			data2.append(j)
		if(len(j)==4):
			data3.append(j)

	root=Tk()
	c = Canvas(master=root, width=500, height=450, bd=0, highlightthickness=0)
	c.master.title('Gates Representation')
	temp=orr
	x1,p1=165,70
	y1,q1=100,100
	x2,p2=195,100
	y2,q2=100,100
	# c=Canvas(root)
	# t=Text(root)
	
	c.create_rectangle(20,20,33,45,fill='#3b5998')
	c.create_text(60,30,text=': AND')
	c.create_line(80,35,100,35)
	c.create_line(100,20,100,50)
	c.create_arc(100-4,28-8,100+19,30+20,start=220,extent=270,fill='black',style=tk.ARC)
	c.create_text(140,30,text=': OR ')
	while(orr>0):
		if(temp==orr):
			u=0
			if(nd==0):
				y=data[u]
				u+=1
				c.create_text(x1-20,y1,text=y,font=('Purisa',10))
				data.remove(y)
			c.create_line(x1-15,y1,x2,y2)
			if(nd==0 or len(d)<2):
				y=data[u]
				u+=1
				c.create_text(x1-20,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
			c.create_line(x1-15,y1+15,x2,y2+15)
			c.create_line(x2,y1-8,x2,y2+24)
			c.create_arc(x2-4,y1-8,x2+19,y2+20,start=220,extent=270,fill='black',style=tk.ARC)
			c.create_line(x2+22,y1+10,x2+40,y1+10)
			if(orr!=1):
				c.create_line(x2+40,y1+10,x2+40,y1+50)
			y1+=50
			y2+=50
			orr-=1
			
			u+=1
			c.pack()
		else:
			x2+=50
			x1+=50
			u=0
			c.create_line(x1-10,y1,x2,y2)
			if(len(data)!=0 and orr==len(data)):
				print(data)
				y=data[u]
				c.create_text(x1-15,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
			elif(nd==0):
				y=data[u]
				c.create_text(x1-15,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
				u+=1
			c.create_line(x1-10,y1+15,x2,y2+15)
			c.create_line(x2,y1-8,x2,y2+24)
			c.create_arc(x2-4,y1-8,x2+19,y2+20,start=220,extent=270,fill='black',style=tk.ARC)
			c.create_line(x2+22,y1+10,x2+40,y1+10)
			if(orr!=1):
				c.create_line(x2+40,y1+10,x2+40,y1+50)
			y1+=50
			y2+=50
			orr-=1
			
			c.pack()
	temp1=nd
	cnt=1
	
	for i in list(d.keys()):
		if(d[i]==1):
			u,v=0,0
			y=data1[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',10))
			c.create_line(p1,q1+15,p2,q2+15)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_rectangle(p2-1,q1-8,p2+20,q2+23,fill='#3b5998')
			if(temp1==nd):
				c.create_line(p2+20,q1,p2+65,q1)
			else:
				c.create_line(p2+20,q1,p2+(42*cnt),q1)
				c.create_line(p2+(42*cnt),q1,p2+(42*cnt),q1-36)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data1.remove(y)
			c.pack()
			
		elif(d[i]==2):
			u,v=0,0
			y=data2[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_text(p1-5,q1+9,text=y[v],font=('Purisa',10))
			v+=1
			print(y[v])
			c.create_line(p1,q1+9,p2,q2+9)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',10))
			c.create_line(p1,q1+18,p2,q2+18)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_rectangle(p2-1,q1-8,p2+20,q2+23,fill='#3b5998')
			if(temp1==nd):
				c.create_line(p2+20,q1,p2+50,q1)
			else:
				c.create_line(p2+20,q1,p2+(42*cnt),q1)
				c.create_line(p2+(42*cnt),q1,p2+(42*cnt),q1-36)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data2.remove(y)
			c.pack()
		elif(d[i]==3):
			u,v=0,0
			y=data3[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_text(p1-5,q1+5,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1+5,p2,q2+5)
			c.create_text(p1-5,q1+10,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1+10,p2,q2+10)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',5))
			
			c.create_line(p1,q1+15,p2,q2+15)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_rectangle(p2-1,q1-8,p2+20,q2+23,fill='#3b5998')
			if(temp1==nd):
				c.create_line(p2+20,q1,p2+50,q1)
			else:
				c.create_line(p2+20,q1,p2+(42*cnt),q1)
				c.create_line(p2+(42*cnt),q1,p2+(42*cnt),q1-36)
			q1+=50
			q2+=50
			nd-=1
			u+=1
			data3.remove(y)
			cnt+=1
			c.pack()
	c.create_text(215,430,text='Fig. Probable gate diagram',anchor='s')
	root.mainloop()
	
def gnand(inp):
	l=[]
	orr=andd=[]
	# dictt=OrderedDict()
	# delimit=['+','.','^']
	# for i in delimit:
	# 	if(i not in inp):
	# 		delimit.remove(i)
	l=inp.split('+')
	# print(l)

	n=len(l)
	if(n>1):
		orr=n-1
	else:
		orr=-1
	
	nd=0
	temp=[0]*n
	d=OrderedDict()
	for i in range(n):
		if(len(l[i])>1):
			nd+=len(l[i])-1
			d[i+1]=len(l[i])-1
			s=''
			for j in l[i]:
				if(j!=l[i][-1:]):
					s+=j+'AND'
			s+=l[i][-1:]
			temp[i]=s
		else:
			temp[i]=l[i]

	# print(d)  print dictionary with index->no.of ands needed!
	# val=temp[-1:][0]
	# s=''
	# for i in temp:
	# 	# if(i!=val):
	# 	s+='('+i+')'+' OR '

	# s=s[:len(s)-4]

	# print('OR--'+str(orr)+' AND--'+str(nd))
	# print(s)

	data,data1,data2,data3=[],[],[],[]		
	for j in l:
		if(len(j)==1):
			data.append(j)
		if(len(j)==2):
			data1.append(j)
		if(len(j)==3):
			data2.append(j)
		if(len(j)==4):
			data3.append(j)

	root=Tk()
	c = Canvas(master=root, width=500, height=450, bd=0, highlightthickness=0)
	c.master.title('NAND Gates Representation')
	temp=orr
	x1,p1=165,70
	y1,q1=100,100
	x2,p2=195,100
	y2,q2=100,100
	# c=Canvas(root)
	# t=Text(root)
	c.create_line(12,25,33,25)
	c.create_line(12,38,33,38)
	c.create_rectangle(20,20,33,45,fill='#3b5998')
	c.create_oval(33,30,37,35)
	c.create_text(65,30,text=': NAND')
	
	while(orr>0):
		if(temp==orr):
			u=0
			if(nd==0):
				y=data[u]
				u+=1
				c.create_text(x1-20,y1,text=y,font=('Purisa',10))
				data.remove(y)
			c.create_line(x1-15,y1,x2-4,y2)
			if(nd==0 ):
				c.create_oval(x2-4,y1,x2,y1+4)
			if(nd==0 or len(d)<2):
				y=data[u]
				u+=1
				c.create_text(x1-20,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
			c.create_line(x1-15,y1+15,x2-4,y2+15)
			if(nd==0 or len(d)<2):
				c.create_oval(x2-4,y1+15,x2,y1+19)
			c.create_line(x2,y1-8,x2,y2+24)
			c.create_rectangle(x2-1,y1-8,x2+20,y2+23,fill='#3b5998')
			c.create_oval(x2+21,y1+5,x2+25,y1+9)
			# c.create_arc(x2-4,y1-8,x2+19,y2+20,start=220,extent=270,fill='black',style=tk.ARC)
			c.create_line(x2+26,y1+7,x2+44,y1+7)
			if(orr!=1):
				c.create_line(x2+44,y1+8,x2+44,y1+50)
			y1+=50
			y2+=50
			orr-=1
			c.pack()
		else:
			x2+=50
			x1+=50
			u=0
			c.create_line(x1-10,y1,x2,y2)
			# if(nd==0):
			c.create_oval(x2-4,y1,x2,y1+4)
			if(orr==len(data) and len(data)!=0):
				y=data[u]
				c.create_text(x1-15,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
			elif(nd==0):
				y=data[u]
				c.create_text(x1-15,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
				u+=1
			c.create_line(x1-10,y1+15,x2,y2+15)
			if(nd==0 or len(d)>=orr):
				
				c.create_oval(x2-4,y1+15,x2,y1+19)
			c.create_line(x2,y1-8,x2,y2+24)
			c.create_rectangle(x2-1,y1-8,x2+20,y2+23,fill='#3b5998')
			c.create_oval(x2+21,y1+5,x2+25,y1+9)
			c.create_line(x2+22,y1+10,x2+40,y1+10)
			if(orr!=1):
				c.create_line(x2+40,y1+10,x2+40,y1+50)
			y1+=50
			y2+=50
			orr-=1
			u+=1
			c.pack()
	temp1=nd
	cnt=1
	for i in list(d.keys()):
		if(d[i]==1):
			u,v=0,0
			y=data1[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',10))
			c.create_line(p1,q1+15,p2,q2+15)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_rectangle(p2-1,q1-8,p2+20,q2+23,fill='#3b5998')
			c.create_oval(p2+20,q1-2,p2+24,q1+2)
			if(temp1==nd):
				c.create_line(p2+24,q1,p2+65,q1)
				if(orr<0):
					c.create_oval(p2+65,q1-2,p2+69,q1+2)
			else:
				c.create_oval(p2+20,q1-2,p2+24,q1+2)
				c.create_line(p2+24,q1,p2+(42*cnt),q1)
				c.create_line(p2+(42*cnt),q1,p2+(42*cnt),q1-36)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data1.remove(y)
			c.pack()
			
		elif(d[i]==2):
			u,v=0,0
			y=data2[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_text(p1-5,q1+9,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1+9,p2,q2+9)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',10))
			c.create_line(p1,q1+15,p2,q2+15)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_rectangle(p2-1,q1-8,p2+20,q2+23,fill='#3b5998')
			if(temp1==nd):
				c.create_oval(p2+20,q1-2,p2+24,q1+2)
				c.create_line(p2+24,q1,p2+54,q1)
				if(orr<0):
					c.create_oval(p2+50,q1-2,p2+54,q1+2)
			else:
				c.create_oval(p2+20,q1-2,p2+24,q1+2)
				c.create_line(p2+20,q1,p2+(42*cnt),q1)
				c.create_line(p2+(42*cnt),q1,p2+(42*cnt),q1-36)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data2.remove(y)
			c.pack()
		elif(d[i]==3):
			u,v=0,0
			y=data3[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_text(p1-5,q1+5,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1+5,p2,q2+5)
			c.create_text(p1-5,q1+10,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1+10,p2,q2+10)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',5))
			c.create_line(p1,q1+15,p2,q2+15)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_rectangle(p2-1,q1-8,p2+20,q2+23,fill='#3b5998')
			if(temp1==nd):
				c.create_oval(p2+20,q1-2,p2+24,q1+2)
				c.create_line(p2+24,q1,p2+54,q1)
				if(orr<0):
					c.create_oval(p2+50,q1-2,p2+54,q1+2)
			else:
				c.create_oval(p2+20,q1-2,p2+24,q1+2)
				c.create_line(p2+20,q1,p2+(42*cnt),q1)
				c.create_line(p2+(42*cnt),q1,p2+(42*cnt),q1-36)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data3.remove(y)
			c.pack()
	c.create_text(215,430,text='Fig. Probable gate diagram',anchor='s')
	root.mainloop()

def gnor(inp):
	l=[]
	orr=andd=[]
	# dictt=OrderedDict()
	delimit=['+','.','^']
	# for i in delimit:
	# 	if(i not in inp):
	# 		delimit.remove(i)
	l=inp.split('+')
	# print(l)

	n=len(l)
	if(n>1):
		orr=n-1
	else:
		orr=-1
	
	nd=0
	temp=[0]*n
	d=OrderedDict()
	for i in range(n):
		if(len(l[i])>1):
			nd+=len(l[i])-1
			d[i+1]=len(l[i])-1
			s=''
			for j in l[i]:
				if(j!=l[i][-1:]):
					s+=j+'AND'
			s+=l[i][-1:]
			temp[i]=s
		else:
			temp[i]=l[i]

	# print(d)  print dictionary with index->no.of ands needed!
	# val=temp[-1:][0]
	# s=''
	# for i in temp:
	# 	# if(i!=val):
	# 	s+='('+i+')'+' OR '

	# s=s[:len(s)-4]

	# print('OR--'+str(orr)+' AND--'+str(nd))
	# print(s)

	data,data1,data2,data3=[],[],[],[]		
	for j in l:
		if(len(j)==1):
			data.append(j)
		if(len(j)==2):
			data1.append(j)
		if(len(j)==3):
			data2.append(j)
		if(len(j)==4):
			data3.append(j)

	root=Tk()
	c = Canvas(master=root, width=500, height=450, bd=0, highlightthickness=0)
	c.master.title('NOR Gates Representation')
	temp=orr
	x1,p1=165,70
	y1,q1=100,100
	x2,p2=195,100
	y2,q2=100,100
	# c=Canvas(root)
	# t=Text(root)
	c.create_line(12,25,33,25)
	c.create_line(12,38,33,38)
	c.create_polygon(20,20,33,24,33,39,20,45,fill='#a93226')
	c.create_oval(33,30,37,35)
	c.create_text(65,30,text=': NOR')
	print('nor',d)
	while(orr>0):
		if(temp==orr):
			c.create_line(x1-15,y1+4,x2-4,y2+4)
			u=0
			if(nd==0):
				y=data[u]
				u+=1
				c.create_text(x1-20,y1,text=y,font=('Purisa',10))
				data.remove(y)
			# if(nd==0):
			# 	c.create_oval(x2-4,y1,x2,y1+4)
			c.create_line(x1-15,y1+15,x2-4,y2+15)
			# if(nd==0 or len(d)<2):
			# 	c.create_oval(x2-4,y1+15,x2,y1+19)
			if(nd==0 or len(d)<2):
				y=data[u]
				u+=1
				c.create_text(x1-20,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
			c.create_line(x2,y1-8,x2,y2+24)
			c.create_polygon(x2-1,y1-8,x2+20,y1,x2+20,y2+17,x2-1,y2+25,fill='#a93226')
			c.create_oval(x2+21,y1+5,x2+25,y1+9)
			# c.create_arc(x2-4,y1-8,x2+19,y2+20,start=220,extent=270,fill='black',style=tk.ARC)
			c.create_line(x2+26,y1+7,x2+44,y1+7)
			c.create_oval(x2+43,y1+5,x2+47,y1+9)
			if(orr!=1):
				c.create_line(x2+44,y1+8,x2+44,y1+50)
			y1+=50
			y2+=50
			orr-=1
			c.pack()
		else:
			x2+=50
			x1+=50
			u=0
			c.create_line(x1-10,y1,x2,y2)
			# if(nd==0):
			# c.create_oval(x2-4,y1,x2,y1+4)
			if(orr==len(data) and len(data)!=0):
				y=data[u]
				c.create_text(x1-15,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
			elif(nd==0):
				y=data[u]
				c.create_text(x1-15,y1+15,text=y,font=('Purisa',10))
				data.remove(y)
				u+=1
			c.create_line(x1-10,y1+15,x2,y2+15)
			# if(nd==0 or len(d)>=orr):
				
			# 	c.create_oval(x2-4,y1+15,x2,y1+19)
			c.create_line(x2,y1-8,x2,y2+24)
			c.create_polygon(x2-1,y1-8,x2+20,y1,x2+20,y2+17,x2-1,y2+25,fill='#a93226')
			c.create_oval(x2+21,y1+5,x2+25,y1+9)
			c.create_line(x2+22,y1+10,x2+40,y1+10)
			c.create_oval(x2+40,y1+5,x2+44,y1+9)
			if(orr!=1):
				c.create_line(x2+40,y1+10,x2+40,y1+50)
			y1+=50
			y2+=50
			orr-=1
			u+=1
			c.pack()
	temp1=nd
	cnt=1
	for i in list(d.keys()):
		if(d[i]==1):
			u,v=0,0
			y=data1[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1,p2-4,q2)
			c.create_oval(p2-4,q1-2,p2,q1+2)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',10))
			c.create_line(p1,q1+15,p2-4,q2+15)
			c.create_oval(p2-4,q1+13,p2,q2+17)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_polygon(p2-1,q1-8,p2+20,q1,p2+20,q2+17,p2-1,q2+25,fill='#a93226')
			c.create_oval(p2+20,q1+4,p2+24,q1+8)
			if(temp1==nd):
				c.create_line(p2+24,q1+4,p2+65,q1+4)
				if(orr<0):
					c.create_oval(p2+65,q1+2,p2+69,q1+6)
			else:
				# c.create_oval(p2+24,q1+4,p2+28,q1+8)
				c.create_line(p2+24,q1+4,p2+(42*cnt),q1+4)
				c.create_line(p2+(42*cnt),q1+4,p2+(42*cnt),q1-32)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data1.remove(y)
			c.pack()
			
		elif(d[i]==2):
			u,v=0,0
			y=data2[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_oval(p2-4,q1-2,p2,q1+2)
			c.create_text(p1-5,q1+9,text=y[v],font=('Purisa',10))
			v+=1
			c.create_line(p1,q1+9,p2,q2+9)
			c.create_oval(p2-4,q1+7,p2,q2+11)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',10))
			c.create_line(p1,q1+15,p2,q2+15)
			c.create_oval(p2-4,q1+13,p2,q2+17)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_polygon(p2-1,q1-8,p2+20,q1,p2+20,q2+17,p2-1,q2+25,fill='#a93226')
			if(temp1==nd):
				c.create_oval(p2+20,q1+4,p2+24,q1+8)
				c.create_line(p2+24,q1+4,p2+54,q1+4)
				if(orr<0):
					c.create_oval(p2+54,q1+2,p2+58,q1+6)
			else:
				c.create_oval(p2+20,q1+4,p2+24,q1+8)
				c.create_line(p2+20,q1+4,p2+(42*cnt),q1+8)
				c.create_line(p2+(42*cnt),q1,p2+(42*cnt),q1-32)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data2.remove(y)
			c.pack()
		elif(d[i]==3):
			u,v=0,0
			y=data3[u]
			c.create_text(p1-5,q1,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1,p2,q2)
			c.create_text(p1-5,q1+5,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1+5,p2,q2+5)
			c.create_text(p1-5,q1+10,text=y[v],font=('Purisa',5))
			v+=1
			c.create_line(p1,q1+10,p2,q2+10)
			c.create_text(p1-5,q1+15,text=y[v],font=('Purisa',5))
			c.create_line(p1,q1+15,p2,q2+15)
			c.create_line(p2,q1-8,p2,q2+24)
			c.create_polygon(p2-1,q1-8,p2+20,q1,p2+20,q1+12,p2,q2+23,fill='#a93226')
			if(temp1==nd):
				c.create_oval(p2+20,q1-2,p2+24,q1+2)
				c.create_line(p2+24,q1,p2+54,q1)
				if(orr==0):
					c.create_oval(p2+50,q1-2,p2+54,q1+2)
			else:
				c.create_oval(p2+20,q1,p2+24,q1+4)
				c.create_line(p2+20,q1+2,p2+(42*cnt),q1+2)
				c.create_line(p2+(42*cnt),q1+2,p2+(42*cnt),q1-34)
			q1+=50
			q2+=50
			nd-=1
			cnt+=1
			u+=1
			data3.remove(y)
			c.pack()
	c.create_text(215,430,text='Fig. Probable gate diagram',anchor='s')
	root.mainloop()
	
