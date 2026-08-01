# 03-login-to-acr.ps1
# Login to Azure Container Registry

$registryName = "imageapiregistry5536"

Write-Host "Logging in to Azure Container Registry: $registryName" -ForegroundColor Green

az acr login --name $registryName

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Successfully logged in to ACR" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to login to ACR" -ForegroundColor Red
    exit 1
}
