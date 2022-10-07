class a:
    def apple(self):
        print("apple")
class b(a):
    def ball(self):
        print("ball")
class c(a):
    def cat(self):
        print("cat")
class d(b):
    def dog(self):
        print("dog")
class e(c):
    def elephant(self):
        print("elephant")
class f(c):
    def frog(self):
        print("frog")
class g(e,f):
    def grape(self):
        print("grape")

g_obj=g()
g_obj.apple()
g_obj.cat()
g_obj.elephant()
g_obj.frog()
g_obj.grape()

d_obj=d()
d_obj.ball()
d_obj.dog()
