import argparse
import subprocess
import sys


class DockerManager:
    """
    The class provides simple commands that hide the complexity of Docker commands
    """
    def __init__(self, tag_name):
        self.name = "api-automation"
        self.image = f"dev/{self.name}"
        self.local_options = f"-v $(pwd):/opt/{self.name} -e PYTHONPATH=\"/opt/{self.name}\""
        self.tag_name = self._format_tags(tag_name) if tag_name else ''

    @staticmethod
    def _format_tags(tag_input):
        """
        Handles single tag or comma-separated multiple tags.
        """
        if ',' in tag_input:
            tags = tag_input.split(',')
            tags = [f'@{tag}' if not tag.startswith('@') else tag for tag in tags]
            return f'-t {",".join(tags)}'
        else:
            if not tag_input.startswith('@'):
                return f'-t @{tag_input}'
            return f'-t {tag_input}'

    @staticmethod
    def run_command(command):
        """
        Executes a shell command and checks for errors.
        """
        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}", file=sys.stderr)
            sys.exit(e.returncode)

    def build(self):
        """
        Builds the Docker image.
        """
        print(f"--> Building {self.name}")
        self.run_command(f"docker build -t {self.image} .")

    def stop(self):
        """
        Stops the Docker container.
        """
        print(f"--> Stopping {self.name}")
        self.run_command(f"docker kill {self.name} || true")

    def start(self):
        """
        Starts the Docker container.
        """
        print(f"--> Starting {self.name}")
        self.run_command(f"docker start {self.name}")

    def rm_container(self):
        """
        Removes the Docker container.
        """
        print(f"--> Removing container {self.name}")
        self.run_command(f"docker rm -f {self.name} || true")

    def local_dev(self):
        """
        Runs the Docker container with local development settings.
        """
        print(f"--> Starting {self.name} with local development settings")
        self.run_command(f"docker run {self.local_options} --name {self.name} --env-file .env -it {self.image} /bin/bash")

    def test(self):
        """
        Runs tests inside the Docker container.
        """
        print(f"--> Running tests in {self.name}")
        self.run_command(f"docker run {self.local_options} --name {self.name} --env-file .env {self.image} "
                         f"behave {self.tag_name} --no-skipped --format=pretty "
                         )

    def dev(self):
        """
        Sets up the environment for local development.
        """
        self.stop()
        self.rm_container()
        self.build()
        self.local_dev()

    def run_tests(self):
        """
        Executes tests by rebuilding and running tests.
        """
        self.stop()
        self.rm_container()
        self.build()
        self.test()


def main():
    """
    Main function to parse command-line arguments and execute corresponding functions using argparse.
    """
    parser = argparse.ArgumentParser(description='Docker container management script.')
    parser.add_argument('command', help='The command to execute (dev, run_tests)')
    parser.add_argument('--tag_name', help='Tag name(s) to run specific tests. Use comma for multiple tags.')

    args = parser.parse_args()

    manager = DockerManager(tag_name=args.tag_name)

    commands = {
        "dev": manager.dev,
        "run_tests": manager.run_tests,
    }

    if args.command in commands:
        commands[args.command]()
    else:
        print(f"Invalid command: {args.command}")
        print("Valid commands are:", ", ".join(commands.keys()))
        sys.exit(1)


if __name__ == "__main__":
    main()
