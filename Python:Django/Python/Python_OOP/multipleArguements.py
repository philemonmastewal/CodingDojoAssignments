def varargs(arg1, *args):
  print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"

In this example, the first argument is assigned to the first method parameter as usual. However, the next parameter is prefixed with an asterisk(the "splat" operator we just introduced), which bundles the remaining arguments into a new tuple, which is then assigned to that parameter.

If we tested the type of args inside our function using type(args) we would get:
def varargs(arg1, *args):
   print "args is of " + str(type(args))
 varargs("one", "two", "three") # output: args is of <type 'tuple'>

Note the .join() method is called on a string that glues the values in the tuple together. For example, the tuple of arguments ('two', 'three') was joined as 'two, three' when we called ', '.join(rest) .
