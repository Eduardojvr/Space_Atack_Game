# .
echo
cls 
clear
echo "#######################################"
echo "Instalação de dependências necessárias"
echo "#######################################"
echo 
echo "[1] MAC"
echo "[2] Linux"
read op

if [ $op == 1 ];
then
  echo "MAC"
  pip install pygame
  brew install hg sdl sdl_image sdl_ttf
  brew install sdl_mixer portmidi
elif [ $op == 2 ];
then
  echo "Linux"
  sudo apt-get install python3-dev mercurial 
  sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev 
fi
 
 
 
 
 
 
