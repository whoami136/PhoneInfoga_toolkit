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
          !!      By: whoami136      !!  /
          !!_________________________!! /
          !/_________________________\!/
              __\_________________/__/!_
             !_______________________!/
[/grey50]
[bold white][---]     ALIEN-INTEL SYSTEM      [---][/bold white]
[grey50][---]    Created by: whoami136    [---][/grey50]
"""
    console.print(banner)

def run_module(module_name, number):
    try:
        module = importlib.import_module(f"modules.{module_name}")
        if hasattr(module, 'execute'):
            result = module.execute(number)
            if result and isinstance(result, str) and result.strip():
                # Theme: White/Grey Panel
                console.print(Panel(
                    result, 
                    title=f"[bold white]{module_name.replace('_', ' ').title()}[/bold white]", 
                    border_style="white"
                ))
    except Exception:
        pass 

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    display_banner()
    
    # Input
    number = console.input("[bold white]Target Node > [/bold white]")
    logging.info(f"Investigation started for: {number}")
    
    # Execution
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _, name, _ in pkgutil.iter_modules(modules.__path__):
            if name == "__init__": 
                continue
            executor.submit(run_module, name, number)

if __name__ == '__main__':
    main()
