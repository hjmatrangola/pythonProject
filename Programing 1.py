# Team Members: Hannah Matrangola
# Course: CS151, Prof. Mehri
# Date: 9/27/21
# Programming Assignment: 1
# Program Inputs: lenght, width, and hight of a room in feet
# Program Outputs: Total area, gallons of primer, gallons of paint
floor_length = float(input ("Enter the length of the floor in ft: "))

floor_width = float(input ("Enter the width of the floor in ft: "))

room_hight = float(input ("Enter the hight of the room in ft: "))


total_area = (floor_length * floor_width * room_hight)

floor_area = floor_length * floor_width

painted_area = total_area - floor_area

print ("Area painted in sq ft = ", painted_area)

Primer = painted_area / 200
print ("gallons of primer needed: ", Primer)
Paint = painted_area / 350
print ("gallons of paint needed: ", Paint)