LOGIN_URL=http://localhost:8765/energy/api/login/
YOUR_USER='use14'
YOUR_PASS='jack12345'
COOKIES=cookies.txt
CURL_BIN="curl -c $COOKIES -b $COOKIES -e $LOGIN_URL"

echo -n "Django Auth: get csrftoken ..."
$CURL_BIN $LOGIN_URL > /dev/null
DJANGO_TOKEN="csrfmiddlewaretoken=$(grep csrftoken $COOKIES | sed 's/^.*csrftoken\s*//')"

echo -n " perform login ..."
$CURL_BIN \
    -d "$DJANGO_TOKEN&username=$YOUR_USER&password=$YOUR_PASS" \
    -X POST $LOGIN_URL

#echo -n " do something while logged in ..."
#$CURL_BIN -d "$DJANGO_TOKEN&..." -X GET http://localhost:8765/energy/api/admin/users/admin

#echo " logout"
#rm $COOKIES
