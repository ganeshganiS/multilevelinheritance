class GrandFather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
class Father(GrandFather):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        GrandFather.__init__(self,grandfathername)
class Myname(Father):
    def __init__(self,myname,fathername,grandfathername):
        self.myname=myname
        Father.__init__(self,fathername,grandfathername)
    def print_name(self):
        print("GrandFather name=",self.grandfathername)
        print("Father name=",self.fathername)
        print("My name=",self.myname)
S=Myname("Ganesh","Gangadhar","Sreeramulu")
S.print_name()

        
        
