import os

print("""
---------------------------------------------------
Linux & Docker Menu Tool - Centralized Command Runner
---------------------------------------------------
""")

ssh_needed_commands = set(range(1, 36)) | set(range(39, 57))
docker_commands = set(range(57, 64))

# Ask SSH credentials once
username = input("Enter your Linux username (or press Enter to skip SSH commands): ")
remote_ip = ""
if username:
    remote_ip = input("Enter your Linux machine IP address: ")

while True:
    print("""
    1. date                   2. cal                3. ifconfig
    4. ls                     5. pwd                6. rm
    7. rmdir                  8. mkdir              9. touch
   10. rm -rf               11. gedit             12. vi
   13. echo                 14. cd                15. cd ..
   16. cat                  17. df                18. ping
   19. yum repolist         20. yum install httpd
   21. rpm -q httpd         22. whoami            23. history
   24. rmdir --help         25. ssh-keygen -t rsa 26. open id_rsa.pub (Windows)
   27. open pp.py (Windows) 28. open menu.html (Windows)
   29. head file.txt        30. head -n 2 file.txt
   31. grep 2 file.txt      32. start httpd       33. status httpd
   34. stop firewalld       35. install pywhatkit
   36. import pywhatkit     37. send WhatsApp msg (instantly)
   38. send Group msg       39. install streamlit
   40. import streamlit     41. import os         42. run app.py (streamlit)
   43. su - user            44. echo to file      45. exit
   46. install httpd (sudo) 47. remove httpd      48. ls -l
   49. chmod                50. chgrp             51. usermod -G
   52. usermod -g           53. pip install       54. import
   55. print                56. ssh root@         57. Docker run
   58. Docker start         59. Docker stop       60. Docker attach
   61. Docker remove        62. Docker images     63. Docker ps -a
   64. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "64":
        print("Exiting... Goodbye!")
        break

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    def run_ssh_command(cmd):
        os.system(f"ssh {username}@{remote_ip} {cmd}")

    # Linux SSH commands
    if choice in ssh_needed_commands:
        if not username or not remote_ip:
            print("SSH credentials required. Restart and enter them first.")
            continue

    if choice == 1:
        run_ssh_command("date")
    elif choice == 2:
        run_ssh_command("cal")
    elif choice == 3:
        run_ssh_command("ifconfig")
    elif choice == 4:
        run_ssh_command("ls")
    elif choice == 5:
        run_ssh_command("pwd")
    elif choice == 6:
        run_ssh_command("rm")
    elif choice == 7:
        run_ssh_command("rmdir")
    elif choice == 8:
        run_ssh_command("mkdir")
    elif choice == 9:
        run_ssh_command("touch")
    elif choice == 10:
        run_ssh_command("rm -rf")
    elif choice == 11:
        run_ssh_command("gedit")
    elif choice == 12:
        run_ssh_command("vi")
    elif choice == 13:
        run_ssh_command("echo")
    elif choice == 14:
        run_ssh_command("cd")
    elif choice == 15:
        run_ssh_command("cd ..")
    elif choice == 16:
        run_ssh_command("cat")
    elif choice == 17:
        run_ssh_command("df")
    elif choice == 18:
        run_ssh_command("ping google.com")
    elif choice == 19:
        run_ssh_command("yum repolist")
    elif choice == 20:
        run_ssh_command("yum install httpd")
    elif choice == 21:
        run_ssh_command("rpm -q httpd")
    elif choice == 22:
        run_ssh_command("whoami")
    elif choice == 23:
        run_ssh_command("history")
    elif choice == 24:
        run_ssh_command("rmdir --help")
    elif choice == 25:
        run_ssh_command("ssh-keygen -t rsa")
    elif choice == 29:
        run_ssh_command("head file.txt")
    elif choice == 30:
        run_ssh_command("head -n 2 file.txt")
    elif choice == 31:
        run_ssh_command("grep 2 file.txt")
    elif choice == 32:
        run_ssh_command("systemctl start httpd")
    elif choice == 33:
        run_ssh_command("systemctl status httpd")
    elif choice == 34:
        run_ssh_command("systemctl stop firewalld")
    elif choice == 35:
        run_ssh_command("pip install pywhatkit")
    elif choice == 36:
        run_ssh_command("python3 -c 'import pywhatkit'")
    elif choice == 39:
        run_ssh_command("pip install streamlit")
    elif choice == 40:
        run_ssh_command("python3 -c 'import streamlit'")
    elif choice == 41:
        run_ssh_command("python3 -c 'import os'")
    elif choice == 42:
        run_ssh_command("streamlit run app.py")
    elif choice == 43:
        run_ssh_command("su - user")
    elif choice == 44:
        run_ssh_command("echo \"hello\" >> file.txt")
    elif choice == 45:
        run_ssh_command("exit")
    elif choice == 46:
        run_ssh_command("sudo yum install httpd")
    elif choice == 47:
        run_ssh_command("sudo yum remove httpd")
    elif choice == 48:
        run_ssh_command("ls -l")
    elif choice == 49:
        run_ssh_command("chmod 755 file.txt")
    elif choice == 50:
        run_ssh_command("chgrp users file.txt")
    elif choice == 51:
        run_ssh_command("usermod -G group user")
    elif choice == 52:
        run_ssh_command("usermod -g group user")
    elif choice == 53:
        run_ssh_command("pip install package")
    elif choice == 54:
        run_ssh_command("python3 -c 'import module'")
    elif choice == 55:
        run_ssh_command("python3 -c 'print(\"Hello\")'")
    elif choice == 56:
        run_ssh_command("ssh root@localhost")

    # Windows-based commands
    elif choice == 26:
        os.system("notepad id_rsa.pub")
    elif choice == 27:
        os.system("notepad pp.py")
    elif choice == 28:
        os.system("notepad menu.html")
    elif choice == 37:
        phone = input("Enter phone number with +91: ")
        msg = input("Enter message: ")
        os.system(f"python -c \"import pywhatkit; pywhatkit.sendwhatmsg_instantly('{phone}', '{msg}')\"")
    elif choice == 38:
        os.system("python -c \"import pywhatkit; pywhatkit.sendwhatmsg_to_group_instantly('team 38', 'hello')\"")

    # Docker commands (via SSH)
    elif choice == 57:
        name = input("Enter container name: ")
        image = input("Enter image name: ")
        run_ssh_command(f"docker run -dit --name {name} {image}")
    elif choice == 58:
        name = input("Enter container name: ")
        run_ssh_command(f"docker start {name}")
    elif choice == 59:
        name = input("Enter container name: ")
        run_ssh_command(f"docker stop {name}")
    elif choice == 60:
        name = input("Enter container name: ")
        run_ssh_command(f"docker attach {name}")
    elif choice == 61:
        name = input("Enter container name: ")
        run_ssh_command(f"docker rm {name}")
    elif choice == 62:
        run_ssh_command("docker images")
    elif choice == 63:
        run_ssh_command("docker ps -a")

    else:
        print("Invalid option. Please choose from the list above.")