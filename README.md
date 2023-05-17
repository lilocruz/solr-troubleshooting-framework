# Solr Troubleshooting Framework

The Solr Troubleshooting Framework is a Python module and command-line tool that helps in troubleshooting and diagnosing issues with Apache Solr installations. It provides a set of functions and commands to perform various checks on the Solr server, core, queries, fields, and logs.

## Features

- Check Solr server availability and ping
- Verify the existence of Solr cores
- Execute Solr queries and check for results
- Validate the presence of specific fields in Solr cores
- Search for error messages in Solr log files

## Installation

To install the Solr Troubleshooting Framework, you can use pip:

```bash
pip install stsf
```

## Usage

The Solr Troubleshooting Framework can be used both as a Python module and as a command-line tool.

## Python Module

```python
import stsf

# Perform Solr checks
# ...

# Example usage: check Solr ping
solr_url = "http://localhost:8983/solr"
if stsf.check_solr_ping(solr_url):
    print("Solr server is responding.")
else:
    print("Solr server is not responding.")
```

## Command-Line Tool

The Solr Troubleshooting Framework provides CLI commands for each check. Here are some examples:

```bash
# Check Solr server ping
stsf check-ping http://localhost:8983/solr/{core-name}

# Check Solr core existence
stsf check-core http://localhost:8983/solr my_core

# Check Solr query results
stsf check-query http://localhost:8983/solr "*:*"

# Check Solr field existence
stsf check-field http://localhost:8983/solr my_core my_field

# Search for error message in Solr log
stsf check-log /var/log/solr.log "Error: Could not create index"
```

## Contributing

Contributions to the Solr Troubleshooting Framework are welcome! If you find any issues, have suggestions for improvements, or would like to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the GPLv3 License.


