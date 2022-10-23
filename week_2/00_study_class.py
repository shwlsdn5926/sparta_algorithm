class Person:
    def __init__(self, param_name):
        # print("i am object", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요. 제 이름은", self.name, "입니다.")
# Person() : 생성자 - 객체 생성 함수
# 생성자를 만들기 위해서는 __init__()이라는 함수를 정의해야 한다.
person1 = Person("노진우")
print(person1.name)
person1.talk()
person2 = Person("노현우")
print(person2.name)
person2.talk()
