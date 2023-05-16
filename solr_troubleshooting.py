# This is the first fuction of an Apache Solr troubleshooting framework that i'm creating.
# Right now the script is not very mature!!.
# Copytright: GPLv3
# AUTHOR: Michael Sanchez (Search Engineer at Lucidworks)

import requests

def check_solr_ping(solr_url):
    # Will check if solr is up & running
    try:
        response = requests.get(solr_url + "/admin/ping", timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

# Core check function
def check_solr_core(solr_url, core_name):
    # Check if the core exists
    try:
        response = requests.get(solr_url + "/admin/cores?action=STATUS&core=" + core_name, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

# Query check function
def check_solr_query(solr_url, query):
    # Check if a Solr query returns any results
    try:
        response = requests.get(solr_url + "/select?q=" + query, timeout=5)
        if response.status_code == 200:
            response_json = response.json()
            if response_json["response"]["numFound"] > 0:
                return True
    except:
        pass
    return False

# Field check function
def check_solr_field(solr_url, core_name, field_name):
    # Check if a Solr core has a field
    try:
        response = requests.get(solr_url + "/" + core_name + "/schema/fields/" + field_name, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

# Log check function
def check_solr_log(solr_log_path, error_message):
    # Check if a specific error message appears in the Solr log file
    try:
        with open(solr_log_path, "r") as log_file:
            log_text = log_file.read()
            if error_message in log_text:
                return True
    except:
        pass
