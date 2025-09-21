#!/bin/bash
read -p "enter year: " year
read -p "enter day: " day 

FILE="./$year/day$day.py"
DIRECTORY="./$year" 

if [ -d $DIRECTORY ]; then
  echo "Directory '$DIRECTORY' exists."
else
  echo "Directory '$DIRECTORY' does not exist. Creating directory..."
  mkdir "$DIRECTORY"
fi


if [ -f "$FILE" ]; then
  echo "File '$FILE' template exists."
else
  echo "File '$FILE' template does not exists. Creating template file..."
  echo "def main():" >>  $FILE
  echo "    with open('./inputs/$year/day$day.txt') as f:" >> $FILE
  echo "        lines = f.readlines()" >> $FILE
  echo "        print(lines)" >> $FILE
  echo "" >> $FILE
  echo "if __name__ == '__main__':" >> $FILE
  echo "    main()" >> $FILE
fi
