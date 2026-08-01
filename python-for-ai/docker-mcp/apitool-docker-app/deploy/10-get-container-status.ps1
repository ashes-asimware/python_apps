# 10-get-container-status.ps1
# Get status information for the Azure Container Instance

$resourceGroup = "ashes-gm-002-rg"
$containerName = "imageapi-container"

Write-Host "Getting container status..." -ForegroundColor Green

az container show `
    --resource-group $resourceGroup `
    --name $containerName `
    --query "{State:instanceView.state, ResourceGroup:resourceGroup, Image:containers[0].image, FQDN:ipAddress.fqdn, IP:ipAddress.ip}" `
    -o table

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✓ Status retrieved successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to retrieve status" -ForegroundColor Red
    exit 1
}
