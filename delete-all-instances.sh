nova list --all-tenant| cut -f2 -d'|' | grep  -E "[0-9|a-z]" | sed s/[[:space:]]//g |parallel "echo 'deleting {}';nova delete {}"
