export MASTODON_ACCESS_TOKEN='kA4w2QtTJ3at17O9paoMF7dk1mZ9mWcM0DLGpKeauuw'
export URL='https://aus.social/api/v1'
# Test access 
curl --header "Authorization: Bearer ${MASTODON_ACCESS_TOKEN=}" \
     -XGET \
     -vvv \
  	 "${URL}/accounts/verify_credentials" | jq
