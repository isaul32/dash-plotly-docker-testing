from flask import Response, json
from dash import Dash, html
import dash

app = Dash(
    __name__,
    use_pages=True,
)

server = app.server

app.layout = html.Div([
	dash.page_container,
])


@server.route("/health")
def health():
    return Response(json.dumps({"status": "UP"}), mimetype="application/json")


if __name__ == "__main__":
    app.run_server(debug=True)
