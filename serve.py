from livereload import Server

server = Server()
server.watch("**/*.html")
server.watch("**/*.js")
server.watch("**/*.css")
server.serve(root=".", port=8000, open_url_delay=1)
