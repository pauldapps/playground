from jinja2 import Environment, FileSystemLoader
import yaml

with open("./template_data.yaml", "r") as ymlfile:
    data = yaml.safe_load(ymlfile)

jienv = Environment(
    loader=FileSystemLoader(
        r"""C:\Users\pauld\Nextcloud\Documents\Scripts\Gitlab\test-project\templates"""
    )
)

template = jienv.get_template("jinja.template.exmaple.j2")
template.render(data=data)
