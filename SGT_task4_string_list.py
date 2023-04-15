# 1)Ask the user to enter the text and a letter. Count how many occurrences of the letter provided. 

text=input('Enter the word: \n')
letter=input('Enter the letter: \n')
print(f'Selected letter count: {text.count(letter)}')

# 1.1) Based on the task 1, count the occurrences of each character in the text provided and display them in the output
letters=[]
letters_count= []
for i in range(0,len(text)):
    letterExist=False
    for l in range(0,len(letters)):
        if letters[l] == text[i]:
            letters_count[l]+=1
            letterExist=True
            break
    if not letterExist:
            letters.append(text[i])
            letters_count.append(1)

for ltt in range(0,len(letters)): 
    print(letters[ltt] +" counted " +str(letters_count[ltt]))


#2)Write the program to sort the list (without using sort function). You can implement any algorithm

list= [30,5,32,6,77,88,1]

for i in range(len(list)):
    for j in range(0,len(list)-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print(list)