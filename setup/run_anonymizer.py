from asyncio.windows_events import NULL
import os, sys
import subprocess


# ensuring PWD is in anonymizer folder in git bash window for scripts to run properly
print('Opening and running Anonymizer application')

if os.path.exists("C:/Users/Remote/anonymizer/"):
    
    os.chdir("C:/Users/Remote/anonymizer/")
    print('-------> Changed to correct directory...')
    anon_env = 'C:/Users/Remote/Desktop/setup/venv-anon.sh'
    conda_env = 'C:/Users/Remote/Desktop/setup/venv-conda.sh'
    print('-------> Starting anonymization...')

    git_bash = subprocess.Popen('"C:/Program Files/Git/bin/bash.exe" --login', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_anon = subprocess.Popen('C:/Users/Remote/Desktop/setup/run.sh', shell=True, stdin=git_bash.stdout)
    run_anon.wait()
    
    out, err = run_anon.communicate()
    if (os.path.getsize('C:/Users/Remote/anonymizer/out') > 0 or NULL):
        print('''
        
          Anonymized images!

            ▒▒▒▒▒▒▒▒▒▒▒▒
            ▒▒▒▒▓▒▒▓▒▒▒▒
            ▒▒▒▒▓▒▒▓▒▒▒▒
            ▒▒▒▒▒▒▒▒▒▒▒▒
            ▒▓▒▒▒▒▒▒▒▒▓▒
            ▒▒▓▓▓▓▓▓▓▓▒▒
            ▒▒▒▒▒▒▒▒▒▒▒▒
            
    Have a great rest of day/night
        ''')
    else:
        print('OH NO! Looks like there was an error writing your files...')

else:
    print('ERROR: Folders not read properly --> Setup failed')

sys.exit(0)
