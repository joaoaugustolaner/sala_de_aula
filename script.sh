#!/usr/bin/env bash

SRC_DIR=$HOME/sala_de_aula/src

mkdir $SRC_DIR
echo "Diretório: $SRC_DIR criado"
sleep .5

touch .gitignore aviso.txt

echo "aviso.txt" > .gitignore
echo "Arquivos criados!"
sleep .5

echo "Obrigado por usar o script :)"



