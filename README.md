# randompass
______                _                  ______                                   _   _____                           _             
| ___ \              | |                 | ___ \                                 | | |  __ \                         | |            
| |_/ /__ _ _ __   __| | ___  _ __ ___   | |_/ /_ _ ___ _____      _____  _ __ __| | | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|    // _` | '_ \ / _` |/ _ \| '_ ` _ \  |  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |\ \ (_| | | | | (_| | (_) | | | | | | | | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_| \_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                                    
By Benjamin Burner                                                                                                                                   

About: random password generator. optimized for cryptographic keys.

Use:
there is two version of the program available. They are split up as the user version and command line version.

  User Version:
    The user version is plug and play. You run the file: python3 randompass_user.py
    The program will prompt you for bit length of desired password, format of generation, and weather youd like to save it to a .txt file.
    If you'd like to use the program for personal use and as simply as possible i recommend the user version.
    
  Command Line Version:
    The command line version may be prefered by some users as they are used to command line arguments while using a program.
    Although that use is valid the main reason for the creation of the command line version is for shell scripting.
    
    Use:
      
      -h : help menu
      -b : length of password in bytes (example: -b 36)
      -f : format of password. 1 for hex 2 for url safe passwords (url safe passwords include special chars and hex passwords do not)
      -s : saving password to a .txt file (example: -s password.txt)
      
For development help read the architecture doc.
