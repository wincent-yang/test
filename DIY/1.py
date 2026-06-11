#help(print)

class Animal:
    def eat(self, food: str) -> None:
        print(f"进食：{food}")

a = Animal()
a.eat("米饭")   # 正常
a.eat(100)   # 报错/IDE警告：类型不匹配

# 1. 先定义食物类
class Food:
    def __init__(self, name: str):
        self.name = name

# 2. 动物类，限定参数必须是 Food 实例
class Animal:
    def eat(self, food: Food) -> None:
        print(f"正在吃 {food.name}")

# 使用
rice = Food("米饭")
cat = Animal()
cat.eat(rice)  # 正常

cat.eat("米饭")  # 报错：不是 Food 对象


