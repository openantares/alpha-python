import json

import httpx

from alpha import Alpha


def test_search_sends_bearer_token_and_explicit_vault_scope() -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert request.url.path == "/v1/tools/search_knowledge"
        assert request.headers["authorization"] == "Bearer alpha_test_key"
        assert json.loads(request.content) == {
            "query": "Sample Contact",
            "vault": "vault_example",
        }
        return httpx.Response(
            200,
            json={"data": [{"id": "person_sample", "name": "Sample Contact"}]},
        )

    transport = httpx.MockTransport(handle)
    with httpx.Client(transport=transport) as http_client:
        client = Alpha(
            base_url="https://alpha.test",
            httpx_client=http_client,
            max_retries=0,
            token="alpha_test_key",
        )
        response = client.knowledge.search_knowledge(
            query="Sample Contact",
            vault="vault_example",
        )

    assert response.data == [{"id": "person_sample", "name": "Sample Contact"}]


def test_add_task_sends_named_owner_without_the_retired_side_field() -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert request.url.path == "/v1/tools/add_task"
        assert json.loads(request.content) == {
            "title": "Confirm launch owner",
            "vault": "vault_example",
            "assigneeName": "Example Owner",
        }
        return httpx.Response(200, json={"data": {"identifier": "EX-9"}})

    transport = httpx.MockTransport(handle)
    with httpx.Client(transport=transport) as http_client:
        client = Alpha(
            base_url="https://alpha.test",
            httpx_client=http_client,
            max_retries=0,
            token="alpha_test_key",
        )
        response = client.actions.add_task(
            title="Confirm launch owner",
            vault="vault_example",
            assignee_name="Example Owner",
        )

    assert response.data == {"identifier": "EX-9"}
