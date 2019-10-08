from builtins import OSError

from jinja2 import Environment, FileSystemLoader
import os

def generate_html(body, report_dir):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('tntfuzzer/utils/template.html')
    dirname = os.path.dirname(report_dir)
    if not os.path.exists(os.path.dirname(report_dir)):
        try:
            os.makedirs(os.path.dirname(report_dir))
        except OSError:
            pass
    path_file = r"{}fuzz_testing_report.html".format(report_dir)
    with open(path_file, mode='w+', encoding='utf-8', buffering=1) as fout:
        html_content = template.render(body=body)
        fout.write(html_content)


if __name__ == "__main__":
    body = []
    obj = {"op_code": "GET", "url": "abc", "status_code": 500,
           "response_msg": "ok", "body": "body", "curl_command": "curl_command"}
    obj2 = {"op_code": "POST", "url": "abc", "status_code": 500,
           "response_msg": "ok", "body": "body", "curl_command": "curl_command"}
    body.append(obj)
    body.append(obj2)
    generate_html(body, "/tmp/reports/")
