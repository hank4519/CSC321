from bcrypt import hashpw
from nltk.corpus import words
from multiprocessing import Process

ENCODING = 'utf-8'

class User:
  def __init__(self, name:str, salt:bytes, hash:bytes) -> None:
    self.name = name
    self.salt = salt
    self.hash = hash
  
  def __repr__(self):
    return self.name

def crack(users:'list[User]'):
  user_dict = dict()
  for user in users:
    if user.salt in user_dict.keys():
      user_dict[user.salt].append(user)
    else:
      user_dict[user.salt] = [user]
  for salt in user_dict.keys():
    # crack_by_salt(user_dict[salt])
    p = Process(target=crack_by_salt, args=(user_dict[salt], ))
    p.start()
    p.join()

def crack_by_salt(user_list: 'list[User]'):
  salt = user_list[0].salt
  word_list = [w for w in words.words() if len(w) >= 6 and len(w) <= 10]
  for word in word_list:
    hash_pass = hashpw(word.encode(ENCODING), salt)
    for user in user_list:
      if hash_pass == user.hash:
        print(f'{user.name} password: {word}')

def read_users():
  users = []
  with open('shadow.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      name_split = line.split(':')
      hash_split = line.split('$')
      name = name_split[0]
      salt = name_split[1][:29]
      hash_val = name_split[1].strip()
      print(name, salt, hash_val)
      # users.append(User(name, salt, hash_val))
  # return users

def main():
  read_users() 
  # crack(read_users())

if __name__ == '__main__':
  main()