pyg = 'ay'
#to pig latin
def spliter():

  text = raw_input('Enter (a) word(s): ')
  words = text.split()
  jword = []
    # for each word in the line:
  for word in words:

    sword = word.lower()
    first = sword[0]
    new_word = sword + first + pyg
    new_word = new_word[1:len(new_word)]
    jword.append(new_word)
  print " ".join(jword)
    
  
#from pig latin
def back_spliter():

  original = raw_input('Enter (a) Pig Latin word(s): ')
  words = original.split()
  jword = []
  for word in words:

    word = word.lower()
    first = word[len(word)-3]
    new_word = word[0:len(word)-3]
    new_word = first + new_word
    jword.append(new_word)
  print " ".join(jword)
not_done = True
while not_done:

  print "Welcome to the Pig latin translator: "
  type = raw_input('Would you like to translate To or From Pig latin?: ')

  if type == "To" or type == "to":
    spliter()
    not_done = False
  elif type == "From" or type == "from":
    back_spliter()
    not_done = False
  else:
    print "Try again"
  