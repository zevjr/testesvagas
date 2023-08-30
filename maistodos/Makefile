API=api

CDAPI=cd $(API);

dev:
	$(CDAPI) uvicorn asgi:application --reload --host 0.0.0.0 --port 8001

format:
	$(CDAPI) sh scripts/format-imports.sh

test:
	$(CDAPI) sh scripts/test.sh

lint:
	$(CDAPI) sh scripts/lint.sh

cov:
	$(CDAPI) sh scripts/test-cov-html.sh
