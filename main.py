import re

pattern = '^The.*Spain$'
txt = "The rain in Spain"
result = re.findall(pattern, txt)
print(result)
# Find all lower case characters alphabetically between "a" and "m":
txt1 = 'The rain in Spain'
pattern1 = '[a-m]'
result1 = re.findall(pattern1, txt1)
print(result1)
# Find all digit characters:
pattern2 = '[0-9]'
txt2 = "That will be 59 dollars"
result2 = re.findall(pattern2, txt2)
print(f"all digit characters {result2}")
#  Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
txt3 = "hello world"
pattern3 = 'he..o'
result3 = re.findall(pattern3, txt3)
print(f"Hello character {result3}")
# Check if the string starts with 'hello':
pattern4 = '^hello'
txt4 = "hello world"
result4 = re.findall(pattern4, txt4)
print(f"began with {result4}")
# Check if the string ends with 'world':
pattern5 = 'world$'
txt5 = "hello world"
result5 = re.findall(pattern5, txt5)
print(f"ends with  {result5}")
# Check if the string contains "ai" followed by 0 or more "x" characters:
pattern6 = 'world$'
txt6 = "hello world"
result6 = re.findall(pattern6, txt6)
print(f"ends with  {result6}")
# Check if the string contains "ai" followed by 0 or more "x" characters:
txt7 = "The rain in Spain falls mainly in the plain!"
pattern7 = 'aix*'
result7 = re.findall(pattern7, txt7)
print(f"contains ai {result7}")
# Check if the string contains "ai" followed by 1 or more "x" characters:
txt8 = "The rain in Spain falls mainly in the plain!"
pattern8 = 'aix+'
result8 = re.findall(pattern8, txt)
print(f"ends with  {result8}")
# Check if the string contains "a" followed by exactly two "l" characters:
pattern9 = 'al{2}'
txt9 = "The rain in Spain falls mainly in the plain!"
result9 = re.findall(pattern9,txt9)
print(f"contains {result9}")

# Check if the string contains either "falls" or "stays":
pattern10 = 'al{2}'
txt10 = "The rain in Spain falls mainly in the plain!"
result10= re.findall(pattern10,txt10)
print(f"contains {result10}")