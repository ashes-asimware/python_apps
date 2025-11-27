# deploy-all.ps1
# Master script to deploy the entire solution from scratch

param(
    [Parameter(Mandatory=$false)]
    [string]$Version = "v1",
    
    [Parameter(Mandatory=$false)]
    [switch]$SkipResourceGroup = $false
)

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Image API - Full Azure Deployment" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to deploy directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

try {
    # Step 1: Create Resource Group
    if (-not $SkipResourceGroup) {
        Write-Host "`n[1/9] Creating Resource Group..." -ForegroundColor Yellow
        & .\01-create-resource-group.ps1
        if ($LASTEXITCODE -ne 0) { throw "Resource Group creation failed" }
    } else {
        Write-Host "`n[1/9] Skipping Resource Group creation" -ForegroundColor Yellow
    }

    # Step 2: Create Container Registry
    Write-Host "`n[2/9] Creating Container Registry..." -ForegroundColor Yellow
    & "$scriptPath\02-create-container-registry.ps1"
    if ($LASTEXITCODE -ne 0) { throw "Container Registry creation failed" }

    # Step 3: Login to ACR
    Write-Host "`n[3/9] Logging in to Container Registry..." -ForegroundColor Yellow
    & "$scriptPath\03-login-to-acr.ps1"
    if ($LASTEXITCODE -ne 0) { throw "ACR login failed" }

    # Step 4: Build Docker Image
    Write-Host "`n[4/9] Building Docker Image..." -ForegroundColor Yellow
    & "$scriptPath\04-build-docker-image.ps1"
    if ($LASTEXITCODE -ne 0) { throw "Docker build failed" }

    # Return to deploy directory after build
    Set-Location $scriptPath

    # Step 5: Tag and Push Image
    Write-Host "`n[5/9] Tagging and Pushing Image..." -ForegroundColor Yellow
    & "$scriptPath\05-tag-and-push-image.ps1" -Version $Version
    if ($LASTEXITCODE -ne 0) { throw "Image push failed" }

    # Step 6: Get ACR Credentials
    Write-Host "`n[6/9] Retrieving ACR Credentials..." -ForegroundColor Yellow
    & "$scriptPath\06-get-acr-credentials.ps1"
    if ($LASTEXITCODE -ne 0) { throw "Failed to get ACR credentials" }

    # Step 7: Create Container Instance
    Write-Host "`n[7/9] Creating Container Instance..." -ForegroundColor Yellow
    & "$scriptPath\07-create-container-instance.ps1" -Version $Version
    if ($LASTEXITCODE -ne 0) { throw "Container Instance creation failed" }

    # Step 8: Wait for container to start
    Write-Host "`n[8/9] Waiting for container to start..." -ForegroundColor Yellow
    Start-Sleep -Seconds 10

    # Step 9: Get Container Status
    Write-Host "`n[9/9] Checking Container Status..." -ForegroundColor Yellow
    & "$scriptPath\10-get-container-status.ps1"

    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "  ✓ Deployment Completed Successfully!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "`nYour API is available at:" -ForegroundColor Cyan
    Write-Host "https://imageapi-app-6264.eastus.azurecontainer.io:8443" -ForegroundColor White
    Write-Host "`nAPI Documentation:" -ForegroundColor Cyan
    Write-Host "https://imageapi-app-6264.eastus.azurecontainer.io:8443/docs" -ForegroundColor White

} catch {
    Write-Host "`n========================================" -ForegroundColor Red
    Write-Host "  ✗ Deployment Failed!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
}
