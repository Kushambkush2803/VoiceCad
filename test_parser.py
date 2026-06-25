from parser import parse_command

tests = [

    "Create a cube 50 mm",

    "Create a cylinder radius 20 height 60",

    "Create a sphere radius 25",

    "Create a box 20 by 30 by 40",

    "Add a hole 10 mm",

    "Fillet edges 2 mm",

    "Chamfer edges 3 mm",

    "Extrude by 20 mm"

]

for test in tests:

    print("-------------------")
    print(test)
    print(parse_command(test))