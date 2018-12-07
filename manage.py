from sshtunnel import SSHTunnelForwarder
import sys

args = sys.argv

server = SSHTunnelForwarder(
    ('example.com', 22),
    ssh_username="name",
    ssh_password="pass",
    remote_bind_address=('0.0.0.0', 8080),
    local_bind_address=('0.0.0.0', int(args[1]))
)

server.start()
