player=["affridi","Imran","baber","shoaib","Hitesh"]
plays=["Cricket","hockey","badminton","football","politics"]
age=[20,25,28,26,29]

zip_data=list(zip(player,plays,age))
print(zip_data)

player=["affridi","Imran","baber","shoaib","Hitesh"]
plays=["Cricket","hockey","badminton","football","politics"]
age=[20,25,28,26,29]

zip_data = dict(zip(player, zip(plays, age)))
print(zip_data)

player=["affridi","Imran","baber","shoaib","Hitesh"]
plays=["Cricket","hockey","badminton","football","politics"]
age=[20,25,28,26,29]

zip_data=tuple(zip(player,plays,age))
print(zip_data)

#unzip