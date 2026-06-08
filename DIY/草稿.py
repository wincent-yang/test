class Person:
    def __init__(self, name, *hobbies, **info):
        self.name = name
        self.hobbies = hobbies   # 元组
        self.info = info         # 字典



# 3. 传 name + 位置参数 + 关键字参数（给 **info）
p3 = Person("王五", "游戏", "阅读", age=20, city="西安", gender="男")
print(p3.name)
print(p3.hobbies)
print(p3.info)

for k, v in p3.info.values():
    print(f"{k}: {v}")