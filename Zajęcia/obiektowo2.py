# #class nazwa_klasy(klasa_nadrzedna)
#
# class Zwierze():
#     def __init__(self):
#         self.oczy=2
#         self.wlosy=True
#
#     def __str__(self):
#         return  f'oczy: {self.oczy}, wlosy: {self.wlosy}'
#
# class Kot(Zwierze):
#     def dajglos(self):
#         print('miau')
#
# class Czlowiek(Zwierze):
#     def dajglos(self):
#         print('heeeee')
#
# class Dresiarz(Czlowiek):
#     def __init__(self):
#         super().__init__()
#         self.wlosy=False
#     def dajglos(self):
#         super().dajglos() #super to odwolanie do klasy nadrzednej czyli do czlwoieka
#         print('chodacy problem')
#
# class Student(Czlowiek):
#     def dajglos(self):
#         print('siema, jestem student')
#
# class Pies(Zwierze):
#     def dajglos(self):
#         print('hauhau')
#
# class Bokser(Pies):
#     pass
#
# class Jamnik(Pies):
#     pass
#
# # zwierze=Zwierze()
# # czlowiek=Czlowiek()
# # czlowiek.dajglos()
# #
# # pies=Pies()
# # pies.dajglos()
# #
# # kot=Kot()
# # kot.dajglos()
# # jamnik=Jamnik()
# # jamnik.dajglos() #z psa
# # print(jamnik.oczy) #ze zwierzecia
#
# dresiarz=Dresiarz()
# dresiarz.dajglos()
# print('nie mam glosy')
# print(dresiarz)


class A():
    def hi(self):
        print('a')

class B(A):
    # def hi(self):
#     #     print('a')
class C(A):
    pass
class D(B,C):
    pass
