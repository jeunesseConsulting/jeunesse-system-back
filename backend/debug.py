import argparse
import os
import subprocess

def start_server():
    command = "daphne -b 0.0.0.0 -p 8000 backend.asgi:application"

    env = os.environ.copy()
    env['DEBUG'] = '1'

    subprocess.run(command, shell=True, env=env)

def main():
    parser = argparse.ArgumentParser(description="Development server")
    parser.add_argument("--start", action="store_true", help="Development server")

    args = parser.parse_args()

    if args.start:
        current_directory = os.getcwd()

        os.chdir(current_directory)

        start_server()
    else:
        print("Please, add the 'start' argument to launch the server")

if __name__ == "__main__":
    main()