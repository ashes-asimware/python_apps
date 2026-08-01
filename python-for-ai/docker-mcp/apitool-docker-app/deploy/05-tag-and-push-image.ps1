# 05-tag-and-push-image.ps1
# Tag and push Docker image to Azure Container Registry

param(
    [Parameter(Mandatory=$false)]
    [string]$Version = "latest"
)

$registryName = "imageapiregistry5536"
$imageName = "imageapi"
$localImage = "apitool-docker-app-imageapi:latest"
$remoteImage = "$registryName.azurecr.io/${imageName}:${Version}"

Write-Host "Tagging image: $localImage -> $remoteImage" -ForegroundColor Green

docker tag $localImage $remoteImage

if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Failed to tag image" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Image tagged successfully" -ForegroundColor Green
Write-Host "Pushing image to Azure Container Registry..." -ForegroundColor Green

docker push $remoteImage

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Image pushed successfully" -ForegroundColor Green
    Write-Host "Image: $remoteImage" -ForegroundColor Cyan
} else {
    Write-Host "✗ Failed to push image" -ForegroundColor Red
    exit 1
}
