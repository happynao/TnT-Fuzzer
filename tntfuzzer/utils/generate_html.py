import os
import ntpath

from builtins import OSError
from jinja2 import Environment, FileSystemLoader


def generate_html(body, report_dir, build_id):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('utils/template.html')
    path = "{}/{}/".format(report_dir, build_id)
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            pass
    with open(r"{}fuzz_testing_report.html".format(path), mode='w+', encoding='utf-8', buffering=1) as f:
        html_content = template.render(body=body)
        f.write(html_content)

def generate_report(report_dir, files):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('utils/index.html')
    if not os.path.exists(os.path.dirname(report_dir)):
        try:
            os.makedirs(os.path.dirname(report_dir))
        except OSError:
            pass
    with open(r"{}index.html".format(report_dir), mode='w+', encoding='utf-8', buffering=1) as f:
        html_content = template.render(files=files)
        f.write(html_content)

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    # Iterate over all the entries
    allFiles = dict()
    for entry in listOfFile:
        #Create full path
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles[entry] = os.path.join(fullPath, "fuzz_testing_report.html")
        #     allFiles = allFiles + getListOfFiles(fullPath)
        # else:
        #     allFiles.append(fullPath)
    return allFiles

# def path_leaf(path):
#     head, tail = ntpath.split(path)
#     path1, build_id = ntpath.basename(head)
#     return path1

if __name__ == "__main__":
    # body = []
    # obj = {"op_code": "GET", "url": "abc", "status_code": 500,
    #        "response_msg": "ok", "body": "body", "curl_command": "curl_command"}
    # obj2 = {"op_code": "POST", "url": "abc", "status_code": 500,
    #        "response_msg": "ok", "body": "body", "curl_command": "curl_command"}
    # body.append(obj)
    # body.append(obj2)
    # generate_html(body, "/tmp/reports/")
    list_of_files = getListOfFiles("/tmp/reports_test/")
    #generate_report("/tmp/reports/", list_of_files)
