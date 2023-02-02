import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.scalars import JSON

from src.password_check import PassRules


@strawberry.type
class Password:
    verify: bool
    noMatch: list[JSON]


@strawberry.type
class Query:
    @strawberry.field
    def verify(self, password: str, rules: list[JSON]) -> Password:
        check = PassRules(password, rules)
        check_all = check.check_all()
        verify = check.verify

        return Password(verify=verify, noMatch=check_all)


schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route('/graphql', graphql_app)
app.add_websocket_route('/graphql', graphql_app)
