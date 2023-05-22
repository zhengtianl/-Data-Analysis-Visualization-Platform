#!/bin/bash

OLD_EMAIL='starkfkworld@ravpn-266-1-student-10-8-43-73.uniaccess.unimelb.edu.au'
CORRECT_NAME='zhengtianl'
CORRECT_EMAIL='458078290@qq.com'

git filter-branch -f --env-filter "
if [ \"\$GIT_COMMITTER_EMAIL\" = \"\$OLD_EMAIL\" ]
then
    if [ -z \"\$GIT_COMMITTER_NAME\" ]
    then
        export GIT_COMMITTER_NAME=\"\$CORRECT_NAME\"
    fi
    if [ -z \"\$GIT_COMMITTER_EMAIL\" ]
    then
        export GIT_COMMITTER_EMAIL=\"\$CORRECT_EMAIL\"
    fi
fi
if [ \"\$GIT_AUTHOR_EMAIL\" = \"\$OLD_EMAIL\" ]
then
    if [ -z \"\$GIT_AUTHOR_NAME\" ]
    then
        export GIT_AUTHOR_NAME=\"\$CORRECT_NAME\"
    fi
    if [ -z \"\$GIT_AUTHOR_EMAIL\" ]
    then
        export GIT_AUTHOR_EMAIL=\"\$CORRECT_EMAIL\"
    fi
fi
" --tag-name-filter cat -- --branches --tags
