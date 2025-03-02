import time

def countdown(seconds):
  """
  Generates a countdown timer.

  Args:
    seconds: The number of seconds to countdown from.
  """

  try:
    seconds = int(seconds)  # Ensure seconds is an integer
    if seconds < 0:
      print("Please enter a positive number of seconds.")
      return

    while seconds > 0:
      mins, secs = divmod(seconds, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r")  # Use '\r' to overwrite the same line
      time.sleep(1)
      seconds -= 1

    print("Countdown finished!")

  except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  try:
    user_input = input("Enter the countdown time in seconds: ")
    countdown(user_input)
  except KeyboardInterrupt:
    print("\nCountdown interrupted.")