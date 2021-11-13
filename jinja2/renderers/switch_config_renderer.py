from jinja2 import Environment, FileSystemLoader
import yaml

with open("./switch_config.example.yaml", "r") as ymlfile:
    data = yaml.safe_load(ymlfile)

jienv = Environment(
    loader=FileSystemLoader(
        r"""C:\Users\pauld\Nextcloud\Documents\Scripts\Gitlab\test-project\jinja2\templates\switch"""
    )
)
template = jienv.get_template("switch_config_template.example.j2")

for switch in data["switches"]:
    output = template.render(data=switch)
    with open(f"{switch['hostname']}_config_output.example.txt", "w") as file:
        for line in output:
            file.write(line)
