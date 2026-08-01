# 01-create-resource-group.ps1
# Create Azure Resource Group for the Image API application

$resourceGroup = "ashes-gm-002-rg"
$location = "eastus"

Write-Host "Creating resource group: $resourceGroup in $location" -ForegroundColor Green

az group create `
    --name $resourceGroup `
    --location $location

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Resource group created successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to create resource group" -ForegroundColor Red
    exit 1
}
