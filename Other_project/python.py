class Vector:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def incX (v):
    v.x += 1

v1 = Vector(1, 2, 3)

print(f"Become: the value x of vector v1 is {v1.x}")

incX(v1)

print(f"After: now, the value x of vector v1 is {v1.x}")