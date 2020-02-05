# Create a function named divisible_by_ten() that takes a list of numbers named
# nums as a parameter. Return the count of how many numbers in the list are 
# divisible by 10
def divisible_by_ten(nums):
  result = []
  for num in nums:
    if num % 10 == 0:
      result.append(num)
  return len(result)

# Create a function named add_greetings() which takes a list of strings named 
# names as a parameter. Add the string "Hello, " in front of each name in names
# and append the greeting to the new list. Return the new list containing the 
# greetings.
def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append('Hello, ' + name)
    return new_list

# Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of 
# the list is not even. The function should then return lst. For example if lst
# started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should 
# return [11, 12, 15].
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

# Create a function named odd_indices() that has one parameter named lst. The 
# function should add every element from lst that has an odd index to a new 
# list. The function should then return this new list.For example, 
# odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2]
def odd_indices(lst):
    new_list = []
    for index in range(1, len(lst), 2):
        new_list.append(lst[index])
    return new_list

# Create a function named exponents() that takes two lists as parameters named 
# bases and powers. Return a new list containing every number in bases raised 
# to every number in powers.
def exponents(bases, powers):
  new_list = []
  for num in bases:
    for item in powers:
      new_list.append(num ** item)
  return new_list

#Create a function named larger_sum() that takes two lists of numbers as 
# parameters named lst1 and lst2. The function should return the list whose 
# elements sum to the greater number. If the sum of the elements of each list 
# are equal, return lst1
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for e in lst1:
    sum1 += e
  for n in lst2:
    sum2 += n
  if sum1 > sum2:
    return lst1
  elif sum1 < sum2:
    return lst2
  else:
    return lst1

# Create a function that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater 
# than 9000. When this happens, the function should return the sum. If the sum 
# of all of the elements is never greater than 9000, the function should return
# total sum of all the elements. For example, if lst was [8000, 900, 120, 5000], 
# then the function should return 9020.  
def over_nine_thousand(lst):
    sum = 0
    for e in lst:
        sum += e
        if (sum > 9000):
            break
    return sum

# Write a function named same_values() that takes two lists of numbers of equal 
# size as parameters. The function should return a list of the indices where 
# the values were equal in lst1 and lst2
def same_values(lst1, lst2):
  new_list = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_list.append(index)
  return new_list

# Create a function named reversed_list() that takes two lists of the same size
# as parameters named lst1 and lst2. The function should return True if lst1 is
# the same as lst2 reversed. The function should return False otherwise.
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True















































