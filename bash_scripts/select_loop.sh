#! /bin/bash

# Select Loop example

select DRINK in tea coffee water juice soda all none
do
  case $DRINK in
    tea|coffee|water|all)
      echo "Go to canteen"
      ;;
    juice|soda)
      echo "Available at home"
      ;;
    none)
      break
      ;;
    *)
      echo "ERROR Invalid selection"
      ;;
  esac
done
