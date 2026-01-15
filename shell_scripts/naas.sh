# Pulls a rejection reason from the No As A Service (NAAS) API and pastes it to the terminal & clipboard
echo $(curl -s https://naas.isalman.dev/no | jq -r .reason | tee >(wl-copy))
