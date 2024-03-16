import random

# print(random.randrange(1,100))

# print("harun 20 yasinda")

# x=int(2.8)
# print(x)

# x=5.8
# yuvarla=round(x)
# print(yuvarla)


# for x in "muz":
#     print(x)


# a ="merhaba dünya"
# print(len(a))


# txt="hayattaki en iyi şey özgür olmazktır"
# print("özgür" in txt)

# txt="orta raftaki ürnlerden ikincisi bedava"
# print( "pahali" not in txt)

# b="merhaba dünya"
# print(b[2:5])

# a="merhaba dünya"
# print(a[:5])

# c="merhaba dünya"
# print(c[2:])

# d="merhaba dünya"
# print(d[-5:-2])

# a="merhaba trakya"
# print(a.upper())

# b="merhaba trakya"
# print(b.strip())

# c="merhaba, trakya"
# print(c.split(","))

# a="merhaba"
# b="harun"
# c=a+" "+b
# print(c)

# yas=20
# txt="benim yaşim "+str(yas)
# print(txt)

# yas=20
# txt="benim yaşim {}"
# print(txt.format(yas))

# ad="harun"
# soyad="ider"
# print(f"adınız:{ ad} \nsoyadınız:{soyad}")



# def su_hesapla(kilo):
#     k_hesapla=float(kilo*0.03)
#     e_hesapla=float(kilo*0.04)

#     cinsiyet=input("lütfen cinsiyetinizi giriniz erkek/kadin : ").lower()
#     if cinsiyet=="erkek":
#         print("cinsiyetiniz : ",cinsiyet)
#         print("içilmesi gereken su : ",e_hesapla)
#     elif cinsiyet=="kadin":
#         print("cinsiyetiniz : ",cinsiyet)
#         print("içilmesi gereken su : ",k_hesapla)
#     elif not cinsiyet:
#         print("cinsiyet boş bırakılamaz")
#     else:
#         print("hatalı giriş yaptınız")


    
# kilo=int(input("kilonuzu giriniz : "))

# su_hesapla(kilo)


# x=1
# y=2.8
# z=2j  

# print(type(x))
# print(type(y))
# print(type(z))

#fonksiyon tanımlama

# def benim_ilk_fonksiyonum():
#     print("1 tab içeride başlanir")
# benim_ilk_fonksiyonum()


# str1="deneme"
# float1=10.6


# print(round(float1))

# def ekranayaz():
#     print("bu benim ilk fonksiyonum")


# ekranayaz()


# var1=20
# var2=50


#parametreli fonksiyonlar

# def benim_ilk_fonk(a,b):
#     output=(((a+b)*50/100)*a/b)
#     return output

# print(benim_ilk_fonk(20,50))

#defult ve flexible fonks

#defult fonksiyonlar

# def cember_cevresini_hesapla(r,pi=3.14):
#     output= 2*pi*r
#     return output

# print(cember_cevresini_hesapla(2))

# esnek flexible fonksiyonlar

# def hesapla(boy,kilo,*args):
#     print(args)
#     output=boy+kilo + args[0]
#     return output

# print(hesapla(1,2,3))
# print(hesapla(1,2,3,4,5))

# def ortalama_hesapla(sinav1,sinav2):
#     ortalama=(sinav1+sinav2)/2
#     return ortalama

# print("oratalamaniz : ",ortalama_hesapla(65,80))






