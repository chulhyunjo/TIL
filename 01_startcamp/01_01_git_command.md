## Git 명령어 한눈에 정리



### 1. basic

```bash
# 작성자 이름, 메일 등록(최초 1번만 실행)
git config --global user.name "github username"
git config --global user.email "github email"

# config 정보 출력
git config --global --list

# 일반 폴더 -> 로컬 저장소
git init

# 버전 상태 출력
git status

# Working Directory -> Staging Area
git add [File]
git add . # 모든 파일 add

# Staging Area -> Commits
git commit -m "메세지"

# commits 목록 출력
git log
git log --oneline # 한줄로 보기 옵션
git log -p # 커밋마다 차이 보기 옵션
```



### 2.remote

```bash
# 로컬 저장소와 원격 저장소를 연결
git remote add origin [Github repository URL]

# 연결된 원격 저장소 목록 조회
git remote -v

# 원격 저장소 연결 삭제
git remote rm origin
git remote remove origin

# 로컬 저장소의 commits을 원격 저장소에 반영
git push origin master
git push -u origin master

# 원격 저장소를 로컬에 복제
git clone [Github repository URL]

# 원격 저장소의 변경 사항 로컬에 받아오기 (동기화)
git pull origin master
```



### 3. reset, revert

```bash
# 특정 커밋 상태로 되돌리기(soft, mixed, hard 세 가지 옵션)
git reset --soft [commit ID]
git reset --mixed [commit ID]
git reset --hard [commit ID]

# 커밋을 취소하는 커밋을 새로 생성하여 특정 커밋을 되돌리기
git revert [commit ID]

# 이전 커밋 목록 모두 출력
git reflog
```



### 4. branch, merge

```bash
	# 브랜치 목록 확인
	git branch
	
	# 새 브랜치 생성
	git branch [brand name]
	
	# 특정 브랜치 삭제
	git branch -d [branch name]
	git branch -D [branch name] # 강제 삭제(병합되지 않은 브랜치도 삭제)
	
	git switch [brand name] # 다른 브랜치로 이동
	git switch -c [brand name] # 브랜치를 생성함과 동시에 이동
	
	# 한 줄로, 모든 브랜치의, 그래프를 포함하여 커밋 목록 출력
	git log --oneline --all --graph
	
	# 브랜치 병합
	git merge [branch name]

```