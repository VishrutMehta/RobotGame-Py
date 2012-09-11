from curses import initscr,curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP,init_pair,color_pair,start_color,use_default_colors,COLOR_RED,COLOR_GREEN,COLOR_BLUE,COLOR_WHITE,COLOR_CYAN,A_BOLD
from random import randrange
count=0
print 'Select level(1,2,3):'
lev=input()
print "Enter the no of defuse codes:"
my=input()
key=KEY_RIGHT
initscr()
class box1():
	pass
def robot1(listing):
	b=box1()
	b.length=3;#change
	b.breadth=3;#c
	b.startx=listing[0]
	b.starty=listing[1] 
	b.list1=[b.startx,b.starty,b.startx+b.length,b.starty+b.breadth]
	def length():
		return b.length
	def breadth():
		return b.breadth
	def list1():
		return b.list1
	def xstart():
		return b.startx
	def ystart():
		return b.starty
	def move(newlist):
	 	b.startx=newlist[0]
		b.starty=newlist[1]
		b.list1=[b.startx,b.starty,b.startx+b.length,b.starty+b.breadth]
	a=box1()
	a.length=length
	a.breadth=breadth
	a.list1=list1
	a.move=move
	a.xstart=xstart
	a.ystart=ystart
	return a
robot = robot1([10,15])
win=newwin(20,70,0,0)
class A():		    
	def start1(no):
			global win
			start_color()
			use_default_colors()
			curs_set(0)
			#win = newwin(16,60,10,30)
			win.keypad(1)
			win.nodelay(1)
			win.border('|','|','_','_','@','@','@','@')
			#count=0
			init_pair(2,COLOR_GREEN,-1)
			init_pair(3,COLOR_BLUE,-1)
			c = [n for n in [[randrange(1,68,1),randrange(1,18,1)] for x in xrange(0,no)]]
			for i in xrange(0,no):
				win.addch(c[i][1],c[i][0],'d',color_pair(2))
			d=[n for n in [[randrange(1,68,1),randrange(1,18,1)] for x in xrange(0,1)] if n not in c]
			init_pair(1, COLOR_RED,-1)
			win.addch(d[0][1],d[0][0],'B',color_pair(1))
		#key=KEY_RIGHT
	def game1(speed,no):
		global key
		global count
		global win
		global robot
		y1=win.inch(robot.ystart(),robot.xstart())
		y2=win.inch(robot.ystart(),robot.xstart()+1)
		y3=win.inch(robot.ystart(),robot.xstart()+2)
		y4=win.inch(robot.ystart(),robot.xstart()+3)
		y5=win.inch(robot.ystart()+1,robot.xstart())
		y6=win.inch(robot.ystart()+2,robot.xstart())
		y7=win.inch(robot.ystart()+3,robot.xstart())
		y8=win.inch(robot.ystart()+1,robot.xstart()+3)
		y9=win.inch(robot.ystart()+2,robot.xstart()+3)
		y10=win.inch(robot.ystart()+3,robot.xstart()+3)
		y11=win.inch(robot.ystart()+3,robot.xstart()+1)
		y12=win.inch(robot.ystart()+3,robot.xstart()+2)
		while key != 27:
			    if(key==112 or key==80):
				    pass
			    win.addstr(0,18,' Defused codes: '+ str(count) +' ')
			    win.timeout(speed) 
			    getkey = win.getch() 
			    key = key if getkey==-1 else getkey
			    new=[robot.xstart()+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), robot.ystart()+(key==KEY_DOWN and 1 or key==KEY_UP and -1)]
			    for i in range(4):
				    for j in range(4):
					    win.addch(robot.ystart()+i,robot.xstart()+j,' ')
			    robot.move(new)
			    y1=win.inch(robot.ystart(),robot.xstart())
			    y2=win.inch(robot.ystart(),robot.xstart()+1)
			    y3=win.inch(robot.ystart(),robot.xstart()+2)
			    y4=win.inch(robot.ystart(),robot.xstart()+3)
			    y5=win.inch(robot.ystart()+1,robot.xstart())
			    y6=win.inch(robot.ystart()+2,robot.xstart())
			    y7=win.inch(robot.ystart()+3,robot.xstart())
			    y8=win.inch(robot.ystart()+1,robot.xstart()+3)
			    y9=win.inch(robot.ystart()+2,robot.xstart()+3)
			    y10=win.inch(robot.ystart()+3,robot.xstart()+3)
			    y11=win.inch(robot.ystart()+3,robot.xstart()+1)
			    y12=win.inch(robot.ystart()+3,robot.xstart()+2)
			    if ((y1 & 255 == 32) and (y2 & 255==32) and (y3 & 255==32) and (y4 & 255==32)and(y5 & 255 == 32) and (y6 & 255==32) and (y7 & 255==32) and (y8 & 255==32)and(y9 & 255 == 32) and (y10 & 255==32) and (y11 & 255==32) and (y12 & 255==32)): robot.move(new)
			    elif ((y1 & 255 == ord('B')) or (y2 & 255==ord('B')) or (y3 & 255==ord('B')) or (y4 & 255==ord('B'))or(y5 & 255 == ord('B')) or (y6 & 255==ord('B')) or (y7 & 255==ord('B')) or (y8 & 255==ord('B'))or(y9 & 255 == ord('B')) or (y10 & 255==ord('B')) or (y11 & 255==ord('B')) or (y12 & 255==ord('B'))) :
				    if(count<no):
					    break
				    if(count==no):
					    break
			    elif ((y1 & 255 == ord('d')) or (y2 & 255==ord('d')) or (y3 & 255==ord('d')) or (y4 & 255==ord('d'))or(y5 & 255 == ord('d')) or (y6 & 255==ord('d')) or (y7 & 255==ord('d')) or (y8 & 255==ord('d'))or(y9 & 255 == ord('d')) or (y10 & 255==ord('d')) or (y11 & 255==ord('d')) or (y12 & 255==ord('d'))):
				    count=count+1
				    robot.move(new)
			    else:
				 break
			    listing=robot.list1()
			    startx1=listing[0]
			    starty1=listing[1]
			    startx2=listing[2]
			    starty2=listing[3]
			    win.addstr(starty1,startx1,' @@ ',color_pair(3))
			    win.addstr(starty1+1,startx1,'|  |',color_pair(3))
			    win.addstr(starty1+2,startx1,' || ',color_pair(3))
			    win.addstr(starty1+3,startx1,'v  v',color_pair(3))
	def start2(no):
		global win
		start_color()
		use_default_colors()
		curs_set(0)
		#win = newwin(16,60,10,30)
		win.keypad(1)
		win.nodelay(1)
		win.border('|','|','_','_','@','@','@','@')
		#count=0
		init_pair(2,COLOR_GREEN,-1)
		init_pair(3,COLOR_BLUE,-1)
		init_pair(4,COLOR_WHITE,COLOR_WHITE)
		k=[[9,5],[9,6],[9,7],[9,8],[9,9]]
		for i in xrange(0,5):
			win.addch(k[i][1],k[i][0],'l',color_pair(4))
		kk=[[50,5],[50,6],[50,7],[50,8],[50,9]]
		for i in xrange(0,5):
			win.addch(kk[i][1],kk[i][0],'l',color_pair(4))
		c = [n for n in [[randrange(1,68,1),randrange(1,18,1)] for x in xrange(0,no)] if n not in k and n not in kk]
		for i in xrange(0,no):
			win.addch(c[i][1],c[i][0],'d',color_pair(2))
		d=[n for n in [[randrange(1,68,1),randrange(1,18,1)] for x in xrange(0,1)] if n not in c and n not in k and n not in kk]
		init_pair(1, COLOR_RED,-1)
		win.addch(d[0][1],d[0][0],'B',color_pair(1))
	def game2(speed,no):
		global key
		global count
		global win
		global robot
		y1=win.inch(robot.ystart(),robot.xstart())
		y2=win.inch(robot.ystart(),robot.xstart()+1)
		y3=win.inch(robot.ystart(),robot.xstart()+2)
		y4=win.inch(robot.ystart(),robot.xstart()+3)
		y5=win.inch(robot.ystart()+1,robot.xstart())
		y6=win.inch(robot.ystart()+2,robot.xstart())
		y7=win.inch(robot.ystart()+3,robot.xstart())
		y8=win.inch(robot.ystart()+1,robot.xstart()+3)
		y9=win.inch(robot.ystart()+2,robot.xstart()+3)
		y10=win.inch(robot.ystart()+3,robot.xstart()+3)
		y11=win.inch(robot.ystart()+3,robot.xstart()+1)
		y12=win.inch(robot.ystart()+3,robot.xstart()+2)
		while key != 27:
			    if(key==112 or key==80):
				    pass
			    win.addstr(0,18,' Defused codes: '+ str(count) +' ')
		   	    win.timeout(speed) 
		    	    getkey = win.getch() 
        	   	    key = key if getkey==-1 else getkey
		  	    new=[robot.xstart()+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), robot.ystart()+(key==KEY_DOWN and 1 or key==KEY_UP and -1)]
			    for i in range(4): #change this 2 if u change robot's length
				for j in range(4):
	 		    		win.addch(robot.ystart()+i,robot.xstart()+j,' ')
		
			    robot.move(new)
			    y1=win.inch(robot.ystart(),robot.xstart())
			    y2=win.inch(robot.ystart(),robot.xstart()+1)
			    y3=win.inch(robot.ystart(),robot.xstart()+2)
		            y4=win.inch(robot.ystart(),robot.xstart()+3)
			    y5=win.inch(robot.ystart()+1,robot.xstart())
			    y6=win.inch(robot.ystart()+2,robot.xstart())
			    y7=win.inch(robot.ystart()+3,robot.xstart())
			    y8=win.inch(robot.ystart()+1,robot.xstart()+3)
			    y9=win.inch(robot.ystart()+2,robot.xstart()+3)
			    y10=win.inch(robot.ystart()+3,robot.xstart()+3)
			    y11=win.inch(robot.ystart()+3,robot.xstart()+1)
			    y12=win.inch(robot.ystart()+3,robot.xstart()+2)
			    if ((y1 & 255 == 32) and (y2 & 255==32) and (y3 & 255==32) and (y4 & 255==32)and(y5 & 255 == 32) and (y6 & 255==32) and (y7 & 255==32) and (y8 & 255==32)and(y9 & 255 == 32) and (y10 & 255==32) and (y11 & 255==32) and (y12 & 255==32)): robot.move(new)
	   		    elif ((y1 & 255 == ord('B')) or (y2 & 255==ord('B')) or (y3 & 255==ord('B')) or (y4 & 255==ord('B'))or(y5 & 255 == ord('B')) or (y6 & 255==ord('B')) or (y7 & 255==ord('B')) or (y8 & 255==ord('B'))or(y9 & 255 == ord('B')) or (y10 & 255==ord('B')) or (y11 & 255==ord('B')) or (y12 & 255==ord('B'))) :
				if(count<no):
					break
		    		if(count==no):
		   			break
		   	    elif ((y1 & 255 == ord('d')) or (y2 & 255==ord('d')) or (y3 & 255==ord('d')) or (y4 & 255==ord('d'))or(y5 & 255 == ord('d')) or (y6 & 255==ord('d')) or (y7 & 255==ord('d')) or (y8 & 255==ord('d'))or(y9 & 255 == ord('d')) or (y10 & 255==ord('d')) or (y11 & 255==ord('d')) or (y12 & 255==ord('d'))):
				 count=count+1
				 robot.move(new)
	 		    else:
				 break
#	   		    for i in range(2): #change this tooo#
#				for j in range(2):#
#					win.addch(robot.ystart()+i,robot.xstart()+j,'R',color_pair(3))#
			    listing=robot.list1()
			    startx1=listing[0]
			    starty1=listing[1]
			    startx2=listing[2]
			    starty2=listing[3]
			    win.addstr(starty1,startx1,' @@ ',color_pair(3))
			    win.addstr(starty1+1,startx1,'|  |',color_pair(3))
			    win.addstr(starty1+2,startx1,' || ',color_pair(3))
			    win.addstr(starty1+3,startx1,'v  v',color_pair(3))
	def start3(no):
		global win
		start_color()
		use_default_colors()
		curs_set(0)
		#win = newwin(16,60,10,30)
		win.keypad(1)
		win.nodelay(1)
		win.border('|','|','_','_','@','@','@','@')
		#count=0
		init_pair(2,COLOR_GREEN,-1)
		init_pair(3,COLOR_BLUE,-1)
		init_pair(4,COLOR_WHITE,COLOR_WHITE)
		init_pair(5,COLOR_CYAN,COLOR_CYAN)
		k=[[9,5],[9,6],[9,7],[9,8],[9,9]]
		for i in xrange(0,5):
			win.addch(k[i][1],k[i][0],'l',color_pair(5))
		kk=[[50,10],[50,11],[50,12],[50,13],[50,14]]
		for i in xrange(0,5):
			win.addch(kk[i][1],kk[i][0],'l',color_pair(5))
		c = [n for n in [[randrange(1,68,1),randrange(1,18,1)] for x in xrange(0,no)] if n not in k and n not in kk]
		for i in xrange(0,no):
			win.addch(c[i][1],c[i][0],'d',color_pair(2))
		d=[n for n in [[randrange(1,68,1),randrange(1,18,1)] for x in xrange(0,1)] if n not in c and n not in k and n not in kk]
		init_pair(1, COLOR_RED,-1)
		m=[n for n in [[randrange(1,68,1),randrange(1,18,1)] for x in xrange(0,4)] if n not in k and n not in c and n not in kk]
		for i in range(4):
			win.addch(m[i][1],m[i][0],'*',A_BOLD)
		win.addch(d[0][1],d[0][0],'B',color_pair(1))
	def game3(speed,no):
		global key
		global count
		global win
		global robot
		y1=win.inch(robot.ystart(),robot.xstart())
		y2=win.inch(robot.ystart(),robot.xstart()+1)
		y3=win.inch(robot.ystart(),robot.xstart()+2)
		y4=win.inch(robot.ystart(),robot.xstart()+3)
		y5=win.inch(robot.ystart()+1,robot.xstart())
		y6=win.inch(robot.ystart()+2,robot.xstart())
		y7=win.inch(robot.ystart()+3,robot.xstart())
		y8=win.inch(robot.ystart()+1,robot.xstart()+3)
		y9=win.inch(robot.ystart()+2,robot.xstart()+3)
		y10=win.inch(robot.ystart()+3,robot.xstart()+3)
		y11=win.inch(robot.ystart()+3,robot.xstart()+1)
		y12=win.inch(robot.ystart()+3,robot.xstart()+2)
		while key != 27:
			    if(key==112 or key==80):
				    pass
			    win.addstr(0,18,' Defused codes: '+ str(count) +' ')
	   		    win.timeout(speed) 
	    		    getkey = win.getch() 
           		    key = key if getkey==-1 else getkey
	  		    new=[robot.xstart()+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), robot.ystart()+(key==KEY_DOWN and 1 or key==KEY_UP and -1)]
			    for i in range(4): #change this 2 if u change robot's length
				for j in range(4):
	 		    		win.addch(robot.ystart()+i,robot.xstart()+j,' ')
			    robot.move(new)
			    y1=win.inch(robot.ystart(),robot.xstart())
			    y2=win.inch(robot.ystart(),robot.xstart()+1)
			    y3=win.inch(robot.ystart(),robot.xstart()+2)
	     		    y4=win.inch(robot.ystart(),robot.xstart()+3)
			    y5=win.inch(robot.ystart()+1,robot.xstart())
			    y6=win.inch(robot.ystart()+2,robot.xstart())
			    y7=win.inch(robot.ystart()+3,robot.xstart())
			    y8=win.inch(robot.ystart()+1,robot.xstart()+3)
			    y9=win.inch(robot.ystart()+2,robot.xstart()+3)
			    y10=win.inch(robot.ystart()+3,robot.xstart()+3)
			    y11=win.inch(robot.ystart()+3,robot.xstart()+1)
			    y12=win.inch(robot.ystart()+3,robot.xstart()+2)
			    if ((y1 & 255 == 32) and (y2 & 255==32) and (y3 & 255==32) and (y4 & 255==32)and(y5 & 255 == 32) and (y6 & 255==32) and (y7 & 255==32) and (y8 & 255==32)and(y9 & 255 == 32) and (y10 & 255==32) and (y11 & 255==32) and (y12 & 255==32)): robot.move(new)
	   		    elif ((y1 & 255 == ord('B')) or (y2 & 255==ord('B')) or (y3 & 255==ord('B')) or (y4 & 255==ord('B'))or(y5 & 255 == ord('B')) or (y6 & 255==ord('B')) or (y7 & 255==ord('B')) or (y8 & 255==ord('B'))or(y9 & 255 == ord('B')) or (y10 & 255==ord('B')) or (y11 & 255==ord('B')) or (y12 & 255==ord('B'))) :
				if(count<no):
					break
			    	if(count==no):
			   		break
			    elif ((y1 & 255 == ord('d')) or (y2 & 255==ord('d')) or (y3 & 255==ord('d')) or (y4 & 255==ord('d'))or(y5 & 255 == ord('d')) or (y6 & 255==ord('d')) or (y7 & 255==ord('d')) or (y8 & 255==ord('d'))or(y9 & 255 == ord('d')) or (y10 & 255==ord('d')) or (y11 & 255==ord('d')) or (y12 & 255==ord('d'))):
				 count=count+1
				 robot.move(new)
	 		    else:
				 break
#	   	    for i in range(2): #change this tooo#
#			for j in range(2):#
#				win.addch(robot.ystart()+i,robot.xstart()+j,'R',color_pair(3))#
			    listing=robot.list1()
			    startx1=listing[0]
			    starty1=listing[1]
			    startx2=listing[2]
			    starty2=listing[3]
			    win.addstr(starty1,startx1,' @@ ',color_pair(3))
			    win.addstr(starty1+1,startx1,'|  |',color_pair(3))
			    win.addstr(starty1+2,startx1,' || ',color_pair(3))
			    win.addstr(starty1+3,startx1,'v  v',color_pair(3))
	if(lev==1):
	#level 1
		start1(my)
		game1(160,my)
	if(lev==2):
		start2(my)
		game2(120,my)
	if(lev==3):
		start3(my)
		game3(100,my)
	endwin()
	if(count==my):
		print 'Successfully decoded the bomb!!yay!!'
		print 'U WIN :D :)'
		print 'Defused Codes: '+ str(count)
	else:
		print 'Failed to defuse the bomb :('
		print 'Defused Codes: '+ str(count)
a=A()
