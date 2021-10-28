import requests
from requests import api
from requests.api import head

server = requests.get('https://api.rust-servers.info/status/5939')
server_info = server.json()
server_player = server_info['players']
server_status = server_info['status']
server_max_players = server_info['players_max']
server_fps = server_info['fps']
server_uptime = server_info['uptime']
server_ip = '102.223.196.222:27015'