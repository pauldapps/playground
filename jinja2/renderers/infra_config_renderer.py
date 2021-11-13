from jinja2 import Environment, FileSystemLoader
import yaml
import re
import itertools
import os


os.chdir(
    r"C:\Users\pauld\Nextcloud\Documents\Scripts\Gitlab\test-project\jinja2\renderers"
)
with open("../config/Infra_config.example.yaml", "r") as ymlfile:
    data = yaml.safe_load(ymlfile)


jienv = Environment(loader=FileSystemLoader("../templates/infra"))

templates = [jienv.get_template(t) for t in jienv.list_templates()]
ups_temp = [i for i in templates if re.search("ups", i.name)][0]
pdu_temp = [i for i in templates if re.search("pdu", i.name)][0]
switch_temp = [i for i in templates if re.search("switch", i.name)][0]

for sw, ups, pdu in itertools.zip_longest(data["switches"], data["UPS"], data["PDU"]):

    if sw:
        sw_output = switch_temp.render(data=sw)
        with open(f"../output/{sw['hostname']}_config_output.example.txt", "w") as file:
            for line in sw_output:
                file.write(line)

    if ups:
        ups_output = ups_temp.render(data=ups)
        with open(
            f"../output/{ups['hostname']}_config_output.example.txt", "w"
        ) as file:
            for line in ups_output:
                file.write(line)

    if pdu:
        pdu_output = pdu_temp.render(data=pdu)
        with open(
            f"../output/{pdu['hostname']}_config_output.example.txt", "w"
        ) as file:
            for line in pdu_output:
                file.write(line)
