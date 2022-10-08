class black_n_white_tv:
    def color(self):
        print("Black and White")

    def video(self):
        print("480p")

    def shape(self):
        print("square")

class colored_tv(black_n_white_tv):
    def screen(self):
        print("LED")

    def color(self):
        print("Colored")

    def video(self):
        print("720p")

obj = colored_tv()
obj.screen()
obj.shape()
obj.color()
obj.video()

# rules of overriding
# 1. create same name method as that of your parent class
# 2. same no. of parameter
    


