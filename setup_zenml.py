import os
print("Registering config for zenml to match the image...")
os.system(r'.venv\Scripts\python -c "from zenml.cli.cli import cli; import sys; sys.argv=[\"zenml\", \"experiment-tracker\", \"register\", \"mlflow_tracker_prices_new\", \"--flavor=mlflow\"]; cli()"')
os.system(r'.venv\Scripts\python -c "from zenml.cli.cli import cli; import sys; sys.argv=[\"zenml\", \"model-deployer\", \"register\", \"mlflow_prices_new\", \"--flavor=mlflow\"]; cli()"')
os.system(r'.venv\Scripts\python -c "from zenml.cli.cli import cli; import sys; sys.argv=[\"zenml\", \"stack\", \"register\", \"local-mlflow-stack-prices-new\", \"-a\", \"default\", \"-o\", \"default\", \"-d\", \"mlflow_prices_new\", \"-e\", \"mlflow_tracker_prices_new\", \"--set\"]; cli()"')
