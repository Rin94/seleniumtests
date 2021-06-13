class fruit:

    color="blue"
    def setColor(self,color):
        self.color=color

    def getColor(self):
        return self.color
    def sayhi(self):
        print("Hi")


orange=fruit()
orange.sayhi()
#you can make the attribute on the fly
print("My color after: ",orange.getColor())
orange.setColor("orange")
print("My color is: ",orange.getColor())
orange.shape="round"
del orange.color
print("Orange color after delete: ",orange.color)
print(orange.shape)
print(dir(orange))