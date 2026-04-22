# Create a function find_axis(v1, v2) which returns the unit vector v3, where v3 is perpendicular to the vectors v1 and v2.
# If the vectors v1 and v2 are parallel (or zero) then the function should raise an exception (ValueError)
# [Hint: v1 and v2 are parallel if the cross product v1 × v2 is zero]. Vectors are instances of the Vector class from Homework 6. 


def find_axis(v1, v2):
    v3 = v1.cross(v2)

    if v3 == Vector(0, 0, 0):
        raise ValueError("Vectors are parallel or zero")

    length = v3.length()
    return Vector(v3.x / length, v3.y / length, v3.z / length)
