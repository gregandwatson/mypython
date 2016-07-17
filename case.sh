#!/bin/bash

#!/bin/bash
printf 'Which host would you like to connect to?\n'
printf '1) Puppet Master\n'
printf '2) Puppet Agent\n'
printf '3) File server\n'

read SSH_HOST

case $SSH_HOST in
     1)
          ssh root@192.168.1.183
          ;;
     2)
          ssh root@192.168.1.182
          ;;
     3)
          ssh 192.168.1.156
          ;; 
     *)
          echo 'That is not a valid choice'
          ;;
esac
