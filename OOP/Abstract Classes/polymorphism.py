from abc import ABC, abstractclassmethod


class A(ABC):
    @abstractclassmethod
    def speak(self, msg):
        ...


class B(A):
    def speak(self, msg):
        print(f'B is talking {msg}')


class C(A):
    def speak(self, msg):
        print(f'C is talking {msg}')


b = B()
c = C()

b.speak("A Subject")
c.speak("A Other Subject")
