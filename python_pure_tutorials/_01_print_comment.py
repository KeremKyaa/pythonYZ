#bu proje yapay zeka için
"""
multiple comment
"""


print("python öğreniyorum")

#float
print(14.5)

# SEPERATE
print("merhabalar","güzel","insanlar",sep=" * ")
#END
print("Merhabalar","Python","Öğreniyorum"," *** ","Dünyasına Hoşgeldiniz")

print("Merhabalar","Python","Öğreniyorum",end=" *** ")
print("Dünyasına Hoşgeldiniz")

#DOCSTRING

print("""Merhabalar Python Öğreniyorum
*** dünyasına hoşgeldiniz""")

# ESCAPE /\
print("""Merhabalar Python Öğreniyorum *** \n\tdünyasına hoşgeldiniz""")

#Değişken İsimlendirmelerde
name = "Hamit"
surname = "Mızrak"

#print("Adım: " , name," \nSoyisim: ",surname)
# 1.YOL
print("Adım: " , name,"Soyisim: ",surname)
# 2. yol
print("Adım: %s Soyisim: %s:"%(name,surname))
# 3.YOL
print(f"Adım: {name}, Soyisim: {surname}")