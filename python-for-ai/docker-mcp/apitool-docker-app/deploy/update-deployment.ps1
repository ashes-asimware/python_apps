# update-deployment.ps1
# Quick update script for pushing new changes to Azure

param(
    [Parameter(Mandatory=$false)]
    [string]$Version = "latest"
)

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Image API - Update Deployment" -ForegroundColor Cyan
Write-Host "  Version: $Version" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to deploy directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

try {
    # Step 1: Login to ACR
    Write-Host "[1/5] Logging in to Container Registry..." -ForegroundColor Yellow
    & "$scriptPath\03-login-to-acr.ps1"
    if ($LASTEXITCODE -ne 0) { throw "ACR login failed" }

    # Step 2: Build Docker Image
    Write-Host "`n[2/5] Building Docker Image..." -ForegroundColor Yellow
    & "$scriptPath\04-build-docker-image.ps1"
    if ($LASTEXITCODE -ne 0) { throw "Docker build failed" }

    # Return to deploy directory after build
    Set-Location $scriptPath

    # Step 3: Tag and Push Image
    Write-Host "`n[3/5] Tagging and Pushing Image..." -ForegroundColor Yellow
    & "$scriptPath\05-tag-and-push-image.ps1" -Version $Version
    if ($LASTEXITCODE -ne 0) { throw "Image push failed" }

    # Step 4: Update Container Instance
    Write-Host "`n[4/5] Updating Container Instance..." -ForegroundColor Yellow
    & "$scriptPath\08-update-container-instance.ps1" -Version $Version
    if ($LASTEXITCODE -ne 0) { throw "Container update failed" }

    # Step 5: Get Container Status
    Write-Host "`n[5/5] Checking Container Status..." -ForegroundColor Yellow
    Start-Sleep -Seconds 5
    & "$scriptPath\10-get-container-status.ps1"

    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "  ✓ Update Completed Successfully!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "`nVersion: $Version" -ForegroundColor Cyan
    Write-Host "API URL: https://imageapi-app-6264.eastus.azurecontainer.io:8443" -ForegroundColor White

} catch {
    Write-Host "`n========================================" -ForegroundColor Red
    Write-Host "  ✗ Update Failed!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
}
