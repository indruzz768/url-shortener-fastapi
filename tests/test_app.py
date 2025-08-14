from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
  r = client.get('/health')
  assert r.status_code == 200
  assert r.json()['status'] == 'ok'

def test_shorten_and_redirect():
  payload = {"original_url": "https://example.com/abc"}
  r = client.post('/shorten/', json=payload)
  assert r.status_code == 201
  data = r.json()
  assert 'short_code' in data
  r2 = client.get('/' + data['short_code'], allow_redirects=False)
  assert r2.status_code in (302, 307)
  assert r2.headers['location'] == payload['original_url']
