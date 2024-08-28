import subprocess

# Start the first script
process1 = subprocess.Popen(['python', 'main.py'])

# Start the second script
process2 = subprocess.Popen(['python', 'bot.py'])

# Wait for both scripts to finish
process1.wait()
process2.wait()
