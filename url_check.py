import os
import requests

# input_u=input("url을 입력하세요.")
# url_1=" google. com, http s://naver.com, daum.net, abcde "
# url=input_u.replace(" ","").split(',')
http='https://'


def game_start():
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (seperated by comma)")
  input_u = input()
  url_1=input_u.replace(" ","").split(',')
  return url_1
url=game_start()

# url 수정
def url_mod(*url):
  mURL=[]
  for x in url:
    ck= "https" not in x
    if ck is True:
      x_1=http+x
    else:
      x_1=x
    mURL.append(x_1)
  return mURL
mURL=url_mod(*url)

# url check
def abc(mURL):
   for x in mURL:
    try:
      x_req=requests.get(x).status_code
    except requests.exceptions.RequestException:
      print(f"{x} is not a valid URL.")
    if x_req == 200:
      print(f"{x} is up!")
    elif x_req == 404:
      print(f"{x} is down!")         
abc(mURL)

def game_again():
  is_terminated = input("Do you want to start over? y/n ")
  if is_terminated == 'y':
    os.system('clear')
    game_start()
  elif is_terminated == 'n':
    print("ok. bye~")
    return
  else:
    print("That's not a valid answer")
    game_again()

game_again()

if __name__ == "__main__":
  game_start()
