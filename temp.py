# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """
# # class user():
# #     def __init__(self,ism,foydalanuvchi_ismi,email,yoshi):
# #         self.name = ism
# #         self.username = foydalanuvchi_ismi
# #         self.mail = email
# #         self.age = yoshi
# #     def get_info(self):
# #         return f"foydalanuvchi nomi: {self.username} , ismi: {self.name} , email:{self.mail} , yoshi {self.age}"
# # talaba1=user("Ravshan","ravshan123","ravshan@mail.ru",21)
# # talaba2=user("Rustam","rusik123","rustambek@mail.ru",31)
# # talaba3=user("Rayxon","rayxon123a3","rayxona@mail.ru",24)
# # talaba4=user("Ramazon","ramizt123","ramazan@mail.ru",19)
# # print(talaba1.get_info(),"\n",talaba2.get_info(),'\n',talaba3.get_info(),'\n',talaba4.get_info())

# ##
# class avto():
#     def __init__(self,model,rang,karopka,narh):
#         self.model = model
#         self.color = rang
#         self.gearbox = karopka
#         self.cost = narh
#         self.distance = 0
#     def get_model(self):
#         return self.model
#     def get_color(self):
#         return self.color
#     def get_gearbox(self):
#         return self.gearbox
#     def get_cost(self):
#         return self.cost
#     def get_distance(self):
#         return self.distance
#     def set_model(self,model):
#         self.model=model
#     def set_color(self,color):
#         self.color=color
#     def set_gearbox(self,gearbox):
#         self.gearbox=gearbox
#     def set_cost(self,cost):
#         self.cost=cost
#     def set_ditance(self,distance):
#         self.distance=distance
#     def set_add_distance1km(self):
#         self.distance+=1
#     def get_info(self):
#         return f"Avtomobil modeli: {self.model} , rangi: {self.color} , karopka: {self.gearbox} , narxi: {self.gearbox} bosib otgan masofasi: {self.distance}"
# avto1=avto('nexia','qora','avtomat',10000)
# class avtosalon():
#     def __init__(self,nomi,manzili):
#         self.name=nomi
#         self.address=manzili
#         self.on_sale=[]
#         self.amount=0
#     def add_new_auto(self,avto):
#         self.amount+=1
#         self.on_sale.append(avto)
#     def get_info_salon_auto(self):
#         return [auto.get_info() for auto in self.on_sale]
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
class fan:
    def __init__(self,nomi):
        self.names = nomi
        self.soni = 0
        self.ruyxati=[]
    def add_some(self,ism):
        self.soni +=1
        self.ruyxati.append(ism)
    def remove_some(self,ism):
        self.soni -=1
        self.ruyxati.remove(ism)
fan1 = fan('matem')
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar=[]
        self.profilar = []
        self.profilar_soni = 0
    def fanga_yozil(self,FANNOMI):
        self.fanlar.append(FANNOMI)
        FANNOMI.add_some(self)
    def remove_fan(self,fannomi):
        if fannomi in self.fanlar:
            fannomi.remove_some(self)
            self.fanlar.remove(fannomi)
        else:
            print('bunday fan mavjud emas')
    def add_profi(self,Profi_ob):
        self.profilar.append(Profi_ob)
        self.profilar_soni+=1
    def remove_profi(self,Profi_ob):
        if Profi_ob in self.profilar:
            Profi_ob.remove_talaba(self)
            self.profilar.remove(Profi_ob)
            self.profilar_soni-=1
    def banned(self,Profi_ob):
        if Profi_ob in self.profilar:
            self.profilar[self.profilar.index(Profi_ob)]= f"you are banned form {Profi_ob}"
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,userID):
        super().__init__(ism,familiya,passport,tyil)
        self.userID = userID
    def get_FIO(self):
        return f"{self.ism} {self.familiya}"
    def get_userID(self):
        return self.userID
    def get_age(self,yil):
        return yil-self.tyil
    def get_passport(self):
        return self.passport
    def set_userID(self,userID):
        self.userID = userID
class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam ):
        super().__init__(ism, familiya, passport, tyil)
        self.profiID = idraqam
        self.talabalari = []
        self.talabalari_soni=0
    def get_FIO(self):
        return f"{self.ism} {self.familiya}"
    def get_userID(self):
        return self.profiID
    def get_age(self,yil):
        return yil-self.tyil
    def get_passport(self):
        return self.passport
    def add_talabalar(self,talaba_ob):
        self.talabalari.append(talaba_ob)
        self.talabalari_soni+=1
        talaba_ob.add_profi(self)
    def ban_user(self,talaba_nomi):
        while talaba_nomi in self.talabalari:
            self.talabalari[self.talabalari.index(talaba_nomi)]=" Banned "
            talaba_nomi.banned(self)
    def remove_talaba(self,talaba_ob):
        if talaba_ob in self.talabalari:
            self.talabalari.remove(talaba_ob)
            self.talabalari_soni-=1
            talaba_ob.remove_profi(self)