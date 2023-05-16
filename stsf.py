# This is the actual program that does the debugging. It imports the "solr_troubleshooting" module.

import solr_troubleshooting

# Set up Solr URL and core name
solr_url = input("Enter your Solr URL in the format of (http://URL:PORT/solr): ")
core_name = input("Enter your Solr core name: ")

# Run diagnostic ping checks
if not solr_troubleshooting.check_solr_ping(solr_url + "/" + core_name):
    print("Solr server is not responding.")
else:
    print("Up & Running!")

# Check Core
if not solr_troubleshooting.check_solr_core(solr_url, core_name):
    print(f"Solr core '{core_name}' does not exist.")
else:
    print(f"The Core {core_name} was found!")

# Check Query
if not solr_troubleshooting.check_solr_query(solr_url + "/" + core_name, "*:*"):
    print("Solr query did not return any results.")
else:
    print("The query was succesful!")

# Check Field    
if not solr_troubleshooting.check_solr_field(solr_url, core_name, "my_field"):
    print(f"Solr core '{core_name}' does not have the 'my_field' field.")
else:
    print(f"Solr core '{core_name}' does have the 'my_field' field.")

# Check logs, note that the path for the log might vary.    
if not solr_troubleshooting.check_solr_log("server/logs/solr.log", "Error: Could not create index"):
    print("The Error: Could not create index' message not found in the Solr logs.")
else:
    print("The error was found in the solr logs!")

# If no errors were found, print success message
print("Solr installation is working correctly!!! Happy Solring.")
