from github import Github

g = Github()
for i, repo in enumerate(g.search_repositories("windows+label:bug+language:python+state:open&sort=created&order=asc")):
    print(repo)
   