import re

def parse_command(text):

    text = text.lower()

    print("Checking:", text)

    if "cube" in text:
        print("Cube matched")
        number = re.search(r"\d+", text)
        if number:
            return {
                "shape":"cube",
                "size":int(number.group())
            }

    if "cylinder" in text:
        print("Cylinder matched")
        nums = re.findall(r"\d+", text)
        print(nums)
        if len(nums) >= 2:
            return {
                "shape":"cylinder",
                "radius":int(nums[0]),
                "height":int(nums[1])
            }

    if "sphere" in text:
        print("Sphere matched")
        number = re.search(r"\d+", text)
        if number:
            return {
                "shape":"sphere",
                "radius":int(number.group())
            }

    if "box" in text:
        print("Box matched")
        nums = re.findall(r"\d+", text)
        print(nums)
        if len(nums) >= 3:
            return {
                "shape":"box",
                "length":int(nums[0]),
                "width":int(nums[1]),
                "height":int(nums[2])
            }

    if "hole" in text:
        print("Hole matched")
        number = re.search(r"\d+", text)
        if number:
            return {
                "operation":"hole",
                "diameter":int(number.group())
            }

    if "fillet" in text:
        print("Fillet matched")
        number = re.search(r"\d+", text)
        if number:
            return {
                "operation":"fillet",
                "radius":int(number.group())
            }

    if "chamfer" in text:
        print("Chamfer matched")
        number = re.search(r"\d+", text)
        if number:
            return {
                "operation":"chamfer",
                "distance":int(number.group())
            }

    if "extrude" in text:
        print("Extrude matched")
        number = re.search(r"\d+", text)
        if number:
            return {
                "operation":"extrude",
                "distance":int(number.group())
            }

    print("No match")
    return None