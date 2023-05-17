# This is the first phase of an Apache Solr troubleshooting framework that i'm creating.
# Right now the script is not very mature is using the click module to create a CLI version of the application.
# Copytright: GPLv3
# AUTHOR: Michael Sanchez (Search Engineer at Lucidworks)

import click
import requests

@click.group()
def stsf():
    # Solr troubleshooting commands
    pass

@stsf.command()
@click.argument('solr_url')
def check_ping(solr_url):
    #Check if Solr server is responding
    try:
        response = requests.get(f"{solr_url}/admin/ping", timeout=5)
        if response.status_code == 200:
            click.echo("Up & Running, Happy Solring!")
        else:
            click.echo("Solr server is DOWN...")
    except requests.RequestException:
        click.echo("Solr server is DOWN...")

@stsf.command()
@click.argument('solr_url')
@click.argument('core_name')
def check_core(solr_url, core_name):
    #Check if a Solr core exists
    try:
        response = requests.get(f"{solr_url}/admin/cores?action=STATUS&core={core_name}", timeout=5)
        if response.status_code == 200:
            click.echo(f"Solr core '{core_name}' exists.")
        else:
            click.echo(f"Solr core '{core_name}' does not exist.")
    except requests.RequestException:
        click.echo(f"Solr core '{core_name}' does not exist.")

@stsf.command()
@click.argument('solr_url')
@click.argument('query')
def check_solr_query(solr_url, query):
    #Check if a Solr query returns any results
    try:
        response = requests.get(f"{solr_url}/select?q={query}", timeout=5)
        if response.status_code == 200:
            response_json = response.json()
            num_found = response_json["response"]["numFound"]
            if num_found > 0:
                click.echo(f"The Solr query returned {num_found} results.")
            else:
                click.echo("The Solr query did not return any results.")
        else:
            click.echo("Error: Failed to execute the Solr query.")
    except requests.RequestException:
        click.echo("Error: Failed to execute the Solr query.")

@stsf.command()
@click.argument('solr_url')
@click.argument('core_name')
@click.argument('field_name')
def check_solr_field(solr_url, core_name, field_name):
    """Check if a Solr core has a specific field."""
    try:
        response = requests.get(f"{solr_url}/{core_name}/schema/fields/{field_name}", timeout=5)
        if response.status_code == 200:
            click.echo(f"The Solr core '{core_name}' has the field '{field_name}'.")
        else:
            click.echo(f"The Solr core '{core_name}' does not have the field '{field_name}'.")
    except requests.RequestException:
        click.echo(f"Error: Failed to check the field '{field_name}' in the Solr core '{core_name}'.")

@stsf.command()
@click.argument('solr_log_path')
@click.argument('error_message')
def check_solr_log(solr_log_path, error_message):
    """Check if a specific error message appears in the Solr log file."""
    try:
        with open(solr_log_path, "r") as log_file:
            log_text = log_file.read()
            if error_message in log_text:
                click.echo(f"The error message '{error_message}' was found in the Solr log file.")
            else:
                click.echo(f"The error message '{error_message}' was not found in the Solr log file.")
    except IOError:
        click.echo(f"Error: Failed to read the Solr log file at '{solr_log_path}'.")

if __name__ == '__main__':
    stsf()