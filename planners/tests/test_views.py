from django.urls import reverse


def test_add_planner_page_with_logged_in_user(client, user):
    url = reverse('planners:planner-create')

    client.login(email=user.email, password='testPass123')
    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Create Planner</h1>' in response.content.decode('UTF-8')


def test_add_planner_page_without_logged_in_user(client):
    url = reverse('planners:planner-create')

    response = client.get(url)

    assert response.status_code == 302
