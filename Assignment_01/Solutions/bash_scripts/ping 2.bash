#!/bin/bash
website=("amazon.com" "www.amazon.com" "www.jacobs-university.de" "moodle.jacobs-university.de")
function ping_IPV4() { websites=("$@")
   for i in "${websites[@]}";
      do
         echo "-----------------------------------------------------------------"
         echo $i
         ping "$i" -c 10
         echo -n
      done
}
ping_IPV4 "${website[@]}" > pingResults.txt
ping_IPV4 "${website[@]}" > pingResults.txt
