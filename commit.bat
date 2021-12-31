ECHO Start
git add .


IF %1.==. GOTO NoCommittxt
set arg1=%1
git commit -a -m %arg1%

GOTO End1

:NoCommittxt
  git commit -a -m "Buff Update"
GOTO End1
:End1
git push
ECHO Pushed
