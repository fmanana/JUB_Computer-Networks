#!/bin/bash

website=("amazon.com" "www.amazon.com" "www.jacobs-university.de" "moodle.jacobs-university.de")

function mtr() {
   websites=("$@")
   for i in "${websites[@]}";
      do
         echo "-----------------------------------------------------------------"
         echo $i
         sudo mtr -4 -z --report "$i"
         echo -n
      done
}


mtr "${website[@]}" > mtrResults.txt
