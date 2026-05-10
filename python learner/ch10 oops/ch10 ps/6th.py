# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class demo:
    def demo(harry):
        print("Hy")

o = demo()
o.demo()

#It runs succesfully, but this is not a good practice becuase it makes programm readability less.