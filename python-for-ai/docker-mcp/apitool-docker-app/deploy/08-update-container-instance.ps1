# 08-update-container-instance.ps1
# Update existing Azure Container Instance with new image version

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

Write-Host "Updating Container Instance to version: $Version" -ForegroundColor Green

# Get ACR credentials
$acrPassword = az acr credential show `
    --name $registryName `
    --resource-group $resourceGroup `
    --query "passwords[0].value" `
    -o tsv

$imageFullPath = "$registryName.azurecr.io/${imageName}:${Version}"

# Delete existing container
Write-Host "Deleting existing container..." -ForegroundColor Yellow
az container delete `
    --resource-group $resourceGroup `
    --name $containerName `
    --yes

# Create new container with updated image
Write-Host "Creating new container with image: $imageFullPath" -ForegroundColor Green

az container create `
    --resource-group $resourceGroup `
    --name $containerName `
    --image $imageFullPath `
    --registry-login-server "$registryName.azurecr.io" `
    --registry-username $registryName `
    --registry-password $acrPassword `
    --dns-name-label $dnsNameLabel `
    --ports 8443 8080 `
    --protocol TCP `
    --cpu $cpu `
    --memory $memory

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Container Instance updated successfully" -ForegroundColor Green
    Write-Host "Version: $Version" -ForegroundColor Cyan
    Write-Host "API URL: https://$dnsNameLabel.eastus.azurecontainer.io:8443" -ForegroundColor Cyan
    Write-Host "Web App URL: https://$dnsNameLabel.eastus.azurecontainer.io:8080" -ForegroundColor Cyan
} else {
    Write-Host "✗ Failed to update Container Instance" -ForegroundColor Red
    exit 1
}
