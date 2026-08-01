# 02-create-container-registry.ps1
# Create Azure Container Registry for storing Docker images

$resourceGroup = "ashes-gm-002-rg"
$registryName = "imageapiregistry5536"
$sku = "Basic"

Write-Host "Creating Azure Container Registry: $registryName" -ForegroundColor Green

az acr create `
    --resource-group $resourceGroup `
    --name $registryName `
    --sku $sku `
    --admin-enabled true

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Container Registry created successfully" -ForegroundColor Green
    Write-Host "Registry Login Server: $registryName.azurecr.io" -ForegroundColor Cyan
} else {
    Write-Host "✗ Failed to create Container Registry" -ForegroundColor Red
    exit 1
}
