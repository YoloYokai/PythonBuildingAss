
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10233121
#    Student name: Joshua Rowley
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *
from random import randint

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#

# Erect buildings as per the provided city plan
def build_city(plan):
    
    for buildingnum in range(len(plan)):
        raw_data = plan[buildingnum]
        site = raw_data[0]
        btype = raw_data[1]
        floors = raw_data[2]
        part_b = raw_data[3]
        colormode(255)

        #check if part B is true or false
        if(part_b=="X"):
            state=False
        elif(part_b=="O"):
            state=True
            
        #check which building type to create
        goto(sites[site-1][1][0],sites[site-1][1][1])
        if(btype=="A"):
            buildinga(floors,state)
        if(btype=="B"):
            buildingb(floors,state)
        if(btype=="C"):
            buildingc(floors,state)
        if(btype=="D"):
            buildingd(floors,state)

#create a rectangle with the turtle starting from the base ending at the top
def building_rectangle(l,h,oc="black",w=1,f="false",fc="black"):
    width(w)
    pd()
    seth(0)
    pencolor(oc)
    fillcolor(fc)
    forward(l/2)
    seth(90)
    if(f=="true"):
        begin_fill()
    pd()
    forward(h)
    left(90)
    forward(l)
    left(90)
    forward(h)
    left(90)
    forward(l/2)
    #checks if fill is true then fills 
    if(f=="true"):
        end_fill()
    pu()
    left(90)
    forward(h)
    seth(0)
#define the function to create the smoke function
def smoke(size,count):
	color = 255
	seth(90)
	for cloud in range(count):
		color -= 255//count
		dot(size,(color,color,color))
		direction = randint(1,2)
		if direction == 1:
			left(randint(0,30))
		elif direction == 2:
			right(randint(0,30))
		forward(size-2)


#arch with varying width and heights used for the leaning tower building    
def arch(width,height):
    pd()
    begin_fill()
    forward(width/2)
    seth(90)
    forward(height-width)
    circle(width/2,180)
    forward(height-width)
    seth(0)
    forward(width/2)
    end_fill()
    pu()
    fd(width/2)

#arch with a grey fill and set width based on height used as a door
def arch_door(height):
    fillcolor("grey")
    begin_fill()
    pd()
    fd(height/2)
    seth(90)
    fd(height/2)
    circle(height/2,180)
    fd(height/2)
    seth(0)
    fd(height/2)
    end_fill()
    pu()

#function to create a window with a cross section
def lmwindow(l,h,oc="black",w=1,f="false",fc="black"):
    pd()
    width(w)
    pencolor(oc)
    fillcolor(fc)
    seth(-90)
    begin_fill()
    fd(h/2)
    seth(0)
    fd(l)
    seth(90)
    fd(h)
    seth(180)
    fd(l)
    seth(-90)
    fd(h/2)
    end_fill()
    seth(0)
    fd(l/2)
    seth(-90)
    bk(h/2)
    fd(h)
    bk(h/2)
    seth(0)
    fd(l/2)
    pu()

#function to set angles based on floor count
def beam_angle(floors):
    if(floors==10) or (floors==6):
        return(80)
    elif(floors==9):
        return(45)
    elif(floors==8):
        return(60.5)
    elif(floors==7):
        return(75)
    elif(floors==5):
        return(82)
    elif(floors==4):
        return(66.3)
    elif(floors==3):
        return(57)
    elif(floors==1):
        return(0)
    elif(floors==2):
        return(52)

#function to create randomised floors for building A 
def randfloors(floors,bwidth,midpoints):
    global middle_of_floor
    
    colormode(255)
    floor_width=randint(2,115)
    height = 40
    fd(floor_width/2)
    right_corner = pos()
    bk(floor_width)
    left_corner = pos()
    fd(bwidth/2)
    x_base = round(xcor())
    y_base = round(ycor())
    #repeats the creation of the floors 
    for floor_count in range(floors):
        floor_width=randint(2,115)
        rand_color =(randint(0,255),randint(0,255),randint(0,255))
        fillcolor(rand_color)
        pencolor(rand_color)
        subtracted_amount=115-floor_width/2
        lower_range = round(x_base-subtracted_amount)
        upper_range = round(x_base+subtracted_amount)
        building_x = randint(lower_range,upper_range)
        building_y = round(y_base + height * (floor_count+1))
        goto(building_x,building_y)
        middle_of_floor = pos()
        midpoints += [pos()]
        seth(0)
        pu()
        fd(floor_width/2)
        top_right = pos()
        bk(floor_width)
        top_left = pos()
        begin_fill()
        pd()
        goto(left_corner)
        goto(right_corner)
        goto(top_right)
        goto(top_left)
        pu()
        end_fill()
        left_corner=top_left
        right_corner=top_right
    pu()
    goto(midpoints[0])
    pd()
    width(5)
    #draw the streak down the centre of the buildings
    for midpointcount in range(len(midpoints)):
        pencolor((randint(0,255),randint(0,255),randint(0,255)))
        goto(midpoints[midpointcount])
    pu()
    
#function to create squares centred on the turtle for the portal door
def csquare(l,oc="black",r=0,w=1,f="true",fc="black"):
    pu()
    seth(r)
    forward(l/2)
    seth(90+r)
    width(w)
    pencolor(oc)
    fillcolor(fc)
    if(f=="true"):
        begin_fill()
    pd()
    forward(l/2)
    for _ in range (3):
        left(90)
        forward(l)
    left(90)
    forward(l/2)
    if(f=="true"):
        end_fill()
    pu()
    left(90)
    forward(l/2)
    seth(0)
    
def buildinga(floors,part_b):
    global middle_of_floor
    midpoints=[]
    rand_color=(randint(0,255),randint(0,255),randint(0,255))
    bwidth=60
    height=40
    base = pos()
    midpoints+=[pos()]
    pu()
    randfloors(floors,bwidth,midpoints)
    #draw portal door
    goto(base)
    pu()
    seth(towards(midpoints[1]))
    fd(height/2)
    seth(0)
    rot=0
    size=0
    tracer_skip = True
    #checks for tracer true or false to skip the creation of the portal as it is very long 
    if not(tracer()):
        tracer_skip = False
    if(tracer_skip):
        tracer(False)
    for _ in range(360):
        rand_color =(randint(0,255),randint(0,255),randint(0,255))
        csquare((height/1.5)-size,fc=rand_color,oc=rand_color,r=rot,f="false")
        rot += 1
        size += (height/1.5)/360
    if(tracer_skip):
        tracer(True)
    width(1)
    pencolor("black")
    pu()
    goto(middle_of_floor)
    #checks if part b is x or o
    if part_b:
        seth(-90)
        fd(8)
        seth(0)
        fillcolor("white")
        pencolor("black")
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        seth(90)
        fd(5)
        seth(0)
        #creates the clock face
        for _ in range(12):
            dot(5)
            circle(25,extent=30)
        width(4)
        seth(90)
        fd(25)
        dot(6)
        clock_middle = pos()
        seth(randint(0,359))
        pd()
        fd(20)
        pu()
        goto(clock_middle)
        pd()
        seth(randint(0,359))
        fd(15)
        pu()
    else:
    	#under construction
        smoke(15,15)
#building B function
def buildingb(floors,part_b):
    width=150
    height=40
    base=pos()
    building_rectangle(width,height,oc="black",fc="white",f="true")
    top=pos()
    pu()
    goto(base)
    bk(46)
    for _ in range(3):
        arch_door(40)
        fd(46)
    pu()
    goto(top) 
    setheading(0)
    fc="light grey"
    #floor creation loop
    for floor in range(floors-1):
        forward(5)
        base=pos()
        building_rectangle(width,height,oc="black",fc="white",f="true")
        top=pos()
        pu()
        goto(base)
        bk(70)
        fd(6)
        #creates arches and alternates colours  
        for arches in range (7):
            if fc == "white":
                fillcolor("light grey")
                fc="light grey"
            elif fc == "light grey":
                fillcolor("white")
                fc="white"
            arch(22,48)
            forward(10.2)
        goto(top)
        #checks if part B is True
    if part_b:
        fillcolor("light grey")
        begin_fill()
        pd()
        base=pos()
        building_rectangle(75,50,fc="white",f="true")
        top=pos()
        pu()
        goto(base)
        arch_door(50)
        goto(top)
        pd()
        building_rectangle(75,6,oc="light grey",fc="light grey",w=4,f="true")
    else:
    	#under construction
        smoke(15,10)

#function for building C
def buildingc(floors,part_b):
    bwidth=200
    height=50
    base=pos()
    building_rectangle(bwidth,height,oc="black",fc="light grey",f="true",w=1)
    top=pos()
    bk(bwidth/2-10)
    bottom_left_corner=pos()
    pu()
    goto(base)
    building_rectangle(40,45,f="true",w=1,fc="grey")
    pd()
    goto(base)
    pu()
    goto(top)
    # floor loop to create each floor 
    for floor in range(floors-1):
        bwidth-=20
        base=pos()
        building_rectangle(bwidth,height,oc="black",f="true",fc="white",w=0)
        top=pos()
        goto(base)
        seth(90)
        fd(height/2)
        seth(180)
        fd((bwidth/2))
        for window in range(bwidth//20):
            lmwindow(20,40,oc="grey",fc="light grey",w=1)
        goto(top)
    pu()
    goto(bottom_left_corner)
    pd()
    seth(90)
    #put an outline around the building to make it stand out 
    for floor in range(floors-1):
        fd(50)
        seth(0)
        fd(10)
        seth(90)
    seth(0)
    fd(bwidth-20)
    for floor in range(floors-1):
        fd(10)
        seth(-90)
        fd(50)
        seth(0)
    pu()
    goto(top)
    if part_b:
        base=pos()
        building_rectangle(bwidth,2,oc="black",fc="grey",f="true",w=1)
        top=pos()
        building_rectangle(2,30,oc="black",fc="black",f="true",w=1)
        dot(15,"orange")
    else:
    	#under construction
        smoke(15,10)

    
        
    
def buildingd(floors,part_b):
    speed=2
    width=200
    angle=beam_angle(floors)
    angle_inverse=(90-angle)*2+angle
    beam_width=1
    height=50
    beama=True
    beamb=True
    # turns off the beams if only the ground floor is present 
    if(floors==1):
        beama=False
        beamb=False
        
    centre_base = xcor()
    edge_right = centre_base + width/2
    edge_left = centre_base - width/2
    foundation=pos()
    building_rectangle(width,height,oc="black",f="true",fc="light grey")
    top=pos()
    base_top=ycor()
    pu()
    goto(foundation)
    bk(width/8)
    seth(0)
    building_rectangle(150,50,f="true",fc="light cyan")
    pu()
    goto(foundation)
    fd((width/8)*3)
    seth(90)
    pd()
    fd(height)
    bk(height/2)
    pu()
    seth(0)
    fd(5)
    dot(5)
    bk(10)
    dot(5)  
    pu()
    goto(top)
    pencolor("grey")
    for floor in range(floors-1):
        building_rectangle(width,height,oc="black",f="true",fc="light blue")
        top=pos()
    roof=ycor()
    bk((width/2)-beam_width/2)
    pd()
    pensize(beam_width)
    seth(-(angle))
    direction=1
    angle_inverse=(90-angle)*2+angle
    #creates the beams from the top left 
    while (beama==True):
       forward(speed)
       if(direction==1):
           if(xcor()<round(edge_right)):
               if (ycor()<=base_top):
                   seth(angle)
               elif(ycor()>=roof):
                   seth(-(angle))
           if(xcor()>round(edge_right)):
               direction=2
               seth(-(angle_inverse))
       elif(direction==2):
           if(xcor()>round(edge_left)):
               if (ycor()<=base_top):
                   seth(angle_inverse)
               elif(ycor()>=roof):
                   seth(-(angle_inverse))
           if(xcor()<=round(edge_left)):
               beama=False
    pu()
    goto(top)
    seth(0)
    fd(width/2-beam_width/2)
    pd()
    pd()
    direction = 1
    seth(-(angle_inverse))
    #creates the beams from the top right corner
    while (beamb==True):
       forward(speed)
       if(direction==1):
           if(xcor()>round(edge_left)):
               if (ycor()<base_top):
                   seth(angle_inverse)
               elif(ycor()>roof):
                   seth(-(angle_inverse))
           if(xcor()<round(edge_left)):
               direction=2
               seth(-(angle))
       elif(direction==2):
           if(xcor()>round(edge_left)):
               if (ycor()<=base_top):
                   seth(angle)
               elif(ycor()>=roof):
                   seth(-(angle))
           if(xcor()>round(edge_right)):
               beamb=False
    pu()
    goto(top)
    if part_b:
   		#checks if part b is an X or O and acts accordingly 
        building_rectangle(width,10,oc="black",fc="grey",f="true")
        bk(width/4)
        building_rectangle((width/4),30,f="true",fc="light grey")
        pu()
    else:
     	#under construction
        smoke(15,10)

        
    
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas(False)

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Buildings and stuff by Joshua Rowley")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.

#build_city(fixed_plan_19) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas(True)

#
#--------------------------------------------------------------------#

