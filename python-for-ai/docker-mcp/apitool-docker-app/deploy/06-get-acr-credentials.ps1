# 06-get-acr-credentials.ps1
# Retrieve Azure Container Registry credentials

$resourceGroup = "ashes-gm-002-rg"
$registryName = "imageapiregistry5536"

Write-Host "Retrieving ACR credentials..." -ForegroundColor Green

$acrUsername = az acr credential show `
    --name $registryName `
    --resource-group $resourceGroup `
    --query "username" `
    -o tsv

$acrPassword = az acr credential show `
    --name $registryName `
    --resource-group $resourceGroup `
    --query "passwords[0].value" `
    -o tsv

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ ACR credentials retrieved successfully" -ForegroundColor Green
    Write-Host "Username: $acrUsername" -ForegroundColor Cyan
    Write-Host "Password: $('*' * $acrPassword.Length)" -ForegroundColor Cyan
    
    # Export for use in other scripts
    $env:ACR_USERNAME = $acrUsername
    $env:ACR_PASSWORD = $acrPassword
    
    # Save to file for next script
    @{
        Username = $acrUsername
        Password = $acrPassword
    } | ConvertTo-Json | Out-File -FilePath "$PSScriptRoot\acr-credentials.json"
    
    Write-Host "Credentials saved to acr-credentials.json" -ForegroundColor Yellow
} else {
    Write-Host "✗ Failed to retrieve ACR credentials" -ForegroundColor Red
    exit 1
}
