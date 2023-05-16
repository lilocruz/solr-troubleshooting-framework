# This is the first fuction of an Apache Solr troubleshooting framework that i'm creating.
# Right now the script is not very mature!!.
# Copytright: GPLv3
# AUTHOR: Michael Sanchez (Search Engineer at Lucidworks)

import requests

def check_solr_ping(solr_url):
    try:
        response = requests.get(f"{solr_url}/admin/ping", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def check_solr_core(solr_url, core_name):
    try:
        response = requests.get(f"{solr_url}/admin/cores?action=STATUS&core={core_name}", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def check_solr_query(solr_url, query):
    try:
        response = requests.get(f"{solr_url}/select?q={query}", timeout=5)
        if response.status_code == 200:
            response_json = response.json()
            return response_json["response"]["numFound"] > 0
        return False
    except requests.RequestException:
        return False

def check_solr_field(solr_url, core_name, field_name):
    try:
        response = requests.get(f"{solr_url}/{core_name}/schema/fields/{field_name}", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def check_solr_log(solr_log_path, error_message):
    try:
        with open(solr_log_path, "r") as log_file:
            log_text = log_file.read()
            return error_message in log_text
    except IOError:
        return False
