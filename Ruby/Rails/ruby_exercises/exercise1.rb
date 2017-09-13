x=5;y=10;z=x+y   #can be on one line if using the semicolons
puts z
first_name = "Philemon"
last_name= "Mastewal"
puts"your name is"+" "+first_name +" "+ last_name
#to insert it can be written like this below
puts"First name is #{first_name} and last name is #{last_name}"
# or (%s for string and %d for decimal %f for float)
puts"First name is %s and last name is %s" % [first_name,last_name]

z = 50
puts "value of z is #{z}"

puts "\t\tI am\n 5'10\" tall"
#\t for tabs
#\n for new line
#\ for something else that you want to ignore in this case the quotation marks at the end of the height 
