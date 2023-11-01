# Define your Azure DevOps organization URL and PAT (Personal Access Token)
$organizationUrl = "https://dev.azure.com/pratham14079"
$pat = "qs2rixaw5y2uvhvq5bzdrff7uooe7cbrzc2myth5bx5yd4pd6qlq"

# Set the API version and the work item ID you want to retrieve
$apiVersion = "7.0"
# Define the REST API URL to list projects
$uri = "$organizationUrl/_apis/projects?api-version=$apiVersion"

# Create headers with the PAT for authentication
$headers = @{
    Authorization = "Basic " + [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$($pat)"))
}

# Send the GET request
$response = Invoke-RestMethod -Uri $uri -Headers $headers -Method Get

# Check if the request was successful
if ($response.value.Count -gt 0) {
    # Iterate through the list of projects and display their names
    foreach ($project in $response.value) {
        Write-Host "Project Name: $($project.name)"
        Write-Host "Project ID: $($project.id)"
        Write-Host "-----------------------------"
    }
} else {
    Write-Host "No projects found in the organization."
}





