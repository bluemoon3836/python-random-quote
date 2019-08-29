import random

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt", 'rt', encoding='UTF8')
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0,last)

  print(quotes[rnd])

if __name__== "__main__":
 main()
