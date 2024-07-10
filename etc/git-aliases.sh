#!/bin/bash

###### edits
export PATH="/c/Users/N537866/mine/python/python311:/c/Users/N537866/mine/python/python311/Scripts:/cygdrive/c/ezj/bin:$PATH"
#HADOOP_HOME
export HADOOP_HOME="/c/ezj/spark-3.3.3-bin-hadoop3"
export SPARK_HOME="/c/ezj/spark-3.3.3-bin-hadoop3"
export PYSPARK_PYTHON="python"
export JAVA_HOME="/c/ezj/jdk-21.0.1"
export JDK_HOME="/c/ezj/jdk-21.0.1"
export PATH="/c/Python311:/c/Python311/Scripts:/c/ezj/bin:$JAVA_HOME/bin:$SPARK_HOME/bin:$PATH"

###### edits
# export PATH="/cygdrive/c/Python311:/cygdrive/c/Python311/Scripts:/cygdrive/c/ezj/bin:$PATH"
#HADOOP_HOME
#SPARK_HOME
export SPARK_HOME="/c/ezj/spark-3.3.3-bin-hadoop3"
export PYSPARK_PYTHON="python"
#JDK_HOME
#export JAVA_HOME="/c/ezj/jdk-21.0.1"
export JDK_HOME="/c/ezj/jdk-21.0.1"
export PATH="/c/Python311:/c/Python311/Scripts:/c/ezj/bin:$JAVA_HOME/bin:$SPARK_HOME/bin:$PATH"

alias ll='ls -al'
######

alias aws='/cygdrive/c/ezj/awscli/Amazon/AWSCLIV2/aws'
alias .ggp='git gc --prune=now'

# devel
# grs() {
# }
.grebase-skip-all() {
	# if [ "$1" == "" ] || [ "$2" == "" ]; then
	# 	echo "usage: <branch-ref> <branch-base>"
	# else
	# 	gitk --all --select-commit=`git merge-base $1 $2` &
	# fi
	for i in `seq 1 $1`; 
	do 
		git rebase --skip;
	done
	''
}

.grebase-all-from-to() {
	mbranches=$2 # '<name of branches space separated>'
	for i in `echo $mbranches`;
	do 
		git rebase $1 $i;
		.grebase-skip-all;
	done
}
.gpush-all() {
	mbranches=$1 # '<name of branches space separated>'
	for i in `echo $mbranches`; 
	do 
		# .gpush-all;
		.gch $i
		push -f
	done
}
alias .greb='git rebase'

# git aliases
#alias g="git" # just a git alias
alias .gis="git status" # show status
alias .gb="git branch -vv --color | less -SR"; alias gb=".gb" # list branches
alias .gba="git branch -a -vv --color | less -SR"; alias gba=".gba" # list branches
alias .gib="git branch -v " # list branches
alias .gch="git checkout" # switch to branch
alias .gch="git checkout"; alias gch=".gch" # switch to branch
alias .gici="git -a -m " # switch commit
alias .gidb="git -a -m " # delete branch
alias .gswitch="git remote set-url origin " # svn switch equivalent
alias .gch="git checkout -m " # switch merge to given branch
alias .gchp="git checkout -m - " # switch merge to previous branch
alias .gx="git checkout -m " # switch merge to given branch

alias sc='scrapy'

# source: http://stackoverflow.com/questions/2255416/how-to-determine-when-a-git-branch-was-created
.gmerge-base-gitk-all() {
	if [ "$1" == "" ] || [ "$2" == "" ]; then
		echo "usage: <branch-ref> <branch-base>"
	else
		gitk --all --select-commit=`git merge-base $1 $2` &
	fi
}

alias .gpush="git push"
# .gpush() {
# 	currentBranch="`git branch | grep '\*' | cut -d':' -f3 | cut -c 3-`"
#         echo "currentBranch: $currentBranch"
# 	echo "Pushing to branch $currentBranch.."
# 	if [ "$1" == "-f" ]; then
# 		goption="$1"
# 	else
# 		goption=""
# 	fi
# 	if [  "$2" != "" ]; then
# 		remotes="$2"
# 	else
# 		remotes=""
# 	fi
# 	for i in `echo $remotes`; do
# 		echo "git push $goption $i" #2> /dev/null
# 		git push $goption $i $currentBranch:$currentBranch #2> /dev/null
# 		git push $goption --tags $i 2> /dev/null
# 	done
# 	#git push $goption origin $currentBranch:$currentBranch
# 	#git push $goption --tags origin
# }
# .gpull() {
# 	currentBranch="`git branch | grep '\*' | cut -d':' -f3 | cut -c 3-`"
# 	echo "Pulling from branch $currentBranch.."
# 	git pull origin $currentBranch
# }
alias .gpull="git pull"
.gpulli() {
	git stash && .gpull && git stash pop stash@{0}
}

.gfetch-setUpstreamTo() {
    if [ "$1" == "" ] || [ "$2" == "" ] || [ "$3" == "" ]; then
        echo "usage: <remote> <branch> <upstream>"
    else
        git fetch $1 $2:$2
        git branch --set-upstream-to=$3 $2
    fi
}

.gsweepPullPush() {
	nsleep=0
		if [ "$1" == "" ]; then
			echo ".gsweepPullPush <remote>"
		else
			gremote="$1"
        for i in `git branch | cut -c 3-`; do
		echo '';
		echo "== git checkout $i =============================================================";
		#git checkout $i;
		sleep $nsleep;
		echo "-- git pull $gremote $i:$i -----------------------------------------------------------";
		#.gpull;
		#git pull $gremote $i:$i
		sleep $nsleep;
		echo "-- git push $gremote $i:$i -----------------------------------------------------------";
		#.gpush;
		git push $gremote $i:$i
		sleep $nsleep;
		done
		fi
}

.grebaseWaterfall() {
	if [ "$1" == "" ] || [ "$2" == "" ]; then
		echo "usage: <from to>"
	else
		for i in `git branch | grep "$2" | xargs echo`; do

			echo "=========="
			echo ""
			echo -n "git rebase $1 $i; ? (y/n): "
			ans=""
			read ans
			if [ "$ans" == "y" ]; then
				echo "rebasing: git rebase $1 $i"
				git rebase $1 $i;
			fi

			echo "----------"
			echo ""
			echo -n "git push $i; ? (y/n): "
			ans=""
			read ans
			if [ "$ans" == "y" ]; then
				echo "pushing $i"
				.gpush

				echo ""
				echo -n "git push -f $i; [FORCE] ? (y/n): "
				ans=""
				read ans
				if [ "$ans" == "y" ]; then
					echo "force pushing $i"
					.gpush -f
				fi

			fi
		done
	fi
}

alias .gstl="git stash list "
.gstshow() {
	for x in `git stash list | cut -d'{' -f2 | cut -d'}' -f1`; do
		git stash show -p stash@{$x}; echo '';
	done
}
alias gsl='.gstl'
alias gss='.gstshow'

gbranchset-upstream-to() {
	if [ "$1" == "" ]; then
		echo "usage: <remote>"
	else
		for i in `git branch`; do
			git branch --set-upstream-to=$1/$i $i 2> /dev/null;
			#echo "git branch --set-upstream-to=$1/$i $i;"
		done
	fi
}

gbranchclean() {
	if [ "$1" == "" ]; then
		echo "usage: <remote>"
	else
	gbranchset-upstream-to $1
	for i in `git branch -vv | grep -v ahead | grep -v behind | grep "$1" | cut -d' ' -f3`; do
		git branch -D $i;
		echo $i;
	done
	fi
}

alias sedGit2Perforce="sed -e 's/git/perforce/g'"
#alias sg2p="sedGit2Perforce"
alias sg2p="grep -v git | perl -pe 's/^.*?:\d+://g'"

alias .gib="git init --bare | sg2p"
alias .gi="git init | sg2p"
alias .gstat="git status | sg2p"
alias .gstatl="git status | sg2p | less -SR"
alias .gd="git diff --color | sg2p"
alias .gds="git diff --staged --color | sg2p"
alias .gdd=".gd; .gds | sg2p"
alias .gdb="git diff --color "
alias .gdl="git diff --color | less -SR"
alias .gdsl="git diff --staged --color | less -SR"
alias .ga="git add | sg2p"
alias .gam="git am --show-current-patch"
# source: http://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git
gcolor="--color=always"
gformat="$gcolor --format=format:'%C(bold blue)%h%C(reset) :: %C(red)%p%C(reset) : %C(green)%t%C(reset) - %an%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %C(auto)%d%C(reset)'"
gformat2="$gcolor --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''           %an%C(reset) - %C(white)%s%C(reset) %C(dim white)'"
#alias .gl=" git log --all --decorate --graph $gformat | sg2p | less"
alias .gl="  git log --decorate --graph $gformat --numstat --parents"
alias .glf=".gl | grep -i '|' | grep '/' | head -n 17 "
alias .glp=" git log --decorate --graph $gformat --parents -p"
alias .glpat=".glp | egrep '::|@' | less -SRi"
alias .glo=" git log --decorate --graph --oneline --parents $gformat"
alias .glo2=" git log --decorate --graph --oneline --parents $gformat2"
alias .glon="git log --all --decorate --oneline $gformat --parents --numstat"
alias .gla=" git log --all --decorate --graph $gformat | sg2p | less -SR"
alias gl=".gl"
alias gla=".gl --all"
alias glp=".glp"
alias glpa=".glp --all"
alias glo=".glo"
alias gloa=".glo --all"
alias glo2=".glo2"
alias glo2a=".glo2 --all"
alias lo=".glo | less -SRi"
alias loa="gloa"; alias llo="loa | less -SRi";
alias lo2=".glo2"
alias lo2a="glo2a"
alias lor2=".glor2"
alias .gdepgraph='git log --oneline --decorate --simplify-by-decoration --graph --color' # git branch dependency graph
alias .gdepgraph-all='.gdepgraph --all | less -SRi' # git branch dependency graph
alias .gdep='.gdepgraph | less -SRi'
alias .gdep-all='.gdepgraph --all | less -SRi'
alias .gdept='.gdepgraph --tags | less -SRi'
alias .gdept-all='.gdepgraph --all | less -SRi'
alias .gcontainsbranch='git branch --contains ' # <branch name>
watch-llo() {
	watch -n3 -c ' git log --decorate --graph --oneline --parents --format=format:'\''%C(bolde)%h%C(reset) :: %C(red)%p%C(reset) : %C(green)%t%C(reset) - %an%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %C(auto)%d%C(reset)'\'''
}
watch-llo-all() {
	watch -n3 -c ' git log --decorate --graph --oneline --parents --format=format:'\''%C(bolde)%h%C(reset) :: %C(red)%p%C(reset) : %C(green)%t%C(reset) - %an%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %C(auto)%d%C(reset)'\'' --all '
}
# https://stackoverflow.com/questions/89332/how-to-recover-a-dropped-stash-in-git
#alias lod="lo $(git fsck --no-reflog | awk '/dangling commit/ {print $3}')"

# list git tag annotation messages
alias .gt="git tag -ln99 | less -SRi"
# fetch and push remote tags
alias .gtpull="git fetch origin --tags"
alias .gtpush="git push origin --tags"
alias .gci=".gb && sleep 0 && git commit -m "
alias .gcini="git commit -m "
alias .ga="git add -i "; alias ga=".ga "
alias .grh="git reset --hard "
alias .grs="git reset --soft "
.grhi() {
  if [ "$1" == "" ]; then
        echo "usage: <git hash>"
  else
	git stash && git reset --hard $1 && git stash pop stash@{0}
  fi
}

alias .gri="git rebase -i "
alias .gr="git remote -v" # list remotes
# quick git rebase -i HEAD~n method
.gfb() {
	if [ "$1" == "" ] || [ "$2" == "" ]; then
	echo "usage: <remote> <branch>"
	else
	git stash
	git checkout -m -
	git fetch $1 $2:$2
	git checkout -m -
	git stash pop stash@{0}
	fi
}
grind() {
	if [ "$1" == "" ]; then
	echo "usage: <number of commuits>"
	else
	#git rebase -i HEAD~$1
	#git rebase -i -v HEAD~$1
	git rebase -i --stat HEAD~$1
	fi
}
alias .grind="grind "
alias .gfetch="git fetch origin"
alias push="git push"
alias pull="git pull"
alias .gra="git commit --amend"
alias .grc="git rebase --continue"
alias .grsk="git rebase --skip"
alias .grab="git rebase --abort"
alias gitc='git checkout -m '
alias c='gitc '
alias .gc="git commit "
alias .gca="git commit --amend"
alias .gcp="git cherry-pick "
alias .gitchildren='../lib/git/git-heads/seschwar_git-heads.github.py.git/git-heads --remote --tags --decorate --oneline --parents -n 10'
.gcpbatch() {
	for i in `echo "$@"`; do
		#echo $i;
		git log --oneline -n 1 $i
		#ans=`read 'ansss'`
		echo -n "cherry-pick $i? (y/n): "
                read ans
                echo "res: $ans"
		if [ "$ans" == "y" ]; then
			.gcp $i
		fi
	done
}

alias .gacpush='.ga && .gc && .gpush'

# source: http://stackoverflow.com/questions/21168846/cant-remove-file-from-git-commit
#alias .g-remove-from-commit="git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch FOLDERNAME" -- --all "

# source: http://stackoverflow.com/questions/12399002/how-to-configure-git-bash-command-line-completion
# In my Ubuntu 14.04 this file is /usr/share/bash-completion/completions/git . /etc/bash_completion.d/git-prompt is used for git prompt support, not for completion
#echo 'bash completions'
#source /usr/share/bash-completion/completions/git

# alias git to g [with bash completion]
# source: http://askubuntu.com/questions/62095/how-to-alias-git-to-g-so-that-bash-completion-rules-are-preserved
#echo 'alias git to g'
complete -o bashdefault -o default -o nospace -F _git g 2>/dev/null || complete -o default -o nospace -F _git g
#complete -o bashdefault -o default -o nospace -F git g 2>/dev/null || complete -o default -o nospace -F git g
#alias g='git'
#source /usr/share/bash-completion/completions/git

# https://gist.github.com/alexeds/3641372
gshdir="git-stash-patches"
git-stash-patches() {
	mkdir git-stash-patches;
	git stash list  > $gshdir/git-stash-list.txt
	for i in `git stash list | cut -d':' -f1`;
	do
		git stash show stash@{0} -p > $gshdir/stash-$i;
	done
}

git-stash-apply-patches() {
	#cd gshdir

	git apply $gshdir/$i
	git stash
}

gitrebasetag() {
	if [ "$1" == "" ] || [ "$2" == "" ]; then
		echo "usage: <upstream> <branch>"
	else
		git rebase $1 $2
		git tag -f $2
	fi
}
alias .grt='gitrebasetag'

.gupdate() {
    if [ "$1" == "" ] || [ "$2" == "" ] || [ "$3" == "" ]; then
        echo "usage: <downstream tag> <remote> <branch>"
    else
	read -p "stash/unstash WiP? (y/[n s]): " ans
	qgitdiff="`git diff`"
	if [ "${ans}" == "y" ] && [ "${qgitdiff}" != "" ]; then
		git stash
	fi
	nsleep=2
	.gb; lo; .ga; .gc; .grind 15; git tag $1 -f; git push $2 $3:$3 --tags -f; sleep $nsleep; lo
	if [ "${ans}" == "y" ] && [ "${qgitdiff}" != "" ]; then
		git stash pop stash@{0}
	fi
    fi
}

.gdangling-commits() {
	git fsck --lost-found > tmp/dangling-commits_fsck--lost-found.log
	for i in `cat tmp/dangling-commits_fsck--lost-found.log | grep -i commit | cut -d' ' -f3`;
	do
		git log --oneline $i > tmp/dangling/$i.log; echo $i;
	done
}

.grebase-quick() {
	git rebase $1 $2;
	git tag -f $2;
}

gitStashExport() {
	if [ "$1" == "" ] || [ "$2" == "" ]; then
		echo "usage: <to directory> <label>"
	else
		exportHdir="$1"
		label="$2"
		mkdir -p $exportHdir
		for i in `git stash list | perl -pe 's/\ /_/g'`; do
			num="`echo $i | perl -pe 's/.*\{([\d]+)\}.*/\1/g'`";
			echo $num;
			git stash show -p stash@{$num} > "`echo "$exportHdir/${label}_$i"`.txt";
		done
	fi
}
