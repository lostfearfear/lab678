#!/bin/bash


create_new_branch() {
    git checkout -b $1
}

add_commit_push() {
    git add $1
    git commit -m "$2"
    git push origin $3
}

merge_branch() {
    git checkout $1
    git merge $2
}

show_current_date() {
    date
}

create_gitignore() {
    echo "*.log" > .gitignore
}

create_log_files() {
    local num=${1:-100} 
    for ((i=1; i<=$num; i++)); do
        echo "Log file $i" > log$i.txt
        echo "Log file $i was created by script.sh on $(date)" >> log$i.txt
    done
}

show_help() {
    echo "Available options:"
    echo "--date: Show today's date"
    echo "--create-gitignore: Create .gitignore file to ignore files containing 'log' in their names"
    echo "--logs [num]: Create log files, optionally specifying the number of files (default is 100)"
    echo "--help: Show this help message"
}

create_tag() {
    git tag v1.0
}

case "$1" in
    "--date")
        show_current_date
        ;;
    "--create-gitignore")
        create_gitignore
        ;;
    "--logs")
        create_log_files $2
        ;;
    "--help")
        show_help
        ;;
    *)
        echo "Unknown option: $1. Use --help to see available options."
        exit 1
        ;;
