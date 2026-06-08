class animal(object):
    def eat(self, food):
        
        print(f"正在吃{food}")

pig: animal = animal()
pig.eat("谷子")

animal.eat(pig,"谷子")