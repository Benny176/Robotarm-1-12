#1

# from RobotArm import RobotArm

# robotArm = RobotArm('exercise 1')

# robotArm.moveRight()
#     robotArm.grab()
#     robotArm.moveLeft()
# robotArm.drop()
# robotArm.wait()


#2

# from RobotArm import RobotArm

# robotArm = RobotArm('exercise 2')

# # Jouw python instructies zet je vanaf hier:

# robotArm.grab()
# for x in range(9):
#     robotArm.moveRight()
# robotArm.drop()

# for x in range(2):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(2):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(5):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(9):
#     robotArm.moveRight()
# robotArm.drop()
# robotArm.wait()



# 3

# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 3')

# for x in range(4):
#     robotArm.grab()
#     robotArm.moveRight()
#     robotArm.drop()
#     robotArm.moveLeft()
# robotArm.wait()


# 4

# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 4')

# robotArm.speed = 2

# for y in range(3):
#     robotArm.grab()
#     robotArm.moveRight()
#     robotArm.moveRight()
#     robotArm.drop()
#     robotArm.moveLeft()
#     robotArm.moveLeft()
# robotArm.moveRight()
# for y in range(3):
#     robotArm.moveRight()
#     robotArm.grab()
#     robotArm.moveLeft()
#     robotArm.drop()
# robotArm.wait()

#6

# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 6')

# robotArm.speed = 3   
# for y in range(7):
#     robotArm.moveRight()

# robotArm.grab()
# robotArm.moveRight()
# robotArm.drop()

# for y in range(7):
#     robotArm.moveLeft()
#     robotArm.moveLeft()
#     robotArm.grab()
#     robotArm.moveRight()
#     robotArm.drop()
# robotArm.wait()

#7
# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 7')
# for x in range(5):
#     for x in range(6):
#         robotArm.moveRight()
#         robotArm.grab()
#         robotArm.moveLeft()
#         robotArm.drop()
#     robotArm.moveRight()
#     robotArm.moveRight()
# robotArm.wait()

# 8
# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 8')
# for y in range(7):
#     robotArm.moveRight()
#     robotArm.grab()
#     for x in range(20):
#         robotArm.moveRight()
#     robotArm.drop()
#     for x in range(20):
#         robotArm.moveLeft()
# robotArm.wait()

#9
# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 9')
# for i in range(4):
#     robotArm.moveRight()
#     robotArm.grab()
# for y in range(4):
#     robotArm.moveRight()
#     robotArm.drop()
# for i in range(5):
#     robotArm.moveLeft()

# robotArm.wait()


# #10
# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 10')
# for y in range(2):
#     for y in range(2):
#         robotArm.moveRight()
#     robotArm.grab()
#     for y in range(2):
#         robotArm.moveRight()
#     robotArm.drop()
#     for y in range(3):
#         robotArm.moveLeft()
#     robotArm.grab()
# robotArm.wait()

#11
# from RobotArm import RobotArm
# robotArm = RobotArm('exercise 11')

# for x in range(7):
#     robotArm.grab()
#     colorc = robotArm.scan()

#     print(colorc)
#     if colorc == "white":
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveRight()

#     else:
#         robotArm.drop()
#         robotArm.moveRight()
# robotArm.grab()
# robotArm.wait()

#12
# from RobotArm import RobotArm

# robotArm = RobotArm('exercise 12')
# robotArm.speed = 3
# for x in range(16):
#     robotArm.grab()
#     colorc = robotArm.scan()

#     print(colorc)
#     if colorc == "red":
#         for y in range (8):
#             robotArm.moveRight()
#         robotArm.drop()
#         for y in range(6):
#             robotArm.moveLeft()
#     else:
#         robotArm.drop()
#         robotArm.moveRight()     
# robotArm.wait()










