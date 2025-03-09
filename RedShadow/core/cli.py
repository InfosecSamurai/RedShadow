from modules import reconnaissance, exploitation, post_exploitation, evasion, reporting
import logging
import sys

# Configure logging
logging.basicConfig(filename="cli.log", level=logging.INFO)

def run_module(module):
    """Run the specified module."""
    logging.info(f"Attempting to run module: {module}")
    try:
        if module == "recon":
            reconnaissance.run()
        elif module == "exploit":
            exploitation.run()
        elif module == "post":
            post_exploitation.run()
        elif module == "evasion":
            evasion.run()
        elif module == "report":
            reporting.run()
        else:
            print("Invalid module. Use -h for help.")
            logging.warning(f"Invalid module requested: {module}")
    except Exception as e:
        print(f"Error running module {module}: {e}")
        logging.error(f"Error running module {module}: {e}")

def start_interactive_mode():
    """Start the interactive CLI mode."""
    logging.info("Starting interactive mode...")
    print("RedShadow - Interactive Mode")
    print("Available commands: recon, exploit, post, evasion, report, exit")

    while True:
        cmd = input("RedShadow > ").strip().lower()
        
        if cmd in ["exit", "quit"]:
            print("Exiting interactive mode...")
            logging.info("Exiting interactive mode.")
            break
        elif cmd in ["recon", "exploit", "post", "evasion", "report"]:
            run_module(cmd)
        else:
            print("Unknown command. Available commands: recon, exploit, post, evasion, report, exit")
            logging.warning(f"Unknown command entered: {cmd}")

def show_help():
    """Display the help menu."""
    print("RedShadow - Command-Line Interface")
    print("Usage: python3 redshadow.py -m <module>")
    print("Available modules: recon, exploit, post, evasion, report")
    print("Interactive mode: python3 redshadow.py")

if __name__ == "__main__":
    logging.info("RedShadow CLI started.")

    if len(sys.argv) > 1:
        if sys.argv[1] == "-m":
            if len(sys.argv) > 2:
                run_module(sys.argv[2])
            else:
                print("Error: No module specified. Use -h for help.")
                logging.error("No module specified with -m flag.")
        elif sys.argv[1] == "-h":
            show_help()
        else:
            print("Unknown argument. Use -h for help.")
            logging.warning(f"Unknown argument: {sys.argv[1]}")
    else:
        start_interactive_mode()