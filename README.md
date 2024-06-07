medias
    Photo
        - 이미지 파일 url 로 저장 (클라우드 flare)
        - 이미지 설명 description
        - 갤러리 (pk gallery)
    Video
        - 영상 파일 url 로 저장 (클라우드 flare)
        - 영상 설명 description
        - 갤러리 (pk gallery)
---
reviews
    - 리뷰 작성자 (pk users)
    - 리뷰 내용
    - 별점
    - 갤리러 (pk gallery)
    - 카메라 (pk cameras)
---
likes
    - 유저 (pk users)
    - 갤러리 (pk gallery)

---
brands
    - 카메라 브랜드 명
    - 브랜드 설명
---
cameras
    - 카메라 모델명
    - 카메라 브랜드 (pk brands)
    - 카메라 화소
    - 카메라 iso
    - 카메라 손떨림보정
    - 가격
    - 출시일 
---
keys
    - 카메라 일련 번호
---
users
    - 아이디
    - 비밀번호
    - 이메일?
    - 이름
    - 별명 (닉네임)
    - 프로필 사진
    - 성별?
    - 소유한 카메라 (pk cameras)
    - 카메라 고유 번호 (모델번호? 정품키? pk key)
---
galleries
    - 제목
    - 설명
    - 해시태그 (pk tag)
    - 사진작가 (pk users)
    - 카메라 종류 (pk cameras)
    - 장소 (pk place)
--- 
tags
    - 태그명

---
place
    - 장소명
    - 주소
    - 도시
    - 나라



---------------------------
API LIST
/api/v1/galleries/ 
    /
    - 갤러리 목록
    /<int:pk>
    - 갤러리 자세히 보기


----
구글 계정 : cwDev99@gmail.com
---
Gallery
/api/v1/galleries - GET, POST
/api/v1/galleries/<Gallery ID> - GET

User
/api/v1/user - POST
/api/v1/user/activate/(uid)/token - GET
/api/v1/user/me - GET
/api/v1/user/change-password - POST
/api/v1/user/log-in - POST
/api/v1/user/log-out - POST

