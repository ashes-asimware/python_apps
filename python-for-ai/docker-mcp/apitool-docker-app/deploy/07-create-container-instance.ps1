# 07-create-container-instance.ps1
# Create Azure Container Instance to run the Docker image

param(
    [Parameter(Mandatory=$false)]
    [string]$Version = "latest"
)

$resourceGroup = "ashes-gm-002-rg"
$containerName = "imageapi-container"
$registryName = "imageapiregistry5536"
$imageName = "imageapi"
$dnsNameLabel = "imageapi-app-6264"
$ports = @(8443, 8080)
$cpu = 1
$memory = 1

# Load ACR credentials
if (Test-Path "$PSScriptRoot\acr-credentials.json") {
    $credentials = Get-Content "$PSScriptRoot\acr-credentials.json" | ConvertFrom-Json
    $acrUsername = $credentials.Username
    $acrPassword = $credentials.Password
} else {
    Write-Host "Retrieving ACR credentials..." -ForegroundColor Yellow
    $acrPassword = az acr credential show `
        --name $registryName `
        --resource-group $resourceGroup `
        --query "passwords[0].value" `
        -o tsv
    $acrUsername = $registryName
}

$imageFullPath = "$registryName.azurecr.io/${imageName}:${Version}"

Write-Host "Creating Azure Container Instance: $containerName" -ForegroundColor Green
Write-Host "Image: $imageFullPath" -ForegroundColor Cyan

az container create `
    --resource-group $resourceGroup `
    --name $containerName `
    --image $imageFullPath `
    --registry-login-server "$registryName.azurecr.io" `
    --registry-username $acrUsername `
    --registry-password $acrPassword `
    --dns-name-label $dnsNameLabel `
    --ports 8443 8080 `
    --protocol TCP `
    --cpu $cpu `
    --memory $memory

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Container Instance created successfully" -ForegroundColor Green
    Write-Host "FQDN: $dnsNameLabel.eastus.azurecontainer.io" -ForegroundColor Cyan
    Write-Host "API URL: https://$dnsNameLabel.eastus.azurecontainer.io:8443" -ForegroundColor Cyan
    Write-Host "Web App URL: https://$dnsNameLabel.eastus.azurecontainer.io:8080" -ForegroundColor Cyan
    Write-Host "Web App URL: https://$dnsNameLabel.eastus.azurecontainer.io:8080" -ForegroundColor Cyan
} else {
    Write-Host "✗ Failed to create Container Instance" -ForegroundColor Red
    exit 1
}
