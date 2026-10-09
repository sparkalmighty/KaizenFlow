from backend.app import app


def test_admin_login_sidebar_and_logout_flow():
    client = app.test_client()

    assert client.get('/').status_code == 200
    assert client.get('/login').status_code == 200
    assert client.get('/admin').status_code == 302
    assert client.get('/members').status_code == 302
    assert client.get('/attendance').status_code == 302

    response = client.post('/api/login', json={'username': 'admin', 'password': 'admin123'})
    assert response.status_code == 200
    assert response.json['redirect'] == '/admin'
    assert client.get('/admin').status_code == 200
    assert client.get('/members').status_code == 200
    assert client.get('/attendance').status_code == 200
    assert client.get('/components/sidebar.html').status_code == 200

    assert client.get('/logout').status_code == 302
    assert client.get('/admin').status_code == 302
