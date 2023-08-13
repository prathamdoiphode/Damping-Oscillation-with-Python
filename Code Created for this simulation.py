#Python coding
#Code by Rajapandi
#Roll no: 423 & 431
#This is the python code for visualizing the damped oscillation by solving the differential equation as a base

#Idea of the System
# The Project is to visualize a famous physical concept "THE DAMPING OSCILLATION"
# Here in this system the rigid support is on y axis at (0,10,0)
# A spring is attached to it and a cube(bob) is attached at the other end of the spring
# We have designed a default system in case the user is new to this concept

from vpython import*
import matplotlib.pyplot as ra

#Function func is defined such that it solves he functional part while solving the differential equation
#This function takes 5 inputs and returns d after completing the operation
def func(k,m,b,x,v):
  d = (k/m)*x-(b/m)*v
  return d
def fun(k,m,b,x,v):
  d = -(k/m)*x - (b/m)*v
  return d
#Here we have displayed some of the instruction for visualizing the system
#Major instructions are regarding the input values that an user should input
print()
print('Created by Roll no : 423 & 431')
print('Welcome to the simulation of the spring mass oscillator')
print()
print()
print('Description : The spring mass oscillator system is pivoted at y axis at (0,10,0)')

print(' we have created the system such that we obtain equilibrium position at origin')
print(' we will take inputs of the position of bob from the user for initializing the oscillation ')
print(' inputs for the bobs position should be in the range 9 to - 9 for witnessing an undistorted oscillation ')
print()
print('WARNING IF YOU DO NOT HAVE ANY SPECIFIC VALUES FOR THE INPUTS PLEASE ENTER 0 ')
print('===============================================================================================================')

# Main part of the code which is used to control the motion of the bob
while True: # While True loop is used for continuously asking inputs from user if the input value is not in the desired form
# try and expect is used in order to control the value error that the user may come across
  try:
  # Taking input from the user for the position of the bob , damping constant and force constant of the spring
    x = float(input('Enter the position of the bob in y axis: '))
    b = float(input('Enter the damping constant: '))
    k = float(input('Enter the force constant of the spring: '))

    # Creating the default values for each of the inputs taken by the user this will be executed if the input entered is 0
    if x == 0:
      x=-5
    if b == 0:
      b = 0
    if k == 0:
      k = 8

    # Defining three arrays for collecting data for plotting the graph of time vs displacement
    y = [x]
    t = [0]
    v = [0]

    # Defining time interval of the oscillation
    ti = 0
    tf = 500
    n = 150000
    dt = (tf - ti) / n
    # Defining the system with the appropriate dimensions
    eq=vector(0,0,0)
    # Wall is the rigid support in the system
    wall=box(pos=vector(0,10,0),size=vector(3,0.3,2),color=color.white)
    # bob with all the attributes like position, mass and velocity
    bob=box(pos=vector(0,x,0),velocity=vector(0,0,0),size=vector(1,1,1),mass=10.0,color=color.blue)
    ref=box(pos=vector(-5,0,0),size=vector(10,0.2,2),color=color.red)
    # pivot is defined for the fixed end of the spring
    pivot=vector(0,10,0)
    # spring with all the attributes such as force constant & damping constant

    spring=helix(pos=pivot,axis=bob.pos-pivot,radius=0.4,constant=k,thickness=0.1,coils=15,dampingconst=b,color=color.white)
    # This part is for plotting the graph of the damping oscillation along side the model to get a great connect between the graph and the model
    j = 1
    while j < n:
      v1 = v[j-1] + dt * fun(k,10,b,y[j-1],v[j-1])
      v.append(v1)
      y1 = y[j-1] + dt*v[j-1]
      y.append(y1)
      t1 = t[j-1] + dt
      t.append(t1)
      j += 1
   # Plotting the graph
    ra.plot(t, y)
    ra.xlabel('Time')
    ra.ylabel('Displacement')
    ra.title('Time vs Displacement graph with damping')

    ra.show()


    # This part of the code is for solving the second order differential equation by euler's method
    # The solution is obtained here by breaking second order differential equation into two different first order differential equations
    # One of the differential equation is (x'[i] = x'[i-1] + dt*function)
    # The second differential equation is (x[i] = x[i-1] + dt*function)
    i=1
    while i < n:
      rate(1000)
      bob.velocity = bob.velocity +dt*func(spring.constant,bob.mass,spring.dampingconst,eq-bob.pos,bob.velocity)
      bob.pos = bob.pos + dt * bob.velocity
      y.append(bob.pos)
      spring.axis = bob.pos - spring.pos
      i = i+1



  except ValueError:
    print('Only numbers are allowed....')
    print('Please enter only numbers....')
    print('Try again')
    print('------------------------------------------------------------------------------------------------------')
  else:
    break


