from tools import *


f=form()
iv =StringVar()

radio(f,"male",1,iv).pack()
radio(f,"female",2,iv).pack()

def test():
    print(iv.get())
button(f,"ok",test).pack()

f.mainloop()
