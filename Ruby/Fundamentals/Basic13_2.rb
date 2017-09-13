
# Print 1-255
(1..255).each { |i| puts i }

# Print odd numbers between 1-255
(1..255).each { |i| puts i if i.odd? }

# Print Sum
sum = 0
(0..255).each { |i| puts "New Number: #{i} Sum: #{sum += i}"}

# Iterating through an array
[1,3,5,7,9,13].each { |elem| puts elem }

# Find Max
puts [-3,-5,-7].max

# Get Average
arr = [2,10,3]
puts arr.reduce(:+) / arr.length.to_f

# Array with Odd Numbers

y = []
(1..255).each { |i| y << i if i.odd? }

# Greater Than Y
arr = [1, 3, 5, 7]
y = 3
puts arr.count { |elem| elem > y }

# Square the values
arr = [1, 5, 10, -2]
puts arr.map! { |elem| elem * elem }


# Eliminate Negative Numbers
arr = [1, 5, 10, -2]
puts arr.each_index { |index| arr[index] = 0 if arr[index] < 0 }

# Max, Min, and Average
arr = [1, 5, 10, -2]
{ max: arr.max, min: arr.min, average: arr.reduce(:+) / arr.length.to_f }

# Shifting the Values in the Array
arr = [1, 5, 10, 7, -2]
arr.rotate!(1)[arr.length-1] = 0

# Number to String

arr = [-1, -3, 2]
puts arr.each_index { |index| arr[index] = "Dojo" if arr[index] < 0 }
