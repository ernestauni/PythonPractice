# Task 1: Write a function that takes two parameters (a and b) and returns their sum.

def sum_numbers(a,b):
    result_sum=a+b
    print(result_sum)

sum_numbers(5,5)

# Task 2:Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string. Hint: you can use given_character in "aeiou"

def count_vowels(string):
    vowels='aeiouAEIOU'
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count

print(count_vowels('Apple'))

# Task 3:Write a function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise

def palindrome(word):
   backward=''
   for char in word:
       backward=char+backward
   word=word.lower()
   backward=backward.lower()
   if backward==word:
       return True
   else:
       return False

print(palindrome('Ada'))

# Task 4:Write a function that takes a list of integers as a parameter and returns a list of only the even integers in the original list

def integers(numbers:list):
    intg_list=[]
    for num in numbers:
        if num%2==0:
            intg_list.append(num)
    return intg_list

print(integers([1,2,3,4,6,8,9]))

# Task 5:Write a function that takes a list of integers and a target sum as parameters and returns a list of two integers from the original list that add up to the target sum.

def target_sum(numbers:list, target:int):
    seen=set()
    for num in numbers:
        diff=target-num
        if diff in seen:
            return [diff,num]
        seen.add(num)

numbers = [2, 7, 11, 15]
target = 9
print(target_sum(numbers, target))  # [0, 1]

# Task 6: Write a function that takes a list of integers as a parameter and returns the product of all the integers in the list.

def product_of_numbers(numbers:list):
    result=1
    for num in numbers:
        result*=num
    return result

print(product_of_numbers([2,2,3]))

# Task 8:Write a function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary that have an even value.

def even_keys(dictionary:dict):
    keys_list=[]
    for key, value in dictionary.items():
        if value%2==0:
            keys_list.append(key)
    return keys_list

print(even_keys({'1':1,'2':2,'3':3,'4':4}))

# Task 9:Write a function that takes a list of dictionaries as a parameter and returns a new dictionary that contains the sum of the values for each key in the original dictionaries.

def sum_of_dict_values(dictionaries):
    summed_dict={}
    for item in dictionaries:
        for key, value in item.items():
            if key not in summed_dict:
                summed_dict[key]=value
            else:
                summed_dict[key]+=value
    return summed_dict

print(sum_of_dict_values([{1:1,2:2,3:3},{1:3,2:1,3:2},{1:1,2:3,3:2}]))

# Task 10:Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped.

def swap_items(tuple_input:tuple):
    convert_list=list(tuple_input)
    last_item=convert_list[-1]
    convert_list[-1]=convert_list[0]
    convert_list[0]=last_item
    return tuple(convert_list)

tuple_test=(1,2,3,4,5)
print(swap_items(tuple_test))

# Task 11:Write a function that takes a set as a parameter and returns a new set that contains only the elements that are not divisible by 3.

def not_divisible_3(set_input:set):
    result_set=set()
    for i in set_input:
        if i%3!=0:
            result_set.add(i)
    return result_set

set_test=(1,2,3,4,5,6,7,8,9)
print(not_divisible_3(set_test))