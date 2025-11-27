# Azure Deployment Scripts

This folder contains PowerShell scripts to deploy the Image API application to Azure.

## Individual Scripts

1. **01-create-resource-group.ps1** - Creates the Azure Resource Group
2. **02-create-container-registry.ps1** - Creates Azure Container Registry (ACR)
3. **03-login-to-acr.ps1** - Authenticates with Azure Container Registry
4. **04-build-docker-image.ps1** - Builds the Docker image locally
5. **05-tag-and-push-image.ps1** - Tags and pushes image to ACR
6. **06-get-acr-credentials.ps1** - Retrieves ACR credentials
7. **07-create-container-instance.ps1** - Creates Azure Container Instance
8. **08-update-container-instance.ps1** - Updates existing container with new image
9. **09-view-container-logs.ps1** - Views container logs
10. **10-get-container-status.ps1** - Gets container status and information

## Master Scripts

### Full Deployment (First Time)

```powershell
.\deploy-all.ps1 -Version "v1"
```

Deploys everything from scratch including resource group, container registry, and container instance.

### Update Deployment (For Code Changes)

```powershell
.\update-deployment.ps1 -Version "v2"
```

Builds, pushes, and updates the container instance with a new version.

## Usage Examples

### Deploy from scratch:
```powershell
cd deploy
.\deploy-all.ps1 -Version "v1"
```

### Update with new code changes:
```powershell
cd deploy
.\update-deployment.ps1 -Version "v4"
```

### Run individual steps:
```powershell
# Build and push only
.\04-build-docker-image.ps1
.\05-tag-and-push-image.ps1 -Version "v5"

# Check status
.\10-get-container-status.ps1

# View logs
.\09-view-container-logs.ps1
```

## Configuration

Update these values in each script if needed:
- **Resource Group**: `ashes-gm-002-rg`
- **Container Registry**: `imageapiregistry5536`
- **Container Name**: `imageapi-container`
- **DNS Label**: `imageapi-app-6264`
- **Port**: `8443`
- **Location**: `eastus`

## Requirements

- Azure CLI installed and logged in (`az login`)
- Docker Desktop running
- PowerShell 7+ recommended
