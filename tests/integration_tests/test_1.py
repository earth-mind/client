import subprocess
import time

class Test1:
    def start_command(self, cmd):
        """Function to start a command using subprocess.Popen."""
        # Start the command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return process

    def test_numero(self):
        assert 1 == 1
        cmd1 = ["anvil", "-p", "8545"]
        cmd2 = ["anvil", "-p", "8546"]

        process1 = self.start_command(cmd1)
        process2 = self.start_command(cmd2)

        # time.sleep(10)  # Wait for 10 seconds

        # Example of how to check if processes are still running
        if process1.poll() is None:
            print("Command 1 is still running")
        else:
            print("Command 1 has finished")

        if process2.poll() is None:
            print("Command 2 is still running")
        else:
            print("Command 2 has finished")
            