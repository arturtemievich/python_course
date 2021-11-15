"""Unit Testing

Unit testing is a software testing method by which individual units of source code
are put under various tests to determine whether they are fit for use.
It determines and ascertains the quality of your code.

The unit test framework in Python is called unittest, which comes packaged with Python.

A unit could be bucketed into various categories:
> An entire module;
> An individual function;
> A complete interface like a class or a method.

Python's unit testing framework was inspired by java's 'JUnit'
and has similar features as major unit testing frameworks in other languages.
"""


def cuboid_volume(l):
    return l * l * l


# length = [2, 1.1, -2.5, 2j, 'two']
#
# for i in range(len(length)):
#     print(f"The volume of cuboid: {cuboid_volume(length[i])}")


"""
There are three things which are certainly incorrect in the above code:
> First, the volume of cuboid being negative;
> Second, the volume of the cuboid is a complex number;
> Finally, the code resulting in a TypeError since you cannot multiply a string, which is a non-int.

The third problem thankfully resulted in an error 
while the first & second still succeeded even though the volume of the cuboid cannot be negative and a complex number.

Unit tests are usually written as a separate code in a different file, 
and there could be different naming conventions that you could follow.
"""


def cuboid_volume_2(l):
    if type(l) not in (int, float):
        raise TypeError("The length of cuboid can only be int or float!")
    return l * l * l
