git filter-branch -f --env-filter "

OLD_EMAIL='starkfkworld@ravpn-266-1-student-10-8-43-73.uniaccess.unimelb.edu.au'
CORRECT_NAME='zhengtianl'
CORRECT_EMAIL='starkfkworld@ravpn-266-1-student-10-8-43-73.uniaccess.unimelb.edu.au'

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
" --tag-name-filter cat -- --branches --tags
