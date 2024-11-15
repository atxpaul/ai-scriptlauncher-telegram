import argparse
import requests

def health_check(server_name):
    """
    Realiza un health check a un servidor.
    """
    url = f"http://{server_name}/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{server_name} está ok.")
        else:
            print(f"{server_name} respondió con el código {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error al verificar {server_name}: {e}")


parser = argparse.ArgumentParser(description='Check servers')
parser.add_argument('--names', nargs='+', required=True, help='Nombres o URLs de los servidores a verificar')

args = parser.parse_args()


for server_name in args.names:
    health_check(server_name)
