.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

CURDIR=$(shell pwd)
WORKDIR=/usr/src/myapp

run: ## Run the command python script.py 
	docker run -it -v $(CURDIR):$(WORKDIR) -w $(WORKDIR) python bash -c "pip install -r requirements.txt; python script.py"

enter: ## Enter into the docker
	docker run -it -v $(CURDIR):$(WORKDIR) -w $(WORKDIR) python bash -c "pip install -r requirements.txt; bash"
