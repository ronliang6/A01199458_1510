"""Calculate cans of paint needed to paint a room given variables"""

COVERAGE = 400
print("please enter the length of your room in feet")
length_feet = float(input())
print("please enter the width of your room in feet")
width_feet = float(input())
print("please enter the height of your room in feet")
height_feet = float(input())
print("please enter the number of coats of paints for your room")
coats = float(input())

surface_area = (width_feet * length_feet) + (2 * length_feet * height_feet) + (2 * width_feet * height_feet)
coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed/COVERAGE
print("To paint your room, you need to purchase " + str(cans_of_paint_required) + " cans of paint.")
