import argparse
import os
import subprocess

def start_server():
    command = "daphne -b 0.0.0.0 -p 8000 backend.asgi:application"

    env = os.environ.copy()
    env['DEBUG'] = '1'
    env['DATABASE_URL'] = 'postgres://jeunesse_db_user:ev1W2gjJEHBTW3eJQxHycUSWk7BmmCLi@dpg-cnk9ul0l6cac73a3gq9g-a.ohio-postgres.render.com/test_db'
    env['SECRET_KEY'] = 'dev_key'

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