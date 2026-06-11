# ============================================================================
# CQECMPLX Kernel Full Deployment Script (Windows PowerShell)
# ============================================================================
# One-command launcher for entire hierarchical kernel + OpenCode CLI
#
# Usage:
#   .\deploy-kernel.ps1                  # Deploy everything
#   .\deploy-kernel.ps1 -FullValidate    # Deploy + validate papers
#   .\deploy-kernel.ps1 -Logs            # Deploy + watch logs
#   .\deploy-kernel.ps1 -Stop            # Stop all services
#
# ============================================================================

param(
    [switch]$FullValidate,
    [switch]$Logs,
    [switch]$Stop,
    [switch]$Help
)

$ErrorActionPreference = "Stop"

# =====================================================================
# Configuration
# =====================================================================

$KernelDir = (Get-Item $PSScriptRoot).FullName
$ComposeFile = "docker-compose-kernel-with-opencode.yml"
$LogDir = "$env:TEMP\cqecmplx-logs"
$Timestamp = Get-Date -Format "yyyyMMdd-HHmmss"

# Colors
$Colors = @{
    "Info"    = "Cyan"
    "Success" = "Green"
    "Warning" = "Yellow"
    "Error"   = "Red"
}

# =====================================================================
# Helper Functions
# =====================================================================

function Write-Log {
    param(
        [string]$Message,
        [string]$Level = "Info"
    )
    
    $color = $Colors[$Level]
    $prefix = switch ($Level) {
        "Success" { "[✓]" }
        "Error"   { "[ERROR]" }
        "Warning" { "[WARN]" }
        default   { "[INFO]" }
    }
    
    Write-Host "$prefix $Message" -ForegroundColor $color
}

function New-Directories {
    Write-Log "Creating directories..."
    
    @($LogDir, "$KernelDir\scripts", "$KernelDir\data") | ForEach-Object {
        if (-not (Test-Path $_)) {
            New-Item -ItemType Directory -Path $_ -Force | Out-Null
        }
    }
    
    Write-Log "Directories created" -Level "Success"
}

function Test-Docker {
    Write-Log "Checking Docker installation..."
    
    try {
        $null = docker ps 2>$null
        Write-Log "Docker is available" -Level "Success"
        return $true
    }
    catch {
        Write-Log "Docker not found or not running" -Level "Error"
        return $false
    }
}

function Test-ComposeFile {
    Write-Log "Checking compose file..."
    
    $composePath = "$KernelDir\$ComposeFile"
    if (-not (Test-Path $composePath)) {
        Write-Log "Compose file not found: $ComposeFile" -Level "Error"
        return $false
    }
    
    Write-Log "Compose file found" -Level "Success"
    return $true
}

function Stop-ExistingServices {
    Write-Log "Checking for existing services..."
    
    $existing = docker ps 2>$null | Select-String "cqecmplx" | Measure-Object | Select-Object -ExpandProperty Count
    
    if ($existing -gt 0) {
        Write-Log "Found existing services. Stopping..." -Level "Warning"
        Push-Location $KernelDir
        try {
            docker-compose -f $ComposeFile down 2>$null | Out-Null
        }
        finally {
            Pop-Location
        }
        Start-Sleep -Seconds 2
        Write-Log "Existing services stopped" -Level "Success"
    }
    else {
        Write-Log "No existing services found"
    }
}

function Start-Services {
    Write-Log "Starting Docker services..."
    
    Push-Location $KernelDir
    try {
        $output = docker-compose -f $ComposeFile up -d 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Log "Failed to start services: $output" -Level "Error"
            return $false
        }
    }
    finally {
        Pop-Location
    }
    
    Write-Log "Services started" -Level "Success"
    Start-Sleep -Seconds 3
    return $true
}

function Verify-Services {
    Write-Log "Verifying services..."
    
    $services = @(
        "cqecmplx-proof-kernel",
        "cqecmplx-opencode-cli",
        "cqecmplx-docker-provider"
    )
    
    $running = 0
    foreach ($service in $services) {
        if (docker ps 2>$null | Select-String $service) {
            $running++
        }
    }
    
    if ($running -eq $services.Count) {
        Write-Log "All services running" -Level "Success"
        return $true
    }
    else {
        Write-Log "Some services failed to start" -Level "Error"
        return $false
    }
}

function Wait-ForKernel {
    Write-Log "Waiting for kernel to be ready..."
    
    $maxAttempts = 30
    $attempt = 1
    
    while ($attempt -le $maxAttempts) {
        try {
            $null = docker exec cqecmplx-proof-kernel curl -s http://localhost:8765/health 2>$null
            Write-Log "Kernel is ready" -Level "Success"
            return $true
        }
        catch {
            Write-Host -NoNewline "`r  Attempt $attempt/$maxAttempts...     "
            Start-Sleep -Seconds 2
            $attempt++
        }
    }
    
    Write-Log "Kernel took longer than expected to start. Continuing..." -Level "Warning"
    return $true
}

function Show-Status {
    Write-Log "Current service status:`n"
    
    docker ps 2>$null | Select-String "cqecmplx" | ForEach-Object {
        $line = $_ -split '\s+'
        Write-Host "  • $($line[-1]) -> $($line[0]) ($($line[-2]))" -ForegroundColor Cyan
    }
}

function Show-Dashboard {
    Clear-Host
    
    Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║   CQECMPLX Hierarchical Kernel - Deployment Complete            ║" -ForegroundColor Cyan
    Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan
    
    Write-Host "✓ Services Running:" -ForegroundColor Green
    docker ps 2>$null | Select-String "cqecmplx" | ForEach-Object {
        $line = $_ -split '\s+'
        Write-Host "  • $($line[-1]) ($($line[-2]))" -ForegroundColor Green
    }
    
    Write-Host "`n✓ Kernel Status:" -ForegroundColor Green
    try {
        $status = docker exec cqecmplx-proof-kernel curl -s http://localhost:8765/health 2>$null
        Write-Host "  Kernel responding" -ForegroundColor Green
    }
    catch {
        Write-Host "  Status unavailable" -ForegroundColor Yellow
    }
    
    Write-Host "`nQuick Commands:" -ForegroundColor Cyan
    Write-Host "  # Access OpenCode terminal:" -ForegroundColor White
    Write-Host "    docker exec -it cqecmplx-opencode-cli python3 /opt/opencode/cli-startup.sh" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  # Run validation:" -ForegroundColor White
    Write-Host "    docker exec -i cqecmplx-opencode-cli python3 << 'EOF'" -ForegroundColor Gray
    Write-Host "    import requests" -ForegroundColor Gray
    Write-Host "    requests.post('http://proof-kernel:8765/api/validate'," -ForegroundColor Gray
    Write-Host "        json={'papers': ['CQE-paper-00'], 'token_string': 'ATCGATCG'}).json()" -ForegroundColor Gray
    Write-Host "    EOF" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  # Monitor hierarchy:" -ForegroundColor White
    Write-Host "    docker ps -a | Select-String 'paper-validator'" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  # View logs:" -ForegroundColor White
    Write-Host "    docker logs -f cqecmplx-proof-kernel" -ForegroundColor Gray
    Write-Host "    docker logs -f cqecmplx-opencode-cli" -ForegroundColor Gray
    Write-Host ""
    Write-Host "API Endpoints:" -ForegroundColor Cyan
    Write-Host "  • Proof Kernel:   http://localhost:8765" -ForegroundColor White
    Write-Host "  • OpenCode CLI:   http://localhost:8766" -ForegroundColor White
    Write-Host ""
}

function Invoke-FullValidation {
    Write-Log "Running paper validation..."
    
    docker exec -i cqecmplx-opencode-cli python3 @"
import requests, json

endpoint = "http://proof-kernel:8765"

try:
    result = requests.post(
        f"{endpoint}/api/validate",
        json={
            "papers": ["CQE-paper-00", "CQE-paper-01"],
            "token_string": "ATCGATCGATCGATCGATCG"
        },
        timeout=300
    ).json()
    
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"Error: {e}")
"@
}

function Show-Help {
    Write-Host @"
Usage: .\deploy-kernel.ps1 [options]

Options:
  (no option)      Deploy all services
  -FullValidate    Deploy + validate papers
  -Logs            Deploy + watch kernel logs
  -Stop            Stop all services
  -Help            Show this help

Examples:
  .\deploy-kernel.ps1                    # Basic deployment
  .\deploy-kernel.ps1 -FullValidate      # Deploy + validate
  .\deploy-kernel.ps1 -Logs              # Deploy + watch logs
  .\deploy-kernel.ps1 -Stop              # Stop services

"@ -ForegroundColor Cyan
}

# =====================================================================
# Main Execution
# =====================================================================

function Main {
    Write-Host ""
    Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║   CQECMPLX Hierarchical Kernel - Full Deployment             ║" -ForegroundColor Cyan
    Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
    
    # Pre-flight checks
    Write-Log "Running pre-flight checks..."
    if (-not (Test-Docker)) { exit 1 }
    if (-not (Test-ComposeFile)) { exit 1 }
    New-Directories
    Write-Host ""
    
    # Setup
    Write-Log "Setting up environment..."
    Stop-ExistingServices
    Write-Host ""
    
    # Deploy
    Write-Log "Deploying services..."
    if (-not (Start-Services)) { exit 1 }
    if (-not (Verify-Services)) { exit 1 }
    Wait-ForKernel
    Write-Host ""
    
    # Show results
    Show-Status
    Show-Dashboard
    
    # Handle options
    if ($FullValidate) {
        Write-Host ""
        Invoke-FullValidation
    }
    elseif ($Logs) {
        Write-Host ""
        Write-Log "Watching kernel logs (Ctrl+C to exit)..."
        docker logs -f cqecmplx-proof-kernel
    }
}

# =====================================================================
# Entry Point
# =====================================================================

if ($Help) {
    Show-Help
}
elseif ($Stop) {
    Write-Log "Stopping services..."
    Push-Location $KernelDir
    try {
        docker-compose -f $ComposeFile down 2>$null
    }
    finally {
        Pop-Location
    }
    Write-Log "Services stopped" -Level "Success"
}
else {
    Main
}
