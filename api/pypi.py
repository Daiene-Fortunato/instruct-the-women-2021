import requests

def version_exists(package_name, version):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/{version}/json")
    if response.status_code == 200:
        return True
    else:
        return False


def latest_version(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    if response.status_code == 404:
        return "None"
    else:
        response = response.json()
        return list(response['releases'].keys())[-1]
