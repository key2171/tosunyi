import requests
from bs4 import BeautifulSoup

limit = 50
url = f"https://kr.indeed.com/취업?q=python&limit={limit}&radius=25"


def extract_indeed_pages():
    # 나는 토순이다.
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    # 주석 테스트

    return (max_page)


def extract_jobs(html):
    title = html.find("h2", {
        "class": "jobTitle"
    }).find("span", title=True).string

    company = html.find("span", {"class": "companyName"})
    if company:
      company_anchor=company.find("a")
      if company_anchor is not None:
          company=str(company_anchor.string)
      else :
          company=str(company.string)
    else:
      company=None 
    location = html.find("div", {"class": "companyLocation"}).text
    job_id = html["data-jk"]

    return {
    'title':title,
    'company':company,
    'location': location,
    'link': f"https://kr.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"
}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
      print(f"Scrapping Indeed: Page {page}")
      result = requests.get(f"{url}&start={page*limit}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("a", {"class": "result"})
      
      for result in results:
        job = extract_jobs(result)
        jobs.append(job)
    return jobs

def get_jobs():
  last_indeed_pages=extract_indeed_pages()
  indeed_jobs=extract_indeed_jobs(last_indeed_pages)
  return indeed_jobs
