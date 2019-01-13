sonar-scanner \
-Dsonar.login=`read -p Username: u; echo $u` \
-Dsonar.password=`read -s -p Password: p; echo $p` 
