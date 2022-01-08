from indeed import get_jobs as get_jobs1


from so import get_jobs as get_so_jobs

from save import save_to_file

get_jobs2=get_jobs1() #indeed

so_jobs=get_so_jobs() #stackoverflow

jobs=get_jobs2+so_jobs
save_to_file(jobs)
