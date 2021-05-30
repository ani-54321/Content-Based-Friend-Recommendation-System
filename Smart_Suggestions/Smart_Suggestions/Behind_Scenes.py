from . import list_in_list as ls
from itertools import chain

class Graph:
    name = "Someone"
    specializations = "Not Provided"
    hobbies = "Not Provided"
    year = "Not Provided"
    next = []
    Users = []

    def __init__(self, data, friend=None):
        self.name = data[2]
        self.email = data[0]
        self.password = data[1]
        self.specializations = data[3]
        self.hobbies = data[4]
        self.region = data[5]
        self.year = data[5]
        if friend!=None:
            self.next.append(friend)
            friend.next.append(self)

    # def data_storing()

    def connections(self):
        for i in range(len(self.next)):
            if self.next[i] == None:
                pass
                # print(self.__dict__, len(self.next))
            else:
                pass
                # print(self.next[i].__dict__)

    @classmethod
    def new_user(cls, new):
        cls.Users.append(new)


class Name:
    def __init__(self, name, next_name=None):
        self.name = name
        self.next = next_name


class Year:
    def __init__(self, yr):
        self.year = yr
        self.left = None
        self.right = None


class Tree:
    Sectors = {"specializations":[], "hobbies":[], "years":Year(2000), "names":[]}
    # specs=[]
    # hobs=[]
    # yrs=[]
    # names=[]

    @classmethod
    def __init__(cls, name, specializations, hobbies, year, friend=None):
        # print(cls, name, specializations, hobbies, year, friend)
        # print(cls.sectors)
        if specializations!=None:
            for elem in ls.different_values(specializations, cls.Sectors["specializations"]):
                cls.Sectors["specializations"].append(elem)
        
        if hobbies!=None:
            for elem in ls.different_values(hobbies, cls.Sectors["hobbies"]):
                cls.Sectors["hobbies"].append(elem)

        if year!=None:
            ret_yr = Year(year)
            cls.level_order(ret_yr, cls.Sectors["years"])
            # else:
            #     cls.Sectors["years"][[i.year for i in cls.Sectors["years"]].index(year)].next = ret_yr

        if name!=None:
            ret_name = Name(name)
            if name not in [i.name for i in cls.Sectors["names"]]:
                cls.Sectors["names"].append(ret_name)
            else:
                cls.Sectors["names"][[i.name for i in cls.Sectors["names"]].index(name)].next = ret_name

    @classmethod
    def level_order(cls, yr, cur):
        while True:
            if cur == None:
                cur = yr
                break
            if yr.year < cur.year:
                cur = cur.left
                cls.Sectors["years"].left = cur
            elif yr.year > cur.year:
                cur = cur.right
                cls.Sectors["years"].right = cur
        
        # print(cur.year)
        # cls.Sectors["years"] = cur
        # print(cur.left)
        


# name = input("Enter your name : ")
# specializations = input("Enter Specializations separated by commas : ").split(',')
# hobbies = input("Enter Hobbies separated by commas : ").split(',')
# year = int(input("Enter your birth year : "))

# owner = Tree("Owner", None, None, None)
new = Graph(["owner@gmail.com", "owNer", "Owner", "name", "name", 2003])
Graph.new_user(new)

# person1 = Graph(name, specializations, hobbies, year)
# p1 = Tree(name, specializations, hobbies, year)
# Graph.new_user(person1)

# person2 = Graph("Shaha", specializations, hobbies, year, person1)
# p2 = Tree("Shaha", specializations, hobbies, 1999)
# p3 = Tree("Shaha", specializations, hobbies, 200)
# p4 = Tree("Shaha", specializations, hobbies, 20000)
# Graph.new_user(person2)
# person2.connections()
# person1.connections()
# print(Graph.Users)

# print(Tree.Sectors["years"].left)

# print(Tree.Sectors["names"][1].next.name)

# Better solution
# Cost effective
# New feature addition
# Use of latest technologies
# Hardware simulation

# Tools
# Block diagram
# Discription (Aims)
# Activity plan (tabular) - Task to be Completed