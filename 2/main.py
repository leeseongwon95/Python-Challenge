"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

def add_to_dict(dic=None, key=None, value=None):
  if str(type(dic)) != "<class 'dict'>":
    print(f"You need to send a dictionary. you sent: {type(dic)}")
    return
  elif key == None or value == None:
    print("You Need to send a word and a definition.")
    return
  elif key in dic:
    print(f"{key} is already on the dictionary. Won't add.")
    return
  dic[key] = value
  print(f"{key} has been added.")
  

def get_from_dict(dic=None, key=None):
  if str(type(dic)) != "<class 'dict'>":
    print(f"You need to send a dictionary. You sent: {type(dic)}")
    return
  elif key == None:
    print("You need to send a word to search for.")
    return
  elif key in dic:
    print(f"{key}: {dic[key]}")
    return
  else:
    print(f"{key} was not found in this dict.")
    return
  

def update_word(dic=None, key=None, value=None):
  if str(type(dic)) != "<class 'dict'>":
    print(f"You need to send a dictionary. You sent: {type(dic)}")
    return
  elif key == None or value == None:
    print("You need to send a word and a definition for update.")
    return
  elif key in dic:
    print(f"{key} has been updated to: {value}")
    dic[key] = value
    return
  else:
    print(f"{key} is not on the dict. Can't update non-existing word.")
    return


def delete_from_dict(dic=None, key=None):
  if str(type(dic)) != "<class 'dict'>":
    print(f"You need to send a dictionary. you sent:{type(dic)}")
    return
  elif key == None:
    print("You need to specify a word to delete.")
    return
  elif key not in dic:
    print(f"{key} is not in this dict. Won't delete.")
    return
  else:
    print(f"{key} has been delete")
    del dic[key]
    return
  

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\