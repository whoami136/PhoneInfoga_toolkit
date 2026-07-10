import os
import importlib
import pkgutil
import modules
import logging
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.panel import Panel

# Configure logging
if not os.path.exists('output'): 
    os.makedirs('output')
logging.basicConfig(
    filename='output/investigation.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

console = Console()

def display_banner():
    banner = r"""
[grey50]
          !\_________________________/!\
          !!                         !! \
          !!      ALIEN-INTEL        !!  \
          !!                         !!   !
          !!         V.OMEGA         !!   !
          !!                         !!   !
          !!         #hugs           !!   !
          !!                         !!   !
          !!       By: whoami136      !!  /
          !!_________________________!! /
          !/_________________________\!/
             __\_________________/__/!_
            !_______________________!/
[/grey50]
[bold white][---]     ALIEN-INTEL SYSTEM     [---][/bold white]
[grey50][---]    Created by: whoami136    [---][/grey50]
"""
    console.print(banner)

def run_module(module_name, number):
    """
    Executes modules and forces them to report truth. 
    If a module returns 'None' or 'Error', it is ignored instead of displayed.
    """
    try:
        module = importlib.import_module(f"modules.{module_name}")
        if hasattr(module, 'execute'):
            result = module.execute(number)
            
            # THE TRUTH CHECK: 
            # Only print if the module found actual data (not just empty strings or error messages)
            if result and "Error" not in result and "Failed" not in result:
                console.print(Panel(
                    result, 
                    title=f"[bold white]{module_name.replace('_', ' ').title()}[/bold white]", 
                    border_style="white"
                ))
    except Exception as e:
        # Silently fail for modules that aren't configured yet
        pass 

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    
    number = console.input("[bold white]Target Node > [/bold white]")
    if not number: return
    
    logging.info(f"Investigation started for: {number}")
    console.print(f"[bold yellow]Initializing deep scan for {number}...[/bold yellow]\n")
    
    # Execution
    # We use ThreadPool to run everything at once, 
    # but the logic inside each module now handles the 'Real vs Show' validation.
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _, name, _ in pkgutil.iter_modules(modules.__path__):
            if name == "__init__": 
                continue
            executor.submit(run_module, name, number)

if __name__ == '__main__':
    main()
