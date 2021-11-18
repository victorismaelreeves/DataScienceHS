function polo(){
    next=$(cat /tmp/missing/marcoDirectory.txt)
    echo "Changing directory to $next"
    cd "$next"
}
