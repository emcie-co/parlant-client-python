@test: 
  poetry run pytest -vvv tests/test_client.py --log-cli-level=DEBUG

@clean:
  rm -rf .parlant-cache