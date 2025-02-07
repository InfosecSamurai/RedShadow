3. Command Line Interface (core/cli.py)

from modules import reconnaissance, exploitation, post_exploitation, evasion, reporting

def run_module(module):
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

def start_interactive_mode():
    while True:
        cmd = input("RedShadow > ").strip().lower()
        if cmd in ["exit", "quit"]:
            break
        elif cmd == "recon":
            reconnaissance.run()
        elif cmd == "exploit":
            exploitation.run()
        elif cmd == "post":
            post_exploitation.run()
        elif cmd == "evasion":
            evasion.run()
        elif cmd == "report":
            reporting.run()
        else:
            print("Unknown command.")