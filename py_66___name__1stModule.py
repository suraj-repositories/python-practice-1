# *******************************
# if __name__ == '__main__'
# *******************************

# y tho?
# 1) Module can be reun as a standalone program 
# 2) Module can be improved and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will executes the code found within '__main__' if it's
# the initial module being run

# import py_66___name__2ndModule as Module2

# print(__name__)
# print(Module2.__name__)


#--------------------------------------------------------------------------

print(__name__)

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")

#--------------------------------------------------------------------------