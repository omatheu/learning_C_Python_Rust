squares1 = (x**2 for x in range(10)) #It's a generating expression!

squares1_list = list(squares1) #It's a way for interate in generating expression!

squares2 = [x**2 for x in range(10)] #It's a list compreension

print(f"This is the result of the first operation with generating expressions {squares1_list}\n")

print(f"This is the second result of the operation with generating expressions {squares2}")
