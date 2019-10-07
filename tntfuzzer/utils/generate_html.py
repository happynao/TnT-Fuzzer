from jinja2 import Environment, FileSystemLoader

def generate_html(body):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('tntfuzzer/utils/template.html')
    with open("result.html", 'w+') as fout:
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
    generate_html(body)
