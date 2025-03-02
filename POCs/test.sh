array=("/" "-" "\\" "|")  # Correct Bash array

for symbol in "${array[@]}"; do
    printf "\r%s " "$symbol"  # Print symbol with carriage return
    sleep 0.5
done
printf "\nDone!\n"  # Move to a new line after loop


num=0

clear

while true;
do
    printf "\r%s " "${array[${num}]}"
    num=$((num+1))
    num=$((num%4))
    sleep .5

done