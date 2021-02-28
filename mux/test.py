# import sys
# import requests
# import collections
# from openpyxl import Workbook
# import csv
# #import pandas as pd


# class GithubAPI:
#     results = []
#     raw = []
#     issues_payload = {
#         "per_page": 100,
#         "page": 1,
#         "state": "all",
#     }
#     auth = ("himani0115", "6a7e57e12e821ab4540e6fadc5dcdf5876b00ae5")

#     def getIssues(self, url):

#         self.issues_payload = {
#             "per_page": 100,
#             "page": 1,
#             "state": "all",
#         }

#         self.raw = []

#         r = requests.get(url, params=self.issues_payload, auth=self.auth).json()

#         while (True):
#             self.raw += r
#             print( self.raw)
#             print(len(self.raw))
#             if len(r) == 100:
#                 self.issues_payload["page"] += 1
#                 r = requests.get(url, params=self.issues_payload, auth=self.auth).json()
#             else:
#                 break
#         for e in self.raw:
#             print("Checking issue " + str(e["number"]))

#             issue = collections.OrderedDict()
#             issue["id"] = e["id"]
#             issue["number"] = e["number"]
#             issue["repo_url"] = e["repository_url"]
#             issue["issue_url"] = e["url"]
#             issue["events_url"] = e["events_url"]
#             issue["state"] = e["state"]
#             issue["html_url"] = e["html_url"]
#             issue["title"] = e["title"]
#             # issue["description"] = e["body"]
#             issue["comments"] = e["comments"]
#             issue["created_at"] = e["created_at"]
#             issue["updated_at"] = e["updated_at"]
#             issue["closed_at"] = e["closed_at"]
#             if not e["milestone"]:
#                 issue["milestone"] = "null"
#             else:
#                 issue["milestone"] = e["milestone"]["title"]

#             labels = []

#             for label in e["labels"]:
#                 labelIssue = collections.OrderedDict()
#                 labelIssue["issue_repo_url"] = e["repository_url"]
#                 labelIssue["issue_id"] = e["id"]
#                 labelIssue["issue_number"] = e["number"]
#                 labelIssue["label_id"] = label["id"]
#                 labelIssue["label"] = label["name"]
#                 labels.append(labelIssue)
#                 # self.results.append(labelIssue)

#             issue["labels"] = labels

#             self.results.append(issue)
#         print(self.results,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#         return self.results


# if __name__ == "__main__":

#     apps = open('hi.csv' )
#     csv_apps = csv.reader(apps)

#     for row in csv_apps:
#         try:
#             app_source = row[0].replace("//github.com", "//api.github.com/repos")
#             print(app_source,)
#         except:
#             pass

#         print("=============================")
#         print(app_source)
#         print("=============================")

#         api = GithubAPI()

#         print("Getting issues...")
#         try:
#             issues = api.getIssues(app_source)
#             print(issues,"$$$$$$$$$$$$$$$$$$$")
#         except:
#             pass

#         print("Creating issues.csv ...")

#         #  create csv file
#     with open("issues.csv", 'a', encoding='utf-8', newline="") as file:
#         writer = csv.writer(file)

#         writer.writerow(("id", "number", "issue_url", "repo_url", "events_url", "state", "html_url",
#                          "milestone", "title", "comments", "created_at", "uploaded_at", "closed_at"))

#         for issue in issues:
#             writer.writerow((issue["id"], issue["number"], issue["issue_url"], issue["repo_url"], issue["events_url"],
#                              issue["state"],
#                              issue["html_url"], issue["milestone"], issue["title"],
#                              issue["comments"], issue["created_at"], issue["updated_at"], issue["closed_at"]))

#             # =======================================================================================
#         print("Creating labels.csv...")

#     with open("labels.csv", 'a', encoding='utf-8', newline="") as file:
#         writer = csv.writer(file)

#         writer.writerow(("issue_repo_url", "issue_id", "issue_number", "label_id", "label"))

#         for issue in issues:
#             print(issue)
#             labels = issue["labels"]
#             print(labels,"jajjajajjaja")
#             for label in labels:
#                 writer.writerow((label["issue_repo_url"], label["issue_id"], label["issue_number"], label["label_id"],
#                                  label["label"]))


from pydriller import RepositoryMining
import csv

url_list = ['https://github.com/ansible/ansible-modules-extras',
            'https://github.com/geerlingguy/ansible-for-devops']

for commit in RepositoryMining(url_list).traverse_commits():
    for m in commit.modifications:
        print(
            "Author {}".format(commit.author.name),
            " modified file {}".format(m.filename),
            " with a change type of {}".format(m.change_type.name),
            " and the complexity is {}".format(m.complexity),
            " and in path:{}".format(commit.project_path),
            " with the Message:''{}''".format(commit.msg),
            " and it contains {} methods".format(len(m.methods)),
            " in commit hash {} ".format(commit.hash),
            " in commit branch {} ".format(commit.branches),
            " with a COMMIT action {}".format(m.change_type),
            " with {} added lines".format(m.added),
            " and {} deleted lines".format(m.removed),
            " having the following code {}".format(m.diff),
            " with NLOC {} ".format(m.nloc)
        )