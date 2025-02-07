import argparse
from core import cli

def main():
    parser = argparse.ArgumentParser(description="RedShadow - Ethical Hacking & Red Teaming Toolkit")
    parser.add_argument("-m", "--module", help="Specify the module to run", choices=["recon", "exploit", "post", "evasion", "report"])
    args = parser.parse_args()
    
    if args.module:
        cli.run_module(args.module)
    else:
        cli.start_interactive_mode()

if __name__ == "__main__":
    main()