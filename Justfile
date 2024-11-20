@test: 
  poetry run pytest -vvv tests/test_client.py --log-cli-level=DEBUG

@roll:
  poetry add wheels/parlant-0.4.1a1-py3-none-any.whl

@plug:
  poetry run python tests/example_plugin.py

@serv:
  poetry run parlant-server -p 8012

@clean:
  rm -rf .parlant-cache