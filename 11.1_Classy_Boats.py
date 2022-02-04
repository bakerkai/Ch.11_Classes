'''
CLASSY BOATS
-----------------
Use the following Pseudocode to create this program:

Let's Float the Boat
--------------------
13.) Instantiate an object of the Submarine( ) class. Don't forget to pass in a name.
14.) Call the dock( ) method once
15.) Call the undock( ) method twice
16.) Call the dock( ) method two more times
17.) Call the submerge( ) method once
18.) Call the undock( ) method once
19.) Call the submerge( ) method a final time.

OUTPUT:
USS Hermon is already docked.
USS Hermon is undocking
USS Hermon is already undocked.
USS Hermon is docking
USS Hermon is already docked.
USS Hermon can't submerge!
USS Hermon is undocking
USS Hermon is submerging!

1.) Create a class called Boat( )
2.) Use a constructor that sets two attributes: name and isDocked.
3.) The name should be entered as an argument when the object is created.
4.) The isDocked attribute is a Boolean variable. Set it to True.
5.) Add a method called dock( )
6.) In this method, if the boat is already docked print "(boat name) is already docked."
7.) If it is not docked, print "(boat name) is docking" and set the isDocked attribute to True.
8.) Add another method called undock( )
9.) In this method, if the boat is already undocked print "(boat name) is already undocked."
10.) If it is docked print "(boat name) is undocking" and set the isDocked attribute to False.
11.) Add another class called Submarine( ) that will inherit the Boat( ) class.
12.) In the Submarine( ) class create a method called submerge( ) that will print "(boat name) is submerging"
if the boat is undocked and "(boat name) can't submerge" if the boat is docked.
'''
class Boat():
    def __init__(self, name):
        self.name = name
        self.isDocked = True
    def dock(self):
        if self.isDocked == True:
            print(self.name, "Is docked.")
        else:
            print(self.name, "Is not docked, and is now docking.")
            self.isDocked = True
    def undock(self):
        if self.isDocked == False:
            print(self.name, "Is already undocked")
        else:
            print(self.name, "Is undocking.")
            self.isDocked = False
class Submarine(Boat):
    def submerge(self):
        if self.isDocked == True:
            print(self.name, "Can not submerge due to it being docked.")
        else:
            self.isDocked = False
            print(self.name, "Is submerging")




def myprogram():
    bote = Submarine("USS Hermon")
    bote.dock()



if __name__ == "__main__":
    myprogram()