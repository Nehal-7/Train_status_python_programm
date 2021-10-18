class Sample:
    a = "Nehal"

obj = Sample()
obj.a = "Faizan"  # Doesn't change class attribute
# Sample.a = "Ayaz"  # Change class attribute

print(Sample.a)
print(obj.a)