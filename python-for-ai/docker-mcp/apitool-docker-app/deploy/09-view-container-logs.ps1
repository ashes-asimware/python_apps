# 09-view-container-logs.ps1
# View logs from the Azure Container Instance

$resourceGroup = "ashes-gm-002-rg"
$containerName = "imageapi-container"

Write-Host "Fetching logs for container: $containerName" -ForegroundColor Green

az container logs `
    --resource-group $resourceGroup `
    --name $containerName

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✓ Logs retrieved successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to retrieve logs" -ForegroundColor Red
    exit 1
}
