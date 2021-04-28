#spaceship name generator
import wordlists as wl
import random
def go(prefix = ""):
    randnoun = wl.rand_noun().capitalize()
    randadj = wl.rand_adj().capitalize()
    kwargs = {'pre':prefix, 'noun':randnoun, 'adj':randadj}
    if prefix:
        string = "{pre} {adj} {noun}"
    else:
        string = "{adj} {noun}"
    return string.format(**kwargs)

def gen_num(num = 30, prefix = ''):
    lt = ""
    for i in range(num):
        lt += go(prefix) + "\n"
    return lt

#go()
if __name__ == "__main__":
    print(gen_num())
