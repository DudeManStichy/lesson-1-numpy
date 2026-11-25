#-import numpy

import numpy as np

#set datatype and details

data_type = [('name', 'S15'),('class', int),('height', float)]
students_details = [('James', 5, 48.5), ('Neil', 6, 52.5),('Paul', 5, 42.10),('Pit', 5, 40.11)]

#create a structured array

students = np.array(students_details, dtype=data_type)
print("Original array:")
print()
print(students)
print()
print("Sort by height")
print()
print(np.sort(students, order='height'))