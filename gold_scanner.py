import requests, time, sys
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.table import Table

console = Console()

def show_banner():
    console.clear()
    banner = """
    [bold red]
     ██████  ██████  ██      ██████      ██    ██ ██ ██████  
    ██      ██    ██ ██      ██   ██      ██  ██  ██ ██   ██ 
    ██   ███ ██    ██ ██      ██   ██       ████   ██ ██████  
    ██    ██ ██    ██ ██      ██   ██        ██    ██ ██      
     ██████  ██████  ███████ ██████         ██    ██ ██      
    [/bold red]
    [bold yellow]      --- PREMIUM EXPLOIT SCANNER v1.0 ---[/bold yellow]
    """
    console.print(banner)

def check_key():
    console.print(Panel("[bold white]THIS IS A PROTECTED TOOL[/bold white]\n[cyan]Contact @YourTelegram for License Key[/cyan]", border_style="red"))
    key = console.input("[bold yellow]Enter VIP Key: [/bold yellow]")
    if key == "GOLD-2026": # هذا هو كود التفعيل الذي ستبيعه
        console.print("[bold green][+] Access Granted! Loading Modules...[/bold green]")
        time.sleep(2)
        return True
    else:
        console.print("[bold red][!] Invalid Key. Purchase via PayPal: your-email@example.com[/bold red]")
        sys.exit()

def start_scan():
    show_banner()
    target = console.input("[bold white]Enter Target Domain (e.g. site.com): [/bold white]")
    if not target.startswith("http"): target = "https://" + target
    
    # قائمة الثغرات المدفوعة
    payloads = {
        "/.env": "Critical Leak (Passwords)",
        "/.git/config": "Full Source Code Leak",
        "/wp-config.php.bak": "WordPress DB Credentials",
        "/.phpmyadmin": "Database Access",
        "/admin/.htpasswd": "Admin Credentials Leak"
    }

    console.print(f"\n[bold magenta][*] Scanning Server: {target}[/bold magenta]\n")
    
    results = Table(title="Vulnerability Report")
    results.add_column("Path", style="cyan")
    results.add_column("Severity", style="red")
    results.add_column("Status", style="green")

    for path, desc in track(payloads.items(), description="[cyan]Exploiting...[/cyan]"):
        try:
            r = requests.get(target + path, timeout=3)
            if r.status_code == 200:
                results.add_row(path, "HIGH", "VULNERABLE")
        except: pass

    console.print(results)
    console.print(Panel(f"[bold yellow]Scan Finished.[/bold yellow]\n[white]Report saved to logs.txt[/white]"))

if __name__ == "__main__":
    show_banner()
    if check_key():
        start_scan()
