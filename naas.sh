echo $(curl -s https://naas.isalman.dev/no | jq -r .reason | tee >(wl-copy))
