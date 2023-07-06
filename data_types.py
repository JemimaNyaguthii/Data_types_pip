
# Write a Python program to get a single string
# from two given strings, separated by a space, 
# and swap the first two characters of each string\
def chars_separate(word1,word2):
    new_word1=word2[:2] + word1[2:]
    new_word2=word1[:2] + word2[2:]
    result = new_word1 + ' '+ new_word2
    return result  
print(chars_separate("jem","mima"))
# 2.Write a Python function that takes a list of 
# words and returns the longest word and the length of the longest one
# def longest_word(words):
# def longest_word(name):
#     word=max(words,key=len)
#     return word

# print(longest_word(["cat","apple","eating"]))    

# 3.Write a Python program that accepts a comma-separated
#  sequence of words as input and prints the distinct words 
#  in sorted form (alphanumerically).



# 4 Write a Python function that takes two lists and returns
#  True if they have at least one common member.
def common_member(list1,list2):  
    output='false'
    for a in list1:
        for b in list2:
            if a==b:
                output ='True'
                return output
print(common_member([21,22,23,1,24],[21,1,3,31,33]))            

# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
list_color=["black","red","maroon","yellow"]
list_codes=["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'list_color':c,'list_codes':f} for c,f in zip(list_color,list_codes)])
# 6. Write a Python program to check whether all dictionaries in a list are empty or not
# dict_check=[{},{},{name:Jem}]
# empty=True
# for i in name:
#     if empty==false:

#         print(all empty)

# 7. Given a list of numbers, use list comprehension 
#  remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
numbers=[3,5,45,97,32,22,10,19,39,43]
remove_odd=[n for n in numbers if n%2!=0]
print(remove_odd) 

# 8. Find the common numbers in two lists (without using a tuple or set) 
list_a = [1,2,3,4]
list_b= [2,3,4,5]
common  = [a for a in list_a if a in list_b]
print(common)

# 9. Use a nested list comprehension to find all of the 
# numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
divisible_numbers=[r for r in range (1,1000) for d in range(2,9) if r%d==0]
print(divisible_numbers)
# 10. Write a Python function to remove all vowels in a string

def remove_vowels():
    empty=[]
    vowels=["a","e""i""o""u"]
    for i in range (len(word)):
        if word[i] is not vowels:
            words=empty +word[i]

