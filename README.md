## Fetches all projects from the JIRA workspace
This script interacts with JIRA's REST API to retrieve all projects available in the workspace. It sends a GET request to the API endpoint: https://your-domain.atlassian.net/rest/api/3/project
When this request is made with proper authentication, the API responds with a list of projects, including their details such as ID, Name, Key, and Type.
## Uses Basic Authentication (Email + API Token)
JIRA's REST API requires authentication to prevent unauthorized access. This script uses Basic Authentication, which consists of:

Email: Your Atlassian account email
API Token: A secure authentication token generated from JIRA
Instead of a password, API tokens are recommended for security reasons.

The authentication is handled using Python’s requests.auth.HTTPBasicAuth
## Prints project names in JSON format
Once the API request is successful, the script extracts the project details and prints them in a formatted JSON structure.

Additionally, the script extracts and prints the first project name by adding code snippet: 
name = output[0]["name"]
print(name)

## Summary:
The script retrieves a list of projects from JIRA.
It authenticates securely using Basic Authentication (Email + API Token).
The response is formatted and displayed in JSON format for better readability.
It extracts and prints the project names.
