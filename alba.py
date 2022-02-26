import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


def save_to_file(jobs):
    file=open(f"{jobs['name']}.csv", mode="w")
    writer=csv.writer(file)
    writer.writerow(["location", "company", "time", "pay", "update"]) 
    for job in jobs["jobs"]:
      writer.writerow(list(job.values()))
    print(f"Completed....{jobs['name']}")

# 슈퍼브랜드 page 추출, 
def extract_alba_pages():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  superrecruit = soup.find("div", {"id":"MainSuperBrand"})
  return superrecruit
page=extract_alba_pages()

# 링크 추출
linkes = page.find_all("a", {"class":"brandHover"})
for x in linkes:
  link = x.attrs['href']
# 슈퍼브랜드 company name 추출
  company_name = x.get_text(strip=1).replace("브랜드채용관","").strip(">")
# company에 name 생성
  if company_name is not None:
    company=company_name.replace("/", " ")
    company={'name': company, 'jobs': []}
   
  # 링크의 각 페이지 추출 
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find_all("tr", {"class":""})
    for z in pages: 
  # 링크의 페이지에서 구직내용 추출 후 컴퍼니별 저장
      location = z.find("td", {"class":"local first"})
      if location is not None:
        location=location.get_text(strip=1).replace("\xa0", " ")
      else:
        pass
      company = z.find("span", {"class":"company"})
      if company is not None:
        company =company.get_text(strip=1)
      else:
        pass
      time = z.find("span", {"class":"time"})
      if time is not None:
        time = time.get_text(strip=1)
      else:
        pass
      pay = z.find("td", {"class":"pay"})
      if pay is not None:
        pay = pay.get_text(strip=1)
      else:
        pass
      update = z.find("td", {"class":"regDate last"})
      if update is not None:
        update = update.get_text(strip=1)
      else:
        pass
      job = {"location":location, "company":company,  "time":time, "pay":pay, "update":update}  
      company['jobs'].append(job)
  
  # save_to_file(company) 
       

