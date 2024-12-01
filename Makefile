.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv sync
	@uv run pre-commit install

.PHONY: install-only
install-only: ## Only install the uv environment
	@echo "🆕 Creating virtual environment using uv"
	@uv sync

.PHONY: sync
sync: ## Resolve all dependencies of the project and write the exact versions into uv.lock
	@echo "🚀 Updating virtual environment and uv.lock based on pyproject.toml"
	@uv sync --frozen

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Linting code: Running pre-commit"
	@uv run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@uv run mypy --install-types --non-interactive

.PHONY: lock
lock: ## Generate new uv.lock file
	@echo "🚀 Generating new uv lock file consistent with 'pyproject.toml'"
	@uv lock

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@uv run pytest tests -vv

.PHONY: build
build: clean-build ## Build wheel file using uv
	@echo "🚀 Creating wheel file"
	@uv build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist



.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
