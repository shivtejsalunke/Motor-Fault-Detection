.PHONY: test synthetic-demo clean

test:
	python -m pytest -q

synthetic-demo:
	PYTHONPATH=src python scripts/make_synthetic_fixture.py --out /tmp/motor_synthetic_fixture.npz
	PYTHONPATH=src python -m motor_fault_detection.train /tmp/motor_synthetic_fixture.npz --sampling-rate 1024 --out /tmp/motor-synthetic-results
	@echo 'NOTE: synthetic smoke-test metrics are not real-world performance.'

clean:
	rm -rf .pytest_cache src/motor_fault_detection/__pycache__ tests/__pycache__
