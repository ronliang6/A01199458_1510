"""Calculate area and radius of a circle with given radius, and compares to circumference and area of circle with
double that radius"""

Pi = 3.14159
radius = 0
print("Please enter a number for a radius")
radius = float(input())
radius_doubled = radius * 2
circumference = 2 * Pi * radius
circumference_doubled_radius = 2 * Pi * radius_doubled
print(circumference)
area = radius * radius * Pi
area_doubled_radius = Pi * radius_doubled * radius_doubled
print(area)

area_comparison = area_doubled_radius / area
circumference_comparison = circumference_doubled_radius / circumference
print("If you double the radius, the circumference becomes " + str(circumference_comparison) +
      " times as big, and the area becomes " + str(area_comparison) + " times as big.")
