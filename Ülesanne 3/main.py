# while(n):
# n = n -1
# print(n)

#--------Näide 1

#for i in range(1,10,5):
    #print(i)
#else:
    #print("lõõp")
#----- Näide 2
#text = "When you staRt looking for InspIration, soMetimes It's harD to finD thE rIght solution. BuT wiTh eFFort and deTerminaTion, anSWers caN be foUnd eveRywHere."

#letter = "a"
#print(letter.islower())

#lenText = len(text)
#for i in range(lenText):
    #print(i)

#for i in text:
    #print(i)

#---- Näide 3

#myStr = "Hello its Tom"
#myTextLen = len(myStr)
#middleSymbol = myTextLen/2
#print(middleSymbol)
#print(myTextLen)
#print(myStr[6])


# [start:end:step]
#print(myStr[0:len(myStr)])

#print(myStr[-1::-1])



#def isPalidrome(s):
    #return s == s[::-1]

#s = "shalash"
#ans = isPalidrome(s)

#if ans:
    #print("yes")
#else:
     #print("no")



#myStr = input("sisesta sõna").lower()
#if myStr == myStr[::-1]:
    #print("see on poleidrome")
#else:
    #print("see ei ole poleidrome")
    

#count_a = myStr.count('a')
#print(f"Kirjade arv 'a': {count_a}")

#vowels ="a"
#vowel_count = 0
#for char in myStr:
    #if char == vowels:
        #vowel_count = vowel_count + 1
#print(f"letters a:", vowel_count)


#sona = "Hello Tom"
# string.replace(oldvalue, newvalue, count)
#sona = sona.replace("Tom","***")
#print(sona)



#sona = "Hello GAY"
# string.replace(oldvalue, newvalue, count)
#sona = sona.replace("Hello","***").replace("GAY","***")
#print(sona)

text ="chip i deil - eto personazhy, chip i deil vsegda pomogaut"
modified_text = text.replace("chip","***").replace("deil","***")
print(modified_text)


text ="chip i deil - eto personazhy, chip i deil vsegda pomogaut"
for i in range (0,len(text),5):
    variable = i+5
    print(text[i:variable])














