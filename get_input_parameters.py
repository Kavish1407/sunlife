import os
import yaml
stack_name = os.environ["stack_name"]
region = os.environ["region"]
NotebookInstanceName = os.environ["NotebookInstanceName"]
NotebookInstanceType = os.environ["NotebookInstanceType"]
SageMakerRoleArn = os.environ["SageMakerRoleArn"]
EBSVolumeSize = os.environ["EBSVolumeSize"]
input_parameters = {}
input_parameters["stack_name"] = stack_name
input_parameters["region"] = region
input_parameters["NotebookInstanceName"] = NotebookInstanceName
input_parameters["NotebookInstanceType"] = NotebookInstanceType
with open("input_vars.yml","w") as file:
    yaml.dump(input_parameters,file)

