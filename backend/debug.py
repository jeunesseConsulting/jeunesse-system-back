import argparse
import os
import subprocess
import time

def start_server():
    command = "daphne -b 0.0.0.0 -p 8000 backend.asgi:application"

    env = os.environ.copy()
    env['DEBUG'] = '1'
    env['DATABASE_URL'] = 'postgres://jeunesse_db_user:ev1W2gjJEHBTW3eJQxHycUSWk7BmmCLi@dpg-cnk9ul0l6cac73a3gq9g-a.ohio-postgres.render.com/test_db'
    env['SECRET_KEY'] = 'dev_key'

    subprocess.run(command, shell=True, env=env)

def migrate_test():
    first_command = "python manage.py makemigrations"
    second_command = "python manage.py migrate"

    env = os.environ.copy()
    env['DEBUG'] = '1'
    env['DATABASE_URL'] = 'postgres://jeunesse_db_user:ev1W2gjJEHBTW3eJQxHycUSWk7BmmCLi@dpg-cnk9ul0l6cac73a3gq9g-a.ohio-postgres.render.com/test_db'
    env['SECRET_KEY'] = 'dev_key'

    first_script = subprocess.Popen(first_command, shell=True, env=env)
    time.sleep(20)
    first_script.terminate()

    second_script = subprocess.Popen(second_command, shell=True, env=env)
    time.sleep(20)
    second_script.terminate()


def main():
    parser = argparse.ArgumentParser(description="Development server")
    parser.add_argument("--start", action="store_true", help="Development server")
    parser.add_argument("--migrate-test", action="store_true", help="Migrate test database")

    args = parser.parse_args()

    if args.start:
        current_directory = os.getcwd()

        os.chdir(current_directory)

        start_server()

    if args.migrate_test:
        current_directory = os.getcwd()

        os.chdir(current_directory)

        migrate_test()


if __name__ == "__main__":
    main()