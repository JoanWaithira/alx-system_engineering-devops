#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

domain_information() {
    local domain="$1"
    local subdomain="$2"
    local line
    line=$(dig "$subdomain"."$domain" | awk '/ANSWER SECTION:/ {getline; print; getline; print}')
    echo "$subdomain $line" | awk '{printf "The subdomain %s is a %s record and points to %s\n", $1, $2, $3}'
}

if [ "$#" -eq 1 ]; then
    domain_information "$1" "www"
    domain_information "$1" "lb-01"
    domain_information "$1" "web-01"
    domain_information "$1" "web-02"
elif [ "$#" -eq 2 ]; then
    domain_information "$1" "$2"
fi

