def sleep_in(weekday, vacation):
    if vacation or not weekday:
      return True
    else:
      return False

# Test Cases:
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

print(sleep_in(False, True))