# Cookie Clicker Bot 1.0!

Play with Python + Selenium until you can *make* ALL OF THE COOKIES! With a single command!

# Setup
1. [Python][1] 
    * [pyenv][2]
        - [Install pyenv][3] (Python Version Manager)
            + Note: For Windows, recommend [pyenv-win][9]
        - Install Python
            + `pyenv install [version in .python-version]` example: `pyenv install 3.11.0b4`
            + `pyenv local [version in .python-version]` example: `pyenv local 3.11.0b4`
2. [make][4]
    * Windows ([chocolatey][5]): `choco install make -y`
    * Mac ([homebrew][6]): `brew install make`
3. [ChromeDriver][7]
    * `make EnsureChromeDriver`
4. Python packages
    * `make Restore`

# Run
* `make` or `make run` or `python CookieClickerBot.py`

# Guide
* The game itself... [Steam Guide][8]
* Bot keybinds: while game is running, press "h"

```
                                    ?JYPPPPGPPPP5PPPP5YJ?
                               7JY5555PPPPPP5PPPPPPGPPPPPPPPPPPP5Y?
                         !?J5PPPPPPPPPP5PP55PP5P55PPPP55PPP5PPPPGGP5J?7
                    !!7?YPGGPPPPPPPPPPPGG55PP5Y5555P5P5555555555PPPGGGGP5J!
                    ?5PGGGPPP55PPPGP5PGG5YYYYYYYYYY5YPP55555555555PP5P55PPPJ!
                 !?5GGPPPG5PPPP555PGBGGGGGGPPP5555555P555YJYYY55555P555Y5PGGPY7
               !?YPPPP555PPP555YYYYYPBBGGGGGGGGGGB555JYP55YYJJY5555555Y55PGPPGG57
             !J5PP555555555PP55JYYYYY5G#BBBGGGGGGBGYYYYP5P5YYJJYYYYYYYYY55GP5PGGG57
            7PPPPPPPP5P555PPP5YJYYYYYY55PGBBB#BBGG5YJJJJY55YYJJJYYJJYYYYYY5PP5PPPGPJ
           7PGPP5555PP5GYPP55YYYYYYYY55YJYYY555YYJJJ??JYJYPY5JYYYYYJJYYYY55YY55PPPGGY~
          !5GGPP5YY5PPPPPPPYYYYYYY5YYYYJY5YYYYJJYYJJ???JJYYY5555YYYYYYYYJY55Y55P5PPPGY~
          JGGPPPP5P555555YYYYJJJJYYYYYJYJPPPYYJYJJJ??????J?JY5YPP5YYYY55YYYJYY555PPGPGJ~
         YGGPPP5PPP5P5YYYYYYYJJJJJJJY55Y5GGGGG5J?????777???JY5PGGG5Y5PGGGGPYYJPPPPPGGGP?~
        YGPPPPP5PG555YJYYYJYYJJJJ?5GGGBBGGGGGGGGJ!77!7!7??JJJJYYPGPGGPPPGGB5YYP5555PPPGGJ~
       ?GGPGGPP55PP5YYYYYJJJJJJ?J?GBGGGGPGGGGGGGB57!!7777?????J5GG55P55PPGB5JYYPPPPPPPPPP7
       PGGGGGPPPPP55YYYYJJJJJJJ?JPBBGGPPPPGGGGGGGBGY7!7!777??7?5GGP5PPPPGBBGYYYYPP5PPPPPGJ
      YGPPPPPPPP555YYYYYJJJJ????JBBBGGPGGGGGGBBBGBBB?!!7777?77?JBBBBBBBBBBBBGP55PP555PPPGP7
      5GPPPPPPP55YYYYJJ????JJ??JBBGGGGGGGGGGGBBBBB#G?7???????JJ?PG55YJJY5555P5555P555PPPPGY
      5GPPPPPPPPGPY5YJJJJJ???J?JGBBBBBBGBBBBGGB##P5JJJ?755JJ?J55J77??????J?JJJYYY55555PPPP5
      5GPPPPPP555P55JYJJ5J???????YPGB##BBBBB#BGY?!!!7777J?77?YGJ77????J??JJJJYYY555555PPPG5
     !YGGPPPPP5555YYYJYJYJ?777777777J5PGBBBBPJ!!!!!777?7!7777?J77????JJJJJJJJYY5555555PPPG5
     !YGGGPPPPP555YYJJ55JYJ??777!!777?7?????7?777!!777!!!7???????77??JJJYYYYY5555PPPPPPPPGP
      !7PGGPPPPP5555YYYYYJYJ??7?7!!7777??????7??77!!!77!!77?J???J??7??JYPPGG55PPPPPPPGGGGGGJ
      !YGGGPPPP555YYYYJJJJ??????JJ7???J??Y????7?77777?77!7777?5??JYYJ5PPGBG5PP55PPPPGGPGG5
      !JGPGPPPPPP5YYYJYJJJ?????PGGP5??7?7YY??????7?????77????JY55PPPPGGBB#BYY555PPPPPPPGG?
       ?GPPPPPP55YYYYYYYYYJJJJPBBBBBBP?7?55JYYJ???JJ??J???????YGBBGGB##BP5BYYY555PPPPPGG5
        YGPP5P55555555Y55YYYYYBBBBPY??JJJ5GGYJJJJJJJYYYJYYYJJYGGPGGGGP5Y55P5P555PPPPGGGP?
         YGPPPY5Y555555YYYYYYYY55J?JJ5PPGPGG5YYYJJYGPP5555YJYP5JYYY55555555YYY55PPPPGGGJ
          5GPP5555555Y555YYY555PPPPBBBGGGGGGGGG5YYGBGPPGGGGPP5YYYYYY5GY5Y55555555PPPGGJ
          7YGGGGGGGPPPP5555PBBBBBBBBBBBBBBBB#PJYY5BBBPGGGGGGGYYYYYYYY55555PP5PPPPPGGGY
           JPBGGGGGGGPPP555GBBBB###BBBB###BPJYYY5BBBBBBBGGGGPYJYYYYYYY5555PPPGPGGGPJ
            7?YGGGGGPGGGPP55Y5PGGBBP555Y5G#PYYYYY5#BBBBBBBBB#BYYJYYYYYY5555PPPGGGG5?
             7?J5GGGGGPPPPPPP5P5555555555PG5YYYYYYPBB#BBB#BGG5YYYYY5555555PPPPGGG5?
                ?J5GGGGGGGPPP555555555555PP55555YY55P55Y5PG5JYYY555PPP5PPPGGGGG5J
                  ?J5GGGGGGGPPPP555555PP5PGPPP555555555555G5Y55555P5PGGGGGGBG5YJ
                    ?J5PGGGGGGPPPPPPPPPPPPPPPPPPP555555555G5555P55PPGGBGGGP5YJ
                      ?JY5PGGGGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGBGGPP5YJ
                         JJYPPGGBGGGGGGGGGGGPPPPPPPPPPPPPGPGGGGGGGBGPP5YJ
                           ?JYY5PGGGGGBBGGBBGGGGGGGGGBBBBBBBBGGGGP55YJ
                               JJYY55PPPPGGGGGGBBBBBBGGGGGGPPP

      $$$$$$\ $$\           $$$$$$$\                      $$\                                            
      \_$$  _|$$ |          $$  __$$\                     \__|                                           
        $$ |$$$$$$\         $$ |  $$ | $$$$$$\   $$$$$$\  $$\ $$$$$$$\   $$$$$$$\                        
        $$ |\_$$  _|        $$$$$$$\ |$$  __$$\ $$  __$$\ $$ |$$  __$$\ $$  _____|                       
        $$ |  $$ |          $$  __$$\ $$$$$$$$ |$$ /  $$ |$$ |$$ |  $$ |\$$$$$$\                         
        $$ |  $$ |$$\       $$ |  $$ |$$   ____|$$ |  $$ |$$ |$$ |  $$ | \____$$\                        
      $$$$$$\ \$$$$  |      $$$$$$$  |\$$$$$$$\ \$$$$$$$ |$$ |$$ |  $$ |$$$$$$$  |$$\ $$\ $$\            
      \______| \____/       \_______/  \_______| \____$$ |\__|\__|  \__|\_______/ \__|\__|\__|           
                                                $$\   $$ |                                               
                                                \$$$$$$  |                                               
                                                \______/                                                
                          $$$$$$\                                     $$\                               
                          $$  __$$\                                    $$ |                              
                          $$ /  \__| $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$$ |$$$$$$\$$$$\   $$$$$$\        
                  $$$$$$\ $$ |$$$$\ $$  __$$\ \____$$\ $$  __$$\ $$  __$$ |$$  _$$  _$$\  \____$$\       
                  \______|$$ |\_$$ |$$ |  \__|$$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |      
                          $$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |      
                          \$$$$$$  |$$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |      
                          \______/ \__|      \_______|\__|  \__| \_______|\__| \__| \__| \_______|      
```
[1]: <https://www.python.org/>
[2]: <https://github.com/pyenv/pyenv#simple-python-version-management-pyenv>
[3]: <https://github.com/pyenv/pyenv#installation>
[4]: <https://www.gnu.org/software/make/>
[5]: <https://chocolatey.org/install#install-step2>
[6]: <https://brew.sh/>
[7]: <https://chromedriver.chromium.org/>
[8]: <https://steamcommunity.com/sharedfiles/filedetails/?id=2591407770>
[9]: <https://github.com/pyenv-win/pyenv-win#quick-start>